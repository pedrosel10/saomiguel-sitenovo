import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the glitch and inline style by adding a class and removing inline
old_inline = 'style="position: relative; display: block; width: fit-content; margin: 0 auto;"'
html = html.replace(old_inline, '')

# Add the CSS for img-logo-wrapper and update client-logo-card
css_old = """    .client-logo-card::after {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: #1a2bc2;
      transform: translateX(-101%);
      z-index: 20;
    }"""

css_new = """    .img-logo-wrapper {
      position: relative;
      display: block;
      width: fit-content;
      margin: 0 auto;
      /* Fix 3D glitching during swiper scroll */
      transform: translateZ(0);
      z-index: 2;
    }

    .client-logo-card::after {
      content: "";
      position: absolute;
      /* Expand by 1px to cover the border */
      top: -1px;
      left: -1px;
      width: calc(100% + 2px);
      height: calc(100% + 2px);
      background-color: #1a2bc2;
      transform: translateX(-101%);
      z-index: 20;
    }"""

html = html.replace(css_old, css_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
