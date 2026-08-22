export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Direct routing for agency portal and vertical dashboards
    let htmlContent = "";

    if (path === "/" || path === "/index.html") {
      return new Response(PORTAL_HTML, {
        headers: { "content-type": "text/html;charset=UTF-8" }
      });
    }

    return new Response(PORTAL_HTML, {
      headers: { "content-type": "text/html;charset=UTF-8" }
    });
  }
};

const PORTAL_HTML = `<!-- INJECTED_PORTAL_HTML -->`;
