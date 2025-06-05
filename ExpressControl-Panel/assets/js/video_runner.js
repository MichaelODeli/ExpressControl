document.addEventListener('DOMContentLoaded', function () {
  var enable = false;  // Параметр, который управляет выполнением

  if (!enable) {
    console.log('vidbg отключён параметром enable = false');
    return; // Выход из кода, если enable == false
  }

  var instance = null;

  function checkVidbg() {
    var hasElement = !!document.querySelector('div.train-manage-grid');
    if (hasElement && !instance) {
      instance = new vidbg(
        "body",
        {
          mp4: "https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_720p_h264.mov",
          overlay: false,
        },
        {}
      );
      console.log('vidbg запущен');
    } else if (!hasElement && instance) {
      instance.destroy();
      instance = null;
      console.log('vidbg остановлен');
    }
  }

  checkVidbg();

  var observer = new MutationObserver(function(mutations) {
    checkVidbg();
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
});