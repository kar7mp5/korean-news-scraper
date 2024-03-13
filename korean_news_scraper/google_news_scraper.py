"""
# google-news-scraper.py

Links from Google News articles for specific keywords are scraped and saved to CSV.
"""

import pandas as pd
import os

from getArticleLinks import getArticleLinks


def googleNewsScraper(keywords: list, lang: str = "ko-KR", abs_path: str = "", show_data: bool = True) -> None:
    for keyword in keywords:
        data = getArticleLinks(lang, keyword) 

        df = pd.DataFrame(data)
        
        # show data on terminal
        if show_data == True:
            print(df)


        print(f"mk {keyword}.csv")
        df.columns = ["News Links"]

        # save the data as .csv 
        try:
            df.to_csv(f"{os.getcwd()}/{abs_path}/{keyword}.csv")
        except:
            print(f"mkdir {abs_path}")
            os.mkdir(f"{abs_path}")
            df.to_csv(f"{os.getcwd()}/{abs_path}/{keyword}.csv")