"""
# google-news-scraper.py

Links from Google News articles for specific keywords are scraped and saved to CSV.
"""

import pandas as pd
import os

from get_article_links import get_article_links


def save_data_csv(keywords: list, abs_path: str = "", show_data: bool = True, lang: str = "ko-KR") -> None:
    """Get article's links

    :param keywords: Keywords; data type is list[str]
    :param abs_path: Data save abs path
    :param show_data: Select to show the data
    :param lang: Select website language. You can use ['ko-KR', 'en-EN']
    """

    for keyword in keywords:
        data = get_article_links(lang, keyword)

        df = pd.DataFrame(data)
        
        # show data on terminal
        if show_data == True:
            print(df)


        print(f"\nScrapping {len(df)} data\nmk {keyword}.csv")

        # save the data as .csv 
        df.columns = ["News Links"]
        try:
            df.to_csv(f"{os.getcwd()}/{abs_path}/{keyword}.csv")
        except:
            print(f"\nmkdir {abs_path}")
            os.mkdir(f"{abs_path}")
            df.to_csv(f"{os.getcwd()}/{abs_path}/{keyword}.csv")