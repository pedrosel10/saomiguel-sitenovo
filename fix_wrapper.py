import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    'style="position: relative; display: block; width: 100%;"',
    'style="position: relative; display: block; width: fit-content; margin: 0 auto;"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
