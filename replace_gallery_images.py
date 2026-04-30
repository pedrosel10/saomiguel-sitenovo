import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the gallery images and their surrounding attributes
# We target the class "gallery__slide-img"
img_pattern = re.compile(r'<img[^>]*class="gallery__slide-img"[^>]*>')

def replace_image(match):
    img_tag = match.group(0)
    
    # Find the number in the existing src (e.g., gallery-08 or gallery-01)
    num_match = re.search(r'gallery-0?(\d)', img_tag)
    if num_match:
        num = int(num_match.group(1))
        num_str = f"{num:02d}"
        
        # New src
        new_src = f'./fotos_clientes/{num_str}_1x.webp'
        
        # Replace src attribute
        new_tag = re.sub(r'src="[^"]*"', f'src="{new_src}"', img_tag)
        
        # Remove srcset if it exists
        new_tag = re.sub(r'\s*srcset="[^"]*"', '', new_tag)
        
        return new_tag
    
    return img_tag

new_html = img_pattern.sub(replace_image, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
