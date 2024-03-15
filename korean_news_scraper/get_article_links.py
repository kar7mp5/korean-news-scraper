"""
# get_article_links.py

When storing a lot of data in the Python list data type, 
there is a disadvantage of slowing down the speed, 
but a separate data type can be introduced later.
"""

from bs4 import BeautifulSoup
import requests
import urllib
import lxml

from tqdm import tqdm

from scroll_down_page import scroll_down_page


def get_article_links(lang: str, keyword: str) -> list[str]:
    """Get article's links

    :param lang: Select website language. You can use ['ko-KR', 'en-EN']
    :param keyword: Search keyword
    """

    # select language
    if lang == "ko-KR":
        url = f"https://news.google.com/search?q={urllib.parse.quote(keyword)}&hl=ko&gl=KR&ceid=KR%3Ako"
    elif lang == "en-EN":
        url = f"https://news.google.com/search?q={urllib.parse.quote(keyword)}&hl=en-US&gl=US&ceid=US:en"
    else:
        raise ValueError("\033[31mUnsupported Language. Try to use 'ko-KR' or 'en-EN'\033[0m")

    scroll_down_page(url)

    # get articles's url
    re = requests.get(url)
    soup = BeautifulSoup(re.text, "lxml")
    news_tags = soup.find_all('a', class_="WwrzSb")

    news_links = ["https://news.google.com/" + tag["href"][2:] for tag in news_tags]  # Links to articles


    return news_links