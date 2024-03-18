# Korean News Scraper

Hello World!  Korean News Scraper aims to be a Korean language data collection tool for LLM.

After version 0.1.1. is possible to use. Please do not use it before.


## Build

```bash
$ python3 setup.py
```


## Required Libraries

- beautifulsoup4
- selenium
- pandas
- requests
- tqdm

## Quick Start

```python
import korean_news_scraper

keywords = ["news", "happy", "environment"]
korean_news_scraper.save_article_links(keywords, "data", lang="en-EN")
korean_news_scraper.extract_article_content("data")
```