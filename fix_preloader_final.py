import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the Webflow ix2 destroy script from the preloader
old_preloader_script = """  <script>
    // Trigger animation and hide preloader after 2.5 seconds
    window.addEventListener('DOMContentLoaded', function() {
      // Trigger transition by adding active class after a tiny delay
      setTimeout(function() {
        document.querySelector('#preloader .preloader-svg').classList.add('active');
      }, 50);

      setTimeout(function() {
        document.getElementById('preloader').classList.add('hidden');
        
        // Restart Webflow animations so they play now
        if (window.Webflow && window.Webflow.require('ix2')) {
           window.Webflow.require('ix2').init();
        }
      }, 2200);
    });

    // Pause Webflow animations initially
    var Webflow = Webflow || [];
    Webflow.push(function() {
      if (window.Webflow.require('ix2')) {
         window.Webflow.require('ix2').destroy();
      }
    });
  </script>"""

new_preloader_script = """  <script>
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

if old_preloader_script in html:
    html = html.replace(old_preloader_script, new_preloader_script)
else:
    print("Could not find old preloader script")

# 2. Remove the saomiguel.js tag from the bottom
script_tag = '<script src="./63734ddc258336c709b2a740/js/saomiguel.js" type="text/javascript"></script>'
if script_tag in html:
    html = html.replace(script_tag, '')
else:
    print("Could not find saomiguel script tag at the bottom")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
