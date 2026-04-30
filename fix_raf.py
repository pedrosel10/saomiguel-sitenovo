import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update the script to mock RAF parameter
old_script = """    window.performance.now = function() {
      if (timePaused) return perfPauseTime;
      return originalPerfNow.call(window.performance) - perfOffset;
    };
    Date.now = function() {
      if (timePaused) return datePauseTime;
      return originalDateNow.call(Date) - dateOffset;
    };"""

new_script = """    window.performance.now = function() {
      if (timePaused) return perfPauseTime;
      return originalPerfNow.call(window.performance) - perfOffset;
    };
    Date.now = function() {
      if (timePaused) return datePauseTime;
      return originalDateNow.call(Date) - dateOffset;
    };

    var originalRAF = window.requestAnimationFrame;
    window.requestAnimationFrame = function(callback) {
      return originalRAF.call(window, function(time) {
        if (timePaused) {
           callback(perfPauseTime);
        } else {
           callback(time - perfOffset);
        }
      });
    };"""

if old_script in html:
    html = html.replace(old_script, new_script)
else:
    print("Could not find the script block to replace")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
