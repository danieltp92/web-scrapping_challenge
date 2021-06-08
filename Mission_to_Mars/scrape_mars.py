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
    featured_image_url = url + href

    list_news["src"] = featured_image_url


    browser.quit()


    # This section extract the facts of Mars

    url = "https://galaxyfacts-mars.com"

    tables = pd.read_html(url)
    tables
    mars_df = tables [0]
    new_head = mars_df.iloc[0]
    mars_df = mars_df[0:]
    mars_df.columns = new_head
    mars_df.rename(columns=mars_df.iloc[0])
    mars_df = mars_df.iloc[1: , :]
    mars_df = mars_df.reset_index(drop=True)

    html_table = mars_df.to_html()
    html_table.replace('\n', '')

    mars_df.to_html('table.html')


    # This section gets the images and descriptions of Mars hemispheres

    url = 'https://marshemispheres.com/'
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    elements = soup.find_all("div", class_="item")

    texts = soup.find_all("div", class_="description")


    i=0
    for text in texts:
        i = i+1
        j=str(i)
        list_news[j] = text.find('h3').get_text()
        
        
    for element in elements:
        i = i+1
        j=str(i)
        img = element.find('img')
        src = img['src']
        list_news[j] = url + src

    print(list_news)
        

    browser.quit()

    return list_news