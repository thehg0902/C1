// Init, nav, small interactions. Progressive enhancement only - every
// component in this file must already work acceptably with JS disabled.

(function initLoadingScreen() {
  var screen = document.getElementById("loading-screen");
  if (!screen) return;

  var MIN_DISPLAY_MS = 500;
  var start = Date.now();

  var hide = function () {
    var wait = Math.max(MIN_DISPLAY_MS - (Date.now() - start), 0);
    setTimeout(function () {
      screen.classList.add("is-hidden");
      screen.addEventListener("transitionend", function () { screen.remove(); }, { once: true });
      // Fallback in case transitionend never fires (e.g. reduced motion).
      setTimeout(function () { if (screen.parentNode) screen.remove(); }, 700);
    }, wait);
  };

  if (document.readyState === "complete") {
    hide();
  } else {
    window.addEventListener("load", hide);
  }
})();

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
      // Formspree form ID not yet configured.
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
    // Calendly link not yet configured. Leave the static fallback link
    // (already in the markup) as the working path.
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

(function initTestimonialCarousel() {
  var root = document.querySelector("[data-carousel]");
  if (!root) return;
  var track = root.querySelector(".testimonial-carousel__track");
  var slides = track ? Array.prototype.slice.call(track.children) : [];
  var prevBtn = root.querySelector("[data-carousel-prev]");
  var nextBtn = root.querySelector("[data-carousel-next]");
  var dotsWrap = root.querySelector("[data-carousel-dots]");
  if (!track || !slides.length || !prevBtn || !nextBtn || !dotsWrap) return;

  root.classList.add("is-ready");

  var AUTO_MS = 6000;
  var reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  var index = 0;
  var timer = null;

  slides.forEach(function (_, i) {
    var dot = document.createElement("button");
    dot.type = "button";
    dot.className = "testimonial-carousel__dot";
    dot.setAttribute("role", "tab");
    dot.setAttribute("aria-label", "Go to testimonial " + (i + 1));
    dot.setAttribute("aria-selected", i === 0 ? "true" : "false");
    dot.addEventListener("click", function () {
      goTo(i);
      restartAuto();
    });
    dotsWrap.appendChild(dot);
  });
  var dots = Array.prototype.slice.call(dotsWrap.children);

  function update() {
    slides.forEach(function (slide, i) {
      slide.classList.toggle("is-active", i === index);
    });
    dots.forEach(function (dot, i) {
      dot.setAttribute("aria-selected", i === index ? "true" : "false");
    });
  }

  function goTo(i) {
    index = (i + slides.length) % slides.length;
    update();
  }

  function next() {
    goTo(index + 1);
  }

  function prev() {
    goTo(index - 1);
  }

  function startAuto() {
    if (reduceMotion) return;
    timer = setInterval(next, AUTO_MS);
  }

  function stopAuto() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  function restartAuto() {
    stopAuto();
    startAuto();
  }

  prevBtn.addEventListener("click", function () {
    prev();
    restartAuto();
  });
  nextBtn.addEventListener("click", function () {
    next();
    restartAuto();
  });

  root.addEventListener("mouseenter", stopAuto);
  root.addEventListener("mouseleave", startAuto);
  root.addEventListener("focusin", stopAuto);
  root.addEventListener("focusout", startAuto);

  update();
  startAuto();
})();
