import korean_news_scraper

keywords = ["미국", "대통령", "대선"]
korean_news_scraper.save_data_csv(keywords, "data", False)
korean_news_scraper.get_article_contents("data")

