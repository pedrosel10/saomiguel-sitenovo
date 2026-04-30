import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_func(match):
    # match.group(0) is the entire `<div data-swiper-gallery="anim" class="gallery__slide-content active">...</div>` up to the closing div of the `gallery__slide-content`.
    # Wait, regex is tricky for nested divs.
    # We can just match the img tag to get the number, and then insert the logo just after the img's closing tag or parent div.
    pass

# Better logic:
# Find all `<div class="overflow-hidden mod--gallery-slide">` and its contents up to `</div>`
# Wait, the structure is:
# <div data-swiper-gallery="anim" class="gallery__slide-content active">
#   <div data-swiper-gallery="anim" class="gallery__slide-title active">Concept Visualization</div>
#   <div class="overflow-hidden mod--gallery-slide">
#     <img ... src="...gallery-08.png" ... />
#   </div>
# </div>

# Let's find each gallery__slide-img
matches = list(re.finditer(r'<img[^>]*class="gallery__slide-img"[^>]*>', html))
# We must iterate backwards to not mess up indices
for match in reversed(matches):
    img_tag = match.group(0)
    src_match = re.search(r'gallery-0?(\d)', img_tag)
    if src_match:
        num = src_match.group(1)
        num_str = f"{int(num):02d}"
        
        logo_html = f'\n                      <div class="client-logo-card" data-swiper-gallery="anim"><img src="./logos_clientes/{num_str}_1_5x.webp" alt="Client Logo {num_str}" class="client-logo-img"></div>'
        
        # Insert logo_html after the `</div>` that closes `<div class="overflow-hidden mod--gallery-slide">`
        # Or better, just put it right after the `<img>` tag!
        # Wait, the `<img>` tag is inside `div.overflow-hidden mod--gallery-slide`.
        # If I put it inside `overflow-hidden`, and the logo has `position: absolute; right: -15px`, it will be cut off by `overflow: hidden`.
        # So I need to put it OUTSIDE the `overflow-hidden` div.
        # The `overflow-hidden` div ends with `</div>`.
        # How to find the `</div>` after the `<img>`?
        
        # img_tag ends at match.end().
        # The next `</div>` after match.end() is the closing tag for the `overflow-hidden` div.
        end_idx = html.find('</div>', match.end())
        if end_idx != -1:
            # Insert logo_html after `</div>` (which is end_idx + 6)
            insert_pos = end_idx + 6
            html = html[:insert_pos] + logo_html + html[insert_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
