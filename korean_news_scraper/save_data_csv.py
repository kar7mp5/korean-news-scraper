"""
# google-news-scraper.py

Links from Google News articles for specific keywords are scraped and saved to CSV.
"""

import pandas as pd
import os

from tqdm import tqdm

from get_article_links import get_article_links


def save_data_csv(keywords: list, relative_path: str = "", lang: str = "ko-KR") -> None:
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
            df.to_csv(f"{os.getcwd()}/{relative_path}/{keyword}.csv")
        except:
            print(f"\033[31m\nmkdir {relative_path}\033[0m")
            os.mkdir(f"{relative_path}")
            df.to_csv(f"{os.getcwd()}/{relative_path}/{keyword}.csv")