from os.path import dirname
from sys import path

path.insert(0, dirname(__file__))
from save_data_csv import save_data_csv
# from get_article_contents import get_article_contents