import feedparser
import json
import requests
from datetime import datetime

RSS = "https://news.google.com/rss/search?q=technology"

feed = feedparser.parse(RSS)

articles = []

def generate_ai(text):
    # Replace with your API (OpenAI / OpenRouter)
    return text[:150] + "..."  # placeholder

for i, entry in enumerate(feed.entries[:5]):
    title = entry.title
    link = entry.link

    summary = generate_ai(title)

    image = f"https://picsum.photos/seed/{i}/600/400"

    articles.append({
        "title": title,
        "summary": summary,
        "link": link,
        "image": image
    })

with open("news.json", "w") as f:
    json.dump(articles, f, indent=2)
