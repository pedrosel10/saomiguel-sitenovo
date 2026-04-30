import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove dynamic injection script
old_preloader_script = """  <script>
    // Trigger animation and hide preloader after 2.5 seconds
    window.addEventListener('DOMContentLoaded', function() {
      setTimeout(function() {
        document.querySelector('#preloader .preloader-svg').classList.add('active');
      }, 50);

      setTimeout(function() {
        document.getElementById('preloader').classList.add('hidden');
        
        // Load the main site script dynamically
        let smScript = document.createElement('script');
        smScript.src = "./63734ddc258336c709b2a740/js/saomiguel.js";
        smScript.type = "text/javascript";
        smScript.onload = function() {
            // Trigger load events so Webflow's page load interactions run NOW
            window.dispatchEvent(new Event('load'));
            if (window.jQuery) {
                $(window).trigger('load');
            }
        };
        document.body.appendChild(smScript);
      }, 2200);
    });
  </script>"""

new_preloader_script = """  <script>
    // Freeze time to pause Webflow IX2 animations
    var originalPerfNow = window.performance.now;
    var originalDateNow = Date.now;
    var perfPauseTime = originalPerfNow.call(window.performance);
    var datePauseTime = originalDateNow.call(Date);
    var timePaused = true;
    var perfOffset = 0;
    var dateOffset = 0;

    window.performance.now = function() {
      if (timePaused) return perfPauseTime;
      return originalPerfNow.call(window.performance) - perfOffset;
    };
    Date.now = function() {
      if (timePaused) return datePauseTime;
      return originalDateNow.call(Date) - dateOffset;
    };

    window.addEventListener('DOMContentLoaded', function() {
      setTimeout(function() {
        var svg = document.querySelector('#preloader .preloader-svg');
        if (svg) svg.classList.add('active');
      }, 50);

      setTimeout(function() {
        var preloader = document.getElementById('preloader');
        if (preloader) preloader.classList.add('hidden');
        
        // Unpause time so Webflow animations resume from frame 0
        perfOffset = originalPerfNow.call(window.performance) - perfPauseTime;
        dateOffset = originalDateNow.call(Date) - datePauseTime;
        timePaused = false;
        
      }, 2200);
    });
  </script>"""

html = html.replace(old_preloader_script, new_preloader_script)

# 2. Add saomiguel.js back to the bottom of the page
if '<script src="./63734ddc258336c709b2a740/js/saomiguel.js"' not in html:
    html = html.replace('</body>', '  <script src="./63734ddc258336c709b2a740/js/saomiguel.js" type="text/javascript"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
