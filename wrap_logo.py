import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace opening tag
html = html.replace(
    '<div class="overflow-hidden mod--gallery-slide">',
    '<div class="img-logo-wrapper" style="position: relative; display: block; width: 100%;"><div class="overflow-hidden mod--gallery-slide">'
)

# We need to close the `img-logo-wrapper` div AFTER each `.client-logo-card` div.
# Looking at the code:
# <div class="client-logo-card" data-swiper-gallery="anim"><img src="./logos_clientes/08_1_5x.webp" alt="Client Logo 08" class="client-logo-img"></div>
# We can replace this exact pattern:
html = re.sub(
    r'(<div class="client-logo-card" data-swiper-gallery="anim"><img src="./logos_clientes/\d{2}_1_5x.webp" alt="Client Logo \d{2}" class="client-logo-img"></div>)',
    r'\1</div>',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
