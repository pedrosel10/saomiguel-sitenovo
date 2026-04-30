import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_old_card = """    .client-logo-card {
      position: absolute;
      top: -1rem;
      right: -1rem;
      width: 7.5rem;
      height: 4rem;
      background-color: #0d0d0d;
      border: 1px solid #333;
      border-radius: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0.75rem;
      z-index: 10;
      overflow: hidden;
      opacity: 0;
    }"""

css_new_card = """    .client-logo-card {
      position: absolute;
      top: -1rem;
      right: -1rem;
      width: 7.5rem;
      height: 4rem;
      background-color: transparent;
      border: 1px solid transparent;
      border-radius: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0.75rem;
      z-index: 10;
      overflow: hidden;
      transition: background-color 0s 0s, border-color 0s 0s;
    }"""

html = html.replace(css_old_card, css_new_card)

css_old_active = """    .swiper-slide-active .client-logo-card,
    .client-logo-card.active {
      opacity: 1;
    }"""

css_new_active = """    .swiper-slide-active .client-logo-card,
    .client-logo-card.active {
      background-color: #0d0d0d;
      border-color: #333;
      transition: background-color 0s 0.75s, border-color 0s 0.75s;
    }"""

html = html.replace(css_old_active, css_new_active)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
