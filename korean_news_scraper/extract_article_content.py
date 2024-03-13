"""
# extract_article_content.py

"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import certifi
import lxml

from tqdm import tqdm

import os


def extract_article_content(relative_path: str):
    """Get article contents from link

    :param relative_path: Get data from abs path
    """

    csv_files = os.listdir(f"{os.getcwd()}/{relative_path}")

    # read csv file
    for csv_file_name in csv_files:
        data = pd.read_csv(f"{os.getcwd()}/{relative_path}/{csv_file_name}")

        for row in tqdm(data["News Links"], desc="Get article's text", ncols=100):
            get_article_text(row)



def get_article_text(url: str):
    """Get article text from link

    :param url: Get text from article's link
    """

    # exeption handling for website blocking
    try:
        re = requests.get(url, verify=certifi.where())
        soup = BeautifulSoup(re.content, "lxml")
        element = soup.find("div")
        text_content = element.get_text()

        # print(''.join([n for n in text_content if not n in ['\n', '/', '\\']]))

    except:
        pass