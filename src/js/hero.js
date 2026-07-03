// Hero video playback: loop continuously (native `loop` attribute on the
// <video> handles the repeat). Respects prefers-reduced-motion - those
// users never get autoplay and see the static poster frame instead.

(function initHeroVideo() {
  var video = document.querySelector("[data-hero-video]");
  if (!video) return;

  var reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  if (reduceMotion) return;

  var playPromise = video.play();
  if (playPromise && typeof playPromise.catch === "function") {
    playPromise.catch(function () {
      // Autoplay blocked - the poster frame is a complete hero on its own.
    });
  }
})();
