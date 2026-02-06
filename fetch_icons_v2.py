import urllib.request
import os
import re

TARGET_DIR = "images/icons"
os.makedirs(TARGET_DIR, exist_ok=True)

# Sources
SOURCES = {
    "n8n": "https://unpkg.com/simple-icons@latest/icons/n8n.svg",
    "python": "https://unpkg.com/simple-icons@latest/icons/python.svg",
    "docker": "https://unpkg.com/simple-icons@latest/icons/docker.svg",
    "anthropic": "https://unpkg.com/simple-icons@latest/icons/anthropic.svg",
    "googlegemini": "https://unpkg.com/simple-icons@latest/icons/googlegemini.svg",
    "openai": "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" 
}

# Grok Manual Generation (Text based, high contrast)
GROK_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 40">
  <text x="50" y="25" font-family="Arial, sans-serif" font-weight="bold" font-size="30" text-anchor="middle" fill="white">Grok</text>
</svg>"""

def fetch_and_process(name, url):
    print(f"Processing {name}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            svg_content = response.read().decode('utf-8')
            
            # Force White Fill
            # 1. Remove existing fill attributes
            svg_content = re.sub(r'fill="[^"]*"', '', svg_content)
            
            # 2. Add fill="white" to svg tag
            if '<svg' in svg_content:
                svg_content = svg_content.replace('<svg', '<svg fill="white"', 1)
            
            # 3. Save
            with open(f"{TARGET_DIR}/{name}.svg", "w", encoding='utf-8') as f:
                f.write(svg_content)
            print(f"-> Saved {name}.svg")
            return True
    except Exception as e:
        print(f"-> Error fetching {name}: {e}")
        return False

# 1. Fetch Standard Icons
for name, url in SOURCES.items():
    fetch_and_process(name, url)

# 2. Save Grok
with open(f"{TARGET_DIR}/grok.svg", "w", encoding='utf-8') as f:
    f.write(GROK_svg)
print("-> Saved grok.svg")
