"""
# get_article_contents.py

"""

import csv


def get_article_contents():
    """Get article contents from link

    """
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["News Links"])


if __name__=="__main__":
    get_article_contents()