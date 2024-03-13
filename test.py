import korean_news_scraper

keywords = ["america", "biden", "trump"]
korean_news_scraper.save_data_csv(keywords, "data", lang="en-EN")
korean_news_scraper.extract_article_content("data")

# from tqdm import tqdm
# import time

# with tqdm(total=100) as pbar:
#     for i in range(10):
#         time.sleep(0.1)
#         pbar.update(10)