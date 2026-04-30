import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the saomiguel.js script tag
html = html.replace('<script src="./63734ddc258336c709b2a740/js/saomiguel.js" type="text/javascript"></script>', '')

# 2. Update the preloader CSS and JS
old_preloader = """  <style>
    #preloader {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: #000000;
      z-index: 99999;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: opacity 0.8s cubic-bezier(0.77, 0, 0.175, 1), visibility 0.8s;
    }"""

new_preloader = """  <style>
    #preloader {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: #000000;
      z-index: 99999;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: opacity 0.8s cubic-bezier(0.77, 0, 0.175, 1), visibility 0.8s;
    }
    #preloader .preloader-svg {
      width: 120px;
      height: auto;
    }"""

html = html.replace(old_preloader, new_preloader)

old_script = """      setTimeout(function() {
        document.getElementById('preloader').classList.add('hidden');
      }, 2200);"""

new_script = """      setTimeout(function() {
        document.getElementById('preloader').classList.add('hidden');
        
        // Delay entrance animations by loading the main script after preloader finishes
        let smScript = document.createElement('script');
        smScript.src = "./63734ddc258336c709b2a740/js/saomiguel.js";
        smScript.type = "text/javascript";
        document.body.appendChild(smScript);
      }, 2200);"""

html = html.replace(old_script, new_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
