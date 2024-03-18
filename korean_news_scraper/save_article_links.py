"""
# save_article_links.py

Links from Google News articles for specific keywords are scraped and saved to CSV.
"""
# Library for scrapping
from bs4 import BeautifulSoup
import requests
import urllib
import lxml

# Library for writting scrapping data
import pandas as pd

# Library for loading bar
from tqdm import tqdm
import os


from scroll_down_page import scroll_down_page




def save_article_links(keywords: list, relative_path: str = "", lang: str = "ko-KR") -> None:
    """Get article's links

    :param keywords: Keywords; data type is list[str]
    :param relative_path: Data save relative path
    :param lang: Select website language. You can use ['ko-KR', 'en-EN']
    """

    for keyword in tqdm(keywords, desc="\033[36mSave scrapping data as .csv\033[0m", ncols=100):
        data = get_article_links(lang, keyword)

        df = pd.DataFrame(data)

        # save the data as .csv
        df.columns = ["News Links"]
        try:
            df.to_csv(f"{os.getcwd()}/{relative_path}/article_links/{keyword}.csv")
        except:
            print(f"\033[31m\nmkdir {relative_path}/article_links/\033[0m")
            print(f"\033[31m\nmkdir {relative_path}/article_contents/\033[0m")

            os.mkdir(f"{relative_path}")
            os.mkdir(f"{relative_path}/article_links")
            os.mkdir(f"{relative_path}/article_contents")

            df.to_csv(f"{os.getcwd()}/{relative_path}/article_links/{keyword}.csv")




def get_article_links(lang: str, keyword: str) -> list[str]:
    """Get article's links
    When storing a lot of data in the Python list data type, 
    there is a disadvantage of slowing down the speed, 
    but a separate data type can be introduced later.

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