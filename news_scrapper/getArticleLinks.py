from bs4 import BeautifulSoup
import requests
import urllib

from scrollDownPage import scrollDownPage


def getArticleLinks(lang: str, keyword: str) -> list[str]:

    print("Extract articles links")

    # select language
    if lang == "ko-KR":
        url = f"https://news.google.com/search?q={urllib.parse.quote(keyword)}&hl=ko&gl=KR&ceid=KR%3Ako"
    elif lang == "en-EN":
        url = f"https://news.google.com/search?q={urllib.parse.quote(keyword)}&hl=en-US&gl=US&ceid=US:en"
    else:
        raise ValueError("Unsupported Language. Try to use 'ko-KR' or 'en-EN'")

    scrollDownPage(url)

    # get articles's url
    re = requests.get(url)
    soup = BeautifulSoup(re.text, "html.parser")
    news_tags = soup.find_all('a', class_="WwrzSb")
    news_links = ["https://news.google.com/" + tag["href"][2:] for tag in news_tags]  # Links to articles

    return news_links