import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all swiper-wrapper mod--gallery w-dyn-items
pattern = re.compile(r'(<div role="list" class="swiper-wrapper mod--gallery w-dyn-items">)(.*?)(</div>\s*</div>)', re.DOTALL)

def reverse_slides(match):
    prefix = match.group(1)
    content = match.group(2)
    suffix = match.group(3)
    
    # Split content into slides
    # Each slide starts with <div role="listitem" class="swiper-slide mod--gallery w-dyn-item">
    slides = re.split(r'(?=<div role="listitem" class="swiper-slide mod--gallery w-dyn-item">)', content)
    # Filter out empty strings
    slides = [s.strip() for s in slides if s.strip()]
    
    # Reverse the order
    slides.reverse()
    
    return prefix + '\n' + '\n'.join(slides) + '\n' + suffix

new_html = pattern.sub(reverse_slides, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
