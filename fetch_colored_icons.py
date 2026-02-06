import urllib.request
import os

TARGET_DIR = "images/icons"
os.makedirs(TARGET_DIR, exist_ok=True)

# Using Simple Icons CDN which returns brand colors by default
ICONS = {
    "n8n": "https://cdn.simpleicons.org/n8n", # Pink/Orange
    "python": "https://cdn.simpleicons.org/python", # Blue/Yellow gradient or multi-path usually
    "docker": "https://cdn.simpleicons.org/docker", # Blue
    "anthropic": "https://cdn.simpleicons.org/anthropic", # Claude (Terracotta)
    "googlegemini": "https://cdn.simpleicons.org/googlegemini", # Blue/Purple
    "openai": "https://cdn.simpleicons.org/openai", # Purple/Black
}

def download_icon(name, url):
    print(f"Fetching {name}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            content = response.read()
            # Write directly
            with open(f"{TARGET_DIR}/{name}.svg", "wb") as f:
                f.write(content)
            print(f"-> Saved {name}.svg")
            return True
    except Exception as e:
        print(f"-> Error fetching {name}: {e}")
        return False

# Download standard icons
for name, url in ICONS.items():
    download_icon(name, url)

# Manual Grok (xAI) - Keeping White for contrast as it doesn't have a strong brand color other than Black/White
# and Black is invisible on Navy.
GROK_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 40">
  <text x="50" y="25" font-family="Arial, sans-serif" font-weight="bold" font-size="30" text-anchor="middle" fill="white">Grok</text>
</svg>"""

with open(f"{TARGET_DIR}/grok.svg", "w") as f:
    f.write(GROK_SVG)
print("-> Saved grok.svg (kept white for visibility)")
