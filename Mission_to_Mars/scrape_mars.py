from bs4 import BeautifulSoup as bs
import requests
import os
import pymongo
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import shutil
from IPython.display import Image

def scrape():

    # This section extracts the latest news of Mars

    executable_path = {'executable_path' : ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    list_news = {}

    list_news["title"] = soup.find("div", class_="content_title").get_text()
    list_news["text"] = soup.find("div", class_="article_teaser_body").get_text()

    browser.quit()

    # This section gets the Featured image from Mars

    executable_path = {'executable_path' : ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    feat_img = soup.find("div", class_="header")
    elem = feat_img.find("a", class_="showimg fancybox-thumbs")
    href = elem['href']
    featured_image_url = url + "/" + href

    response = requests.get(featured_image_url, stream=True)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    Image(url='img.png')


    browser.quit()

    return list_news

