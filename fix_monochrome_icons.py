import os

TARGET_DIR = "images/icons"
os.makedirs(TARGET_DIR, exist_ok=True)

# OpenAI official icon is monochromatic. On dark bg, it MUST be white.
# "Original color" for OpenAI usually means Black, which is invisible here.
# So we enforce White for visibility, which is the correct brand usage on dark.
OPENAI_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white">
  <path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0" fill-rule="evenodd"/>
</svg>"""

with open(f"{TARGET_DIR}/openai.svg", "w") as f:
    f.write(OPENAI_SVG)
print("Restored OpenAI (White)")

# Grok (xAI) - Keeping White for visibility
GROK_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 40">
  <text x="50" y="25" font-family="Arial, sans-serif" font-weight="bold" font-size="30" text-anchor="middle" fill="white">Grok</text>
</svg>"""

with open(f"{TARGET_DIR}/grok.svg", "w") as f:
    f.write(GROK_SVG)
print("Restored Grok (White)")
