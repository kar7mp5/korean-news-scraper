"""
# extract_article_content.py

Extract article's contents
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import certifi
import lxml
import os

from tqdm import tqdm




def extract_article_content(relative_path: str):
    """Get article contents from link

    :param relative_path: Get data from abs path
    """

    csv_files = os.listdir(f"{os.getcwd()}/{relative_path}")

    # read csv file
    for csv_file_name in csv_files:
        data = pd.read_csv(f"{os.getcwd()}/{relative_path}/{csv_file_name}")

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
        re = requests.get(url, verify=certifi.where())
        soup = BeautifulSoup(re.content, "lxml")
        element = soup.find("div")
        text_content = element.get_text()
        pd.DataFrame(text_content.split('.')).to_csv(f"{os.getcwd()}/{relative_path}/{file_name[:-4]}_{index}.csv", encoding="utf-8")

        # print(''.join([n for n in text_content if not n in ['\n', '/', '\\']]))

    except:
        pass