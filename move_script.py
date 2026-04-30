import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove it from the top
html = html.replace('<script src="./63734ddc258336c709b2a740/js/saomiguel.js" type="text/javascript"></script>', '')

# Put it back at the end of the body (before </body>)
html = html.replace('</body>', '<script src="./63734ddc258336c709b2a740/js/saomiguel.js" type="text/javascript"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
