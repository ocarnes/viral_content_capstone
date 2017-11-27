#turn raw data into features for modeling
import pandas as pd
import numpy as np
import pprint
from bs4 import BeautifulSoup
import requests
import os
import time
# month set on line 102 and 104

def soups(urls, titles, cats, index, url):
    time.sleep(1)
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')

    new = str(soup.findAll('div', "timeline--article--content--title entry-title")).strip('</a>\n</div>]').strip('[<div class="timeline--article--content--title entry-title"').split('</a>\n</div>, <div class="timeline--article--content--title entry-title"')

    new = ''.join(new).split('>')

    new2 =''.join(new[1:len(new):2]).split('\n<a href="')

    for line in new2[1:len(new2)]:
        splits = line.strip('"').split(" title=")
        urls.append(splits[0])
        titles.append(splits[1])
        cats.append(category[index])
        url = str(soup.find('nav', 'page-navigation').findAll('a')).split('href=')[-1].strip('>next page</a>]').strip('"')
    return urls, titles, cats, url

if __name__ == '__main__':
    category = ['Entertainment',
     'Celebrity News',
     'TV',
     'Famous Relationships',
     'Movie Trailers',
     'Movies',
     'Music',
     'Online Videos',
     'Rumors',
     'Lifestyle',
     'Shopping',
     'Travel',
     'Fashion',
     'Food & Dining',
     'Geek Culture',
     'Parenting',
     'Religion',
     'Health',
     'Health Studies',
     'Medicine',
     'Nutrition',
     'News',
     'Politics',
     'Animal News',
     'Education',
     'Green News',
     'Media Industry',
     'Odd News',
     'World',
     'South America',
     'Africa',
     'Asia',
     'Australia News',
     'Canada',
     'Europe',
     'Middle East',
     'Odd News',
     'Pics',
     'Opinion',
     'Sports',
     'Baseball',
     'Basketball',
     'Boxing',
     'Football',
     'Golf',
     'Hockey',
     'MMA',
     'NASCAR',
     'Soccer',
     'Tennis',
     'Science',
     'Discoveries',
     'Space',
     'Theories',
     'Technology',
     'Automotive',
     'Green Tech',
     'Gadgets',
     'Mobile',
     'Gaming',
     'Business',
     'Social Media',
     'Start-up',
     'Buzzworthy']

    url = #site url
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')

    arr = str(soup.find('ul', "block--in footer--categories--in").findAll('a')).split('"')[1:129:2]

    arr[-1]=arr[-1]+'archives/2017/07/page/1/'

    arr = 'archives/2017/07/page/1/?'.join(arr)
    arr = arr.split('?')
    titles = []
    urls = []
    cats = []
    url_new = arr[0]
    for index, url in enumerate(arr):
        url_new = url
        while abs(len(url_new)-len(url))<=2:
            url = url_new
            urls, titles, cats, url_new = soups(urls, titles, cats, index, url)
            if url == url_new:
                break
            print(url)
    df = pd.DataFrame(data=np.array([titles, urls, cats]).T, columns=['post_title', 'tinyUrl', 'postCategories_name'])
    df.to_pickle('../../data/july_articles.pkl')
