"""
# scroll_down_page.py

Beautifulsoup has the disadvantage of not being able to load all pages, 
so I used Selenium to scroll to the end of the page.
"""
# Library for 
from selenium import webdriver




def scroll_down_page(url: str) -> None:
    """Scroll to the end of the page

    :param url: Website url
    """

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        driver = webdriver.Chrome(options=options)
        driver.get(url)
    except:
        raise ValueError("\033[31mInvaild URL\033[0m")


    #This code will scroll down to the ends
    while True:
        try:
            # Action scroll down
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            break
        except:
            pass
    
    driver.quit()