import requests
from bs4 import BeautifulSoup


def parse_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    res = []

    span_elements = soup.find_all(
        "span",
        class_="bloko-tag__section bloko-tag__section_text",
        attrs={"data-qa": "bloko-tag__text"},
    )

    for span in span_elements:
        res.append(span.get_text())

    return res
