from bs4 import BeautifulSoup
import pandas as pd
import os

from getArticleLinks import getArticleLinks

def googleNewsScraper(keywords: list = None):

    keyword = "문재인"
    data = getArticleLinks("ko-KR", keyword) 

    df = pd.DataFrame(data)
    print(df)

    df.columns = ["News Links"]
    # df.to_csv(f"{os.getcwd()}/data/collected_data/{keyword}.csv")

    return data