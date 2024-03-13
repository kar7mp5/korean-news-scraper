# Korean News Scraper

Hello World!  Korean News Scraper aims to be a Korean language data collection tool for LLM.

After version 0.1.1. is possible to use. Please do not use it before.


## Build

```bash
$ run setup.py
```


## Required Libraries

- beautifulsoup4
- selenium
- pandas
- requests


## Quick Start

```python
import korean_news_scraper

keywords = ["미국", "대통령", "대선"]
korean_news_scraper.save_data_csv(keywords, "data", False)
korean_news_scraper.get_article_contents("data")
```