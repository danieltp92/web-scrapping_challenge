from http.client import HTTP_PORT
from tarfile import HeaderError
from splinter import Browser, browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path' : ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    list_news = {}

    list_news["title"] = soup.find("div", class_="content_title").get_text()
    list_news["text"] = soup.find("div", class_="article_teaser_body").get_text()

    browser.quit()

    return list_news