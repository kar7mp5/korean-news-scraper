from selenium import webdriver


def scrollDownPage(url: str) -> None:

    print("Scroll down the page")

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        driver = webdriver.Chrome(options=options)
        driver.get(url)
    except:
        raise ValueError("Invaild URL")


    #This code will scroll down to the ends
    while True:
        try:
            # Action scroll down
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            break
        except:
            pass
    
    driver.quit()