from os.path import dirname
from sys import path

path.insert(0, dirname(__file__))

from save_data_csv import save_data_csv
from extract_article_content import extract_article_content