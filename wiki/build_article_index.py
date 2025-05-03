import os
import json

ARTICLES_DIR = "articles"
OUTPUT_FILE = os.path.join(ARTICLES_DIR, "index.json")

def build_index():
    articles = []
    for filename in os.listdir(ARTICLES_DIR):
        if filename.endswith(".html"):
            slug = filename[:-5]  # remove .html
            articles.append(slug)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(sorted(articles), f, indent=2)

    print(f"✅ index.json written to {OUTPUT_FILE} ({len(articles)} entries)")

if __name__ == "__main__":
    build_index()
