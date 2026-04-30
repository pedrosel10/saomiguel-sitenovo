import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Robust pattern: match from swiper-wrapper start to the next div that is NOT a slide
# Better: match everything between the swiper-wrapper start and the pagination wrap start
pattern = re.compile(r'(<div role="list" class="swiper-wrapper mod--gallery w-dyn-items">)(.*?)(?=<div class="gallery__pagin-wrap">)', re.DOTALL)

def reverse_slides(match):
    prefix = match.group(1)
    content = match.group(2)
    
    # Each slide starts with <div role="listitem" class="swiper-slide mod--gallery w-dyn-item">
    # We find all occurrences and split
    slides = re.split(r'(?=<div role="listitem" class="swiper-slide mod--gallery w-dyn-item">)', content)
    # Filter out empty strings and the trailing whitespace/divs at the end of the list
    # The last element in 'slides' might contain the closing </div> of the wrapper.
    # We need to extract that closing </div>.
    
    # Actually, content ends with one or more </div> that close the wrapper.
    # Let's find where the last slide ends.
    slides = [s for s in slides if s.strip()]
    
    # The last slide string contains the </div> that closes the wrapper itself.
    # Let's find the last </div> in the last slide.
    # A slide has 4 opening divs: listitem, gallery__slide-content, img-logo-wrapper, overflow-hidden
    # Plus client-logo-card? No, client-logo-card is a sibling of overflow-hidden.
    # So:
    # <div role="listitem">
    #   <div class="gallery__slide-content">
    #     <div class="img-logo-wrapper">
    #       <div class="overflow-hidden"></div>
    #       <div class="client-logo-card"></div>
    #     </div>
    #   </div>
    # </div>
    # That's 3 closing divs at the end of a slide.
    
    # Let's just reverse the slides and handle the wrapper closing tag.
    # We can detect the wrapper closing tag by looking for the last </div> in 'content'.
    
    # Actually, a better way:
    # 1. Find all slide blocks using regex
    # 2. Extract them
    # 3. Replace the entire block of slides with reversed ones
    
    # Let's try finding all slides within the wrapper
    slide_pattern = re.compile(r'<div role="listitem" class="swiper-slide mod--gallery w-dyn-item">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    
    # This is still fragile. Let's use a simpler approach.
    # We know there are exactly 8 slides in each wrapper.
    return prefix + content + "REVERSE_ME" # Dummy to see if it matches

# Let's just do it manually with a python script that counts div depth
def reverse_gallery(html):
    parts = re.split(r'(<div role="list" class="swiper-wrapper mod--gallery w-dyn-items">)', html)
    new_parts = [parts[0]]
    for i in range(1, len(parts), 2):
        wrapper_start = parts[i]
        rest = parts[i+1]
        
        # Now we find the 8 slides in 'rest'
        slides = []
        current_pos = 0
        for _ in range(8):
            slide_start = rest.find('<div role="listitem"', current_pos)
            if slide_start == -1: break
            
            # Find the end of this slide by counting divs
            # A slide has specific depth. Let's just find the next slide start or the wrapper end.
            next_slide_start = rest.find('<div role="listitem"', slide_start + 20)
            if next_slide_start == -1:
                # Last slide. Find the end of the slides before the pagination.
                end_of_slides = rest.find('<div class="gallery__pagin-wrap"', slide_start)
                # The wrapper ends with some </div>s before the pagination
                # Let's look for the </div> that closes the swiper-wrapper
                # But it's easier to just take everything up to the wrapper end.
                # Actually, let's just use the next_slide_start logic.
                pass
            
        # Re-evaluating: swapping the src and logo numbers is MUCH safer and easier.
        # There are 8 images and 8 logos.
        # Original order: 08, 07, 06, 05, 04, 03, 02, 01
        # Target order: 01, 02, 03, 04, 05, 06, 07, 08
        pass

# NEW PLAN: Swap src numbers 01<->08, 02<->07, 03<->06, 04<->05
# This avoids DOM manipulation errors.
# But wait, there are 3 tabs. Each tab has the same set.
# So I can just replace all "08" with "TEMP08", then "01" with "08", then "TEMP08" with "01".

# Wait! The user says "as logos e imagens todas corretas. só preciso inverter a ordem".
# If I swap 01 and 08, then 01 becomes 08 and 08 becomes 01.
# Visually, the first slide (which was 08) becomes 01.
# The last slide (which was 01) becomes 08.
# This is exactly what the user wants!

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to swap the numbers in the filenames
# fotos_clientes/01_1x.webp <-> fotos_clientes/08_1x.webp
# logos_clientes/01_1_5x.webp <-> logos_clientes/08_1_5x.webp

for i in range(1, 5):
    j = 9 - i # 1->8, 2->7, 3->6, 4->5
    si = f"{i:02d}"
    sj = f"{j:02d}"
    
    # Swap photos
    html = html.replace(f'fotos_clientes/{si}_1x.webp', f'TEMP_PHOTO_{si}')
    html = html.replace(f'fotos_clientes/{sj}_1x.webp', f'fotos_clientes/{si}_1x.webp')
    html = html.replace(f'TEMP_PHOTO_{si}', f'fotos_clientes/{sj}_1x.webp')
    
    # Swap logos
    html = html.replace(f'logos_clientes/{si}_1_5x.webp', f'TEMP_LOGO_{si}')
    html = html.replace(f'logos_clientes/{sj}_1_5x.webp', f'logos_clientes/{si}_1_5x.webp')
    html = html.replace(f'TEMP_LOGO_{si}', f'logos_clientes/{sj}_1_5x.webp')
    
    # Swap alt texts
    html = html.replace(f'alt="Client Logo {si}"', f'TEMP_ALT_{si}')
    html = html.replace(f'alt="Client Logo {sj}"', f'alt="Client Logo {si}"')
    html = html.replace(f'TEMP_ALT_{si}', f'alt="Client Logo {sj}"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
