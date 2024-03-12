from setuptools import setup, find_packages

setup(
    name='korean-news-scraper',
    version='0.0.1',
    url='https://github.com/kimminsum/korean-news-scraper.git',
    author='kar7mp5',
    author_email='tommy1005a@gmail.com',
    description='A python package to scrape news.',
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4', 'selenium', 'pandas'],
)