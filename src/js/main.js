// Init, nav, small interactions. Progressive enhancement only - every
// component in this file must already work acceptably with JS disabled.

(function initNavToggle() {
  var nav = document.querySelector(".site-nav");
  var toggle = document.querySelector("[data-nav-toggle]");
  if (!nav || !toggle) return;

  toggle.addEventListener("click", function () {
    var isOpen = nav.getAttribute("data-open") === "true";
    nav.setAttribute("data-open", isOpen ? "false" : "true");
    toggle.setAttribute("aria-expanded", isOpen ? "false" : "true");
  });

  nav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      nav.setAttribute("data-open", "false");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
})();

(function initContactForm() {
  var form = document.querySelector("[data-form='formspree']");
  var status = document.querySelector("[data-form-status]");
  if (!form || !status) return;

  form.addEventListener("submit", function (event) {
    if (form.getAttribute("action").indexOf("YOUR_FORM_ID") !== -1) {
      // Formspree form ID not yet configured - see state/QUESTIONS.md.
      // Let the native submit fall through rather than silently failing.
      return;
    }
    event.preventDefault();
    status.textContent = "Sending...";
    status.removeAttribute("data-state");

    fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    })
      .then(function (response) {
        if (response.ok) {
          status.textContent = "Thanks - we got your message and will be in touch soon.";
          status.setAttribute("data-state", "success");
          form.reset();
        } else {
          status.textContent = "Something went wrong. Please call us instead: (647) 732-1484.";
          status.setAttribute("data-state", "error");
        }
      })
      .catch(function () {
        status.textContent = "Something went wrong. Please call us instead: (647) 732-1484.";
        status.setAttribute("data-state", "error");
      });
  });
})();

(function initCalendlyLazyLoad() {
  var container = document.querySelector("[data-calendly-embed]");
  if (!container) return;
  var url = container.getAttribute("data-calendly-url");
  if (!url || url.indexOf("YOUR_CALENDLY_LINK") !== -1) {
    // Calendly link not yet configured - see state/QUESTIONS.md. Leave the
    // static fallback link (already in the markup) as the working path.
    return;
  }

  var loaded = false;
  var loadWidget = function () {
    if (loaded) return;
    loaded = true;
    var script = document.createElement("script");
    script.src = "https://assets.calendly.com/assets/external/widget.js";
    script.async = true;
    script.onload = function () {
      if (window.Calendly) {
        window.Calendly.initInlineWidget({ url: url, parentElement: container });
      }
    };
    document.body.appendChild(script);
  };

  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          loadWidget();
          observer.disconnect();
        }
      });
    });
    observer.observe(container);
  } else {
    loadWidget();
  }
})();
