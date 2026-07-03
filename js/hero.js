// Hero video playback: play once on first visit, then freeze on the last
// frame. Returning visitors and prefers-reduced-motion see the frozen
// frame immediately (poster stands in until metadata loads).

(function initHeroVideo() {
  var video = document.querySelector("[data-hero-video]");
  if (!video) return;

  var STORAGE_KEY = "cplusroofing:heroPlayed";
  var reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  var alreadyPlayed = false;
  try {
    alreadyPlayed = localStorage.getItem(STORAGE_KEY) === "1";
  } catch (e) {
    // localStorage unavailable (private mode, etc.) - fall back to
    // playing once per page load, no persistence.
  }

  var freezeOnLastFrame = function () {
    if (video.duration && isFinite(video.duration)) {
      video.currentTime = Math.max(video.duration - 0.05, 0);
    }
    video.pause();
  };

  if (reduceMotion || alreadyPlayed) {
    video.addEventListener("loadedmetadata", freezeOnLastFrame, {
      once: true,
    });
    return;
  }

  video.addEventListener(
    "ended",
    function () {
      freezeOnLastFrame();
      try {
        localStorage.setItem(STORAGE_KEY, "1");
      } catch (e) {
        // ignore
      }
    },
    { once: true }
  );

  var playPromise = video.play();
  if (playPromise && typeof playPromise.catch === "function") {
    playPromise.catch(function () {
      // Autoplay blocked - the poster frame is a complete hero on its own.
    });
  }
})();
