import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the SVG string
svg_match = re.search(r'let svg = `(<svg class="heading__hieroglyphs".*?</svg>)`', html, re.DOTALL)
if not svg_match:
    print("Could not find SVG")
    exit(1)

svg_content = svg_match.group(1)

# Modify the SVG class so it starts animating immediately or we control it
# Actually, the existing CSS targets `svg.heading__hieroglyphs.active .svg-elem-*`
# We can just change the class to "heading__hieroglyphs preloader-svg active"
preloader_svg = svg_content.replace('class="heading__hieroglyphs"', 'class="heading__hieroglyphs preloader-svg active"')

preloader_html = f"""
  <style>
    #preloader {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: #000000;
      z-index: 99999;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: opacity 0.8s cubic-bezier(0.77, 0, 0.175, 1), visibility 0.8s;
    }}
    #preloader.hidden {{
      opacity: 0;
      visibility: hidden;
    }}
    /* Speed up the animation for the preloader specifically */
    #preloader .heading__hieroglyphs .svg-elem-1 {{ transition-delay: 0.1s; }}
    #preloader .heading__hieroglyphs .svg-elem-2 {{ transition-delay: 0.2s; }}
    #preloader .heading__hieroglyphs .svg-elem-3 {{ transition-delay: 0.3s; }}
    #preloader .heading__hieroglyphs .svg-elem-4 {{ transition-delay: 0.4s; }}
    #preloader .heading__hieroglyphs .svg-elem-5 {{ transition-delay: 0.5s; }}
    #preloader .heading__hieroglyphs .svg-elem-6 {{ transition-delay: 0.6s; }}
    #preloader .heading__hieroglyphs .svg-elem-7 {{ transition-delay: 0.7s; }}
    #preloader .heading__hieroglyphs .svg-elem-8 {{ transition-delay: 0.8s; }}
    #preloader .heading__hieroglyphs .svg-elem-9 {{ transition-delay: 0.9s; }}
    #preloader .heading__hieroglyphs .svg-elem-10 {{ transition-delay: 1.0s; }}
    #preloader .heading__hieroglyphs .svg-elem-11 {{ transition-delay: 1.1s; }}
    #preloader .heading__hieroglyphs .svg-elem-12 {{ transition-delay: 1.2s; }}
    #preloader .heading__hieroglyphs .svg-elem-13 {{ transition-delay: 1.3s; }}
    #preloader .heading__hieroglyphs .svg-elem-14 {{ transition-delay: 1.4s; }}
    #preloader .heading__hieroglyphs .svg-elem-15 {{ transition-delay: 1.5s; }}
    #preloader .heading__hieroglyphs .svg-elem-16 {{ transition-delay: 1.6s; }}
    
    #preloader .heading__hieroglyphs path {{
        transition-duration: 0.4s !important;
    }}
  </style>
  <div id="preloader">
    {preloader_svg}
  </div>
  <script>
    // Hide preloader after 2.5 seconds (allows animation to finish)
    window.addEventListener('DOMContentLoaded', function() {{
      setTimeout(function() {{
        document.getElementById('preloader').classList.add('hidden');
      }}, 2200);
    }});
  </script>
"""

# Find the body tag and insert the preloader
body_match = re.search(r'<body[^>]*>', html)
if body_match:
    body_tag = body_match.group(0)
    html = html.replace(body_tag, body_tag + '\n' + preloader_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Preloader added successfully")
