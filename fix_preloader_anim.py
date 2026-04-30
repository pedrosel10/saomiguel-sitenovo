import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the active class in the preloader SVG
html = html.replace('class="heading__hieroglyphs preloader-svg active"', 'class="heading__hieroglyphs preloader-svg"')

# Update the script to add the class after load
script_old = """  <script>
    // Hide preloader after 2.5 seconds (allows animation to finish)
    window.addEventListener('DOMContentLoaded', function() {
      setTimeout(function() {
        document.getElementById('preloader').classList.add('hidden');
      }, 2200);
    });
  </script>"""

script_new = """  <script>
    // Trigger animation and hide preloader after 2.5 seconds
    window.addEventListener('DOMContentLoaded', function() {
      // Trigger transition by adding active class after a tiny delay
      setTimeout(function() {
        document.querySelector('#preloader .preloader-svg').classList.add('active');
      }, 50);

      setTimeout(function() {
        document.getElementById('preloader').classList.add('hidden');
      }, 2200);
    });
  </script>"""

html = html.replace(script_old, script_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
