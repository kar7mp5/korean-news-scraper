from setuptools import setup, find_packages

setup(
    name='news-scraper',
    version='0.0.1',
    url='https://github.com/morganbarber/python-news-scraper',
    author='kar7mp5',
    author_email='tommy1005a@gmail.com',
    description='A python package to scrape news.',
    packages=find_packages(),    
    install_requires=['requests', 'beautifulsoup4', 'urllib', 'selenium'],
)