"""
# extract_article_content.py

Extract article's contents
"""
# Library for scrapping articles' content
from bs4 import BeautifulSoup
import requests
import certifi

import pandas as pd
import time
import lxml
import os

# Library for loading bar
from tqdm import tqdm




def extract_article_content(relative_path: str):
    """Get article contents from link

    :param relative_path: Get data from abs path
    """

    csv_files = os.listdir(f"{os.getcwd()}/{relative_path}/article_links")

    # read csv file
    for csv_file_name in csv_files:
        data = pd.read_csv(f"{os.getcwd()}/{relative_path}/article_links/{csv_file_name}")

        for index, row in enumerate(tqdm(data["News Links"], desc="Get article's text", ncols=100)):
            save_article_content(row, relative_path, csv_file_name, index)




def save_article_content(url: str, relative_path: str, file_name: str, index: int):
    """Get article text from link

    :param url: Get text from article's link
    :param relative_path: Relative Path
    :param file_name: File Name
    :param index: Index Number
    """

    # exeption handling for website blocking
    try:
        re = requests.get(url, verify=certifi.where(), timeout=2)
        soup = BeautifulSoup(re.content, "lxml")
        element = soup.find("div")
        text_content = element.get_text()

        # ignore unnecessary words
        if len(text_content) <= 2000:
            return

        text_content = ''.join([n for n in text_content if not n in ['\n', '/', '\\', '(', ')', '[', ']', '"', "'"]]).split('.')
        

        for idx, val in enumerate(text_content):
            if len(val.strip()) <= 100:
                del text_content[idx]


        try:
            pd.DataFrame(text_content).to_csv(f"{os.getcwd()}/{relative_path}/article_contents/{file_name[:-4]}_{index}.csv", encoding="utf-8")
        except:
            print(f"\033[31m\nmkdir {relative_path}/article_contents/\033[0m")
            os.mkdir(f"{relative_path}/article_contents")
            pd.DataFrame(text_content).to_csv(f"{os.getcwd()}/{relative_path}/article_contents/{file_name[:-4]}_{index}.csv", encoding="utf-8")

    except:
        pass