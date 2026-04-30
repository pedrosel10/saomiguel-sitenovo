import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all slides
slides = soup.find_all('div', class_='swiper-slide mod--gallery w-dyn-item')

for slide in slides:
    content_div = slide.find('div', class_='gallery__slide-content')
    if not content_div:
        continue
        
    img = slide.find('img', class_='gallery__slide-img')
    if not img:
        continue
        
    src = img.get('src', '')
    # Match gallery-01 to gallery-08
    match = re.search(r'gallery-0?(\d)', src)
    if match:
        num = match.group(1)
        num_str = f"{int(num):02d}"
        
        # Check if card already exists
        existing_card = slide.find('div', class_='client-logo-card')
        if not existing_card:
            # Create the card
            # <div class="client-logo-card" data-swiper-gallery="anim">
            #   <img src="./logos_clientes/01_1_5x.webp" alt="Client Logo" class="client-logo-img">
            # </div>
            card = soup.new_tag('div', **{'class': 'client-logo-card', 'data-swiper-gallery': 'anim'})
            logo_img = soup.new_tag('img', src=f"./logos_clientes/{num_str}_1_5x.webp", alt=f"Client Logo {num_str}", **{'class': 'client-logo-img'})
            card.append(logo_img)
            
            # Append it to content_div
            content_div.append(card)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
