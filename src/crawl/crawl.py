import os
import sys
from pathlib import Path

import newspaper
import yaml
from tqdm import tqdm
from yaml.loader import SafeLoader

from .crawler import get_links, crawl_data


def crawl_1(max_page: int = 10):
    CURRENT_DIR = Path(__file__).parent.parent.parent.resolve()  # Main directory
    DATA_DIR = CURRENT_DIR / 'data' / 'data_1'
    MIN_PAGE = 1

    if not DATA_DIR.is_dir():
        os.makedirs(DATA_DIR)

    links2 = [
        'https://vnexpress.net/suc-khoe',
        # 'https://vnexpress.net/du-lich',
        # 'https://vnexpress.net/so-hoa',
        # 'https://vnexpress.net/kinh-doanh',
        # 'https://vnexpress.net/giai-tri',
        # 'https://vnexpress.net/the-thao'
    ]

    links3 = [
        # 'https://vnexpress.net/thoi-su',
        # 'https://vnexpress.net/goc-nhin',
        # 'https://vnexpress.net/the-gioi',
        # 'https://vnexpress.net/khoa-hoc',
        # 'https://vnexpress.net/phap-luat',
        # 'https://vnexpress.net/giao-duc',
        # 'https://vnexpress.net/oto-xe-may',
        # 'https://vnexpress.net/hai',
    ]

    try:  
        for link in links2:
            news_links = []

            for i in tqdm(list(range(MIN_PAGE, max_page + 1)), desc=link):
                sub_link = link + '-p' + str(i)  # Topic link with page number
                news_links += get_links(sub_link, 'h2')

            for sub_link in tqdm(news_links, desc='Crawling'):
                crawl_data(sub_link, DATA_DIR)

        for link in links3:
            news_links = []

            for i in tqdm(list(range(MIN_PAGE, max_page + 1)), desc=link):
                sub_link = link + '-p' + str(i)  # Topic link with page number
                news_links += get_links(sub_link, 'h3')

            for sub_link in tqdm(news_links, desc='Crawling'):
                crawl_data(sub_link, DATA_DIR)
    except Exception as e:
        print(sys.exc_info()[2])


def crawl_2():
    with open('newspaper_link.yaml', 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))
        vietnamese_link = data[0]['Vietnamese']

    print(vietnamese_link)


    url = 'https://vnexpress.net/kich-ban-nao-cho-duc-o-vong-cuoi-world-cup-2022-4541291.html'

    article = newspaper.Article(url)
    article.download()
    article.parse()

    print(article.publish_date)


    CURRENT_DIR = Path(os.getcwd())
    DATA_DIR = CURRENT_DIR / 'data'
    MAX_ARTICLE_COUNT = 100

    for link in vietnamese_link:
        news_name = link.split('//')[1].split('.')[0]

    news_paper = newspaper.build(link)
    if not Path(DATA_DIR / news_name).is_dir():
        os.mkdir(str(DATA_DIR / news_name))

    article_count = 0

    for article in news_paper.articles:
        article_count += 1
        if article_count > MAX_ARTICLE_COUNT:
            break

        # print(article.text)
        
        url = article.url
        article = newspaper.Article(url)

        article.download()
        article.parse()

        print(article.url)

