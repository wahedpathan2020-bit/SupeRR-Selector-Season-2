import json
import os
import template_styles
import template_scripts
import template_html

print("Loading data...")
with open("dashboard_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

raw_data_json = json.dumps(data)
css_content = template_styles.CSS_CONTENT
js_content = template_scripts.JS_CONTENT

print("Assembling HTML...")
html = template_html.HTML_TEMPLATE
html = html.replace("{css_content}", css_content)
html = html.replace("{js_content}", js_content)
html = html.replace("{raw_data_json}", raw_data_json)

out_file = "index.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Successfully generated {out_file} ({os.path.getsize(out_file):,} bytes)!")

