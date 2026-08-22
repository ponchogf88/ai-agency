#!/usr/bin/env python3
"""
Pipeline orchestrator: vigila carpetas del funnel y mueve archivos
según la lógica de transición definida.
"""

from __future__ import annotations

import json
import shutil
import sys
import time
from pathlib import Path
from threading import Lock, Thread

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver

from builder import build_assets

# Carpetas del pipeline (relativas al directorio de trabajo)
STAGES = (
    "01_leads_raw",
    "02_diagnosed",
    "03_assets_ready",
    "04_ready_to_pitch",
    "05_outreach_sent",
    "06_responses",
)

# (carpeta_origen, mensaje_consola, carpeta_destino)
TRANSITIONS: dict[str, tuple[str, str]] = {
    "01_leads_raw": (
        "[SCOUT -> DIAGNOSER] Procesando lead...",
        "02_diagnosed",
    ),
    "02_diagnosed": (
        "[DIAGNOSER -> BUILDER/FILMER] Generando assets...",
        "03_assets_ready",
    ),
    "03_assets_ready": (
        "[CHECKER] Auditando calidad...",
        "04_ready_to_pitch",
    ),
    "04_ready_to_pitch": (
        "[PITCHER/MOBILE] Preparando hardware móvil...",
        "05_outreach_sent",
    ),
}

PROCESS_DELAY_SECONDS = 2
MOVE_RETRIES = 8
MOVE_RETRY_DELAY_SECONDS = 0.25


class PipelineOrchestrator(FileSystemEventHandler):
    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir.resolve()
        self._processing: set[str] = set()
        self._lock = Lock()

    def _stage_name(self, path: Path) -> str | None:
        try:
            rel = path.relative_to(self.base_dir)
            if rel.parts:
                return rel.parts[0]
        except ValueError:
            pass
        return None

    def _is_valid_file(self, path: Path) -> bool:
        if not path.is_file():
            return False
        name = path.name
        if name.startswith("."):
            return False
        return True

    def _claim(self, key: str) -> bool:
        with self._lock:
            if key in self._processing:
                return False
            self._processing.add(key)
            return True

    def _release(self, key: str) -> None:
        with self._lock:
            self._processing.discard(key)

    def on_created(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        self._handle_path(Path(event.src_path))

    def on_moved(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        dest = getattr(event, "dest_path", None)
        if dest:
            self._handle_path(Path(dest))

    def _handle_path(self, path: Path) -> None:
        path = path.resolve()
        if not self._is_valid_file(path):
            return

        stage = self._stage_name(path)
        if stage not in TRANSITIONS:
            return

        key = str(path)
        if not self._claim(key):
            return

        message, dest_stage = TRANSITIONS[stage]
        Thread(
            target=self._process_transition,
            args=(path, message, dest_stage, key),
            daemon=True,
        ).start()

    def _process_transition(
        self,
        src: Path,
        message: str,
        dest_stage: str,
        claim_key: str,
    ) -> None:
        try:
            print(message, flush=True)
            time.sleep(PROCESS_DELAY_SECONDS)

            if not src.exists():
                return

            if self._stage_name(src) == "02_diagnosed":
                try:
                    build_assets(src, self.base_dir / "03_assets_ready")
                except (OSError, ValueError, json.JSONDecodeError) as exc:
                    print(f"  [ERROR] Builder falló para '{src.name}': {exc}", file=sys.stderr, flush=True)

            dest_dir = self.base_dir / dest_stage
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / src.name

            if dest.exists():
                stem = src.stem
                suffix = src.suffix
                dest = dest_dir / f"{stem}_{int(time.time() * 1000)}{suffix}"

            self._safe_move(src, dest)
        finally:
            self._release(claim_key)

    def _safe_move(self, src: Path, dest: Path) -> None:
        last_error: Exception | None = None
        for attempt in range(1, MOVE_RETRIES + 1):
            try:
                if not src.exists():
                    return
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dest))
                print(f"  -> Movido: {src.name} -> {dest.parent.name}/", flush=True)
                return
            except (OSError, shutil.Error) as exc:
                last_error = exc
                if attempt < MOVE_RETRIES:
                    time.sleep(MOVE_RETRY_DELAY_SECONDS)
        print(
            f"  [ERROR] No se pudo mover '{src}' tras {MOVE_RETRIES} intentos: {last_error}",
            file=sys.stderr,
            flush=True,
        )


def ensure_directories(base_dir: Path) -> None:
    for name in STAGES:
        (base_dir / name).mkdir(parents=True, exist_ok=True)


def create_observer() -> Observer:
    """Elige el observer más compatible (FSEvents falla en algunos entornos)."""
    if sys.platform == "darwin":
        try:
            from watchdog.observers.kqueue import KqueueObserver

            return KqueueObserver()
        except (ImportError, OSError, SystemError):
            pass
    try:
        return Observer()
    except (OSError, SystemError):
        pass
    return PollingObserver(timeout=1.0)


def main() -> None:
    base_dir = Path.cwd()
    ensure_directories(base_dir)

    handler = PipelineOrchestrator(base_dir)
    observer = create_observer()

    for name in STAGES:
        watch_path = base_dir / name
        observer.schedule(handler, str(watch_path), recursive=False)

    print("Orchestrator iniciado. Vigilando pipeline:", flush=True)
    for name in STAGES:
        print(f"  - {base_dir / name}", flush=True)
    print("Transiciones activas hasta 05_outreach_sent. Ctrl+C para salir.\n", flush=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo orchestrator...", flush=True)
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
