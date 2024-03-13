"""
# get_article_contents.py

"""

from bs4 import BeautifulSoup
import requests
import lxml
import certifi

import os, csv


def get_article_contents(abs_path: str):
    """Get article contents from link

    :param abs_path: Get data from abs path
    """

    csv_files = os.listdir(f"{os.getcwd()}/{abs_path}")

    for csv_file_name in csv_files:
        with open(f"{os.getcwd()}/{abs_path}/{csv_file_name}", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row["News Links"])
                tmp = row["News Links"]
                get_article_text(tmp)




def get_article_text(url: str):
    """Get article text from link

    :param abs_path: Get text from article's link
    """

    # exeption handling for website blocking
    try:
        re = requests.get(url, verify=certifi.where())
        soup = BeautifulSoup(re.content, "lxml")
        element = soup.find("div")
        text_content = element.get_text()

        print(''.join([n for n in text_content if not n in ['\n', '/', '\\']]))

    except:
        pass


if __name__=="__main__":
    get_article_contents("data")