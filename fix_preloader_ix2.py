import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the CSS for the preloader SVG to ignore the absolute positioning
old_preloader_css = """    #preloader .preloader-svg {
      width: 120px;
      height: auto;
    }"""
new_preloader_css = """    #preloader .preloader-svg {
      width: 120px !important;
      height: auto !important;
      position: static !important;
      top: auto !important;
      left: auto !important;
      transform: none !important;
    }"""
html = html.replace(old_preloader_css, new_preloader_css)

# 2. Update the preloader script and restore saomiguel.js
old_script = """      setTimeout(function() {
        document.getElementById('preloader').classList.add('hidden');
        
        // Delay entrance animations by loading the main script after preloader finishes
        let smScript = document.createElement('script');
        smScript.src = "./63734ddc258336c709b2a740/js/saomiguel.js";
        smScript.type = "text/javascript";
        document.body.appendChild(smScript);
      }, 2200);
    });
  </script>"""

new_script = """      setTimeout(function() {
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
  </script>
  <script src="./63734ddc258336c709b2a740/js/saomiguel.js" type="text/javascript"></script>"""

html = html.replace(old_script, new_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
