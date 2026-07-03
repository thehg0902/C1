// Scroll entrance animations - CSS-only stack flag, so this JS only toggles
// classes; every transition/keyframe itself lives in base.css wrapped in
// @media (prefers-reduced-motion: no-preference).

(function initEntranceAnimations() {
  var reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  if (reduceMotion || !("IntersectionObserver" in window)) return;

  document.body.classList.add("anim-ready");

  var targets = document.querySelectorAll("[data-animate]");
  targets.forEach(function (el, index) {
    el.style.setProperty("--stagger-i", index % 6);
  });

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  targets.forEach(function (el) {
    observer.observe(el);
  });
})();
