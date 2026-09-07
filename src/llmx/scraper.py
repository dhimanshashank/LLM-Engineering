"""Fetch a page and return readable text. From week 1 day 1, reused everywhere after."""

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    )
}


def _soup(url):
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def fetch_website_contents(url, limit=2_000):
    """Title plus body text, stripped of scripts/styles, truncated to `limit` chars."""
    soup = _soup(url)
    title = soup.title.string if soup.title else "No title found"
    if not soup.body:
        return title
    for tag in soup.body(["script", "style", "img", "input"]):
        tag.decompose()
    text = soup.body.get_text(separator="\n", strip=True)
    return f"{title}\n\n{text}"[:limit]


def fetch_website_links(url):
    """Every href on the page, unfiltered. Let the LLM decide which ones matter."""
    return [a.get("href") for a in _soup(url).find_all("a") if a.get("href")]
