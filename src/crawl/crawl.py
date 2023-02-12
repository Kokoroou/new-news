import os
import sys
from pathlib import Path

import newspaper
import yaml
from tqdm import tqdm
from yaml.loader import SafeLoader

from .crawler import get_links, crawl_data

MAIN_DIR = Path(__file__).parent.parent.parent.resolve()  # Main directory


def crawl_1(max_page: int = 10):
    save_dir = MAIN_DIR / 'data' / 'data_1'
    min_page = 0

    os.makedirs(save_dir, exist_ok=True)

    links2 = [
        'https://vnexpress.net/suc-khoe',
        'https://vnexpress.net/du-lich',
        'https://vnexpress.net/so-hoa',
        'https://vnexpress.net/kinh-doanh',
        'https://vnexpress.net/giai-tri',
        'https://vnexpress.net/the-thao'
    ]

    links3 = [
        'https://vnexpress.net/thoi-su',
        'https://vnexpress.net/goc-nhin',
        'https://vnexpress.net/the-gioi',
        'https://vnexpress.net/khoa-hoc',
        'https://vnexpress.net/phap-luat',
        'https://vnexpress.net/giao-duc',
        'https://vnexpress.net/oto-xe-may',
        'https://vnexpress.net/hai',
    ]

    try:  
        for link in links2:
            news_name = link.split('//')[1].split('.')[0]
            news_save_dir = save_dir / news_name

            os.makedirs(news_save_dir, exist_ok=True)

            news_links = []

            for i in tqdm(list(range(min_page, max_page + 1)), desc=link):
                sub_link = link + '-p' + str(i)  # Topic link with page number
                news_links += get_links(sub_link, 'h2')

            for sub_link in tqdm(news_links, desc='Crawling'):
                crawl_data(sub_link, news_save_dir)

        for link in links3:
            news_name = link.split('//')[1].split('.')[0]
            news_save_dir = save_dir / news_name

            os.makedirs(news_save_dir, exist_ok=True)

            news_links = []

            for i in tqdm(list(range(min_page, max_page + 1)), desc=link):
                sub_link = link + '-p' + str(i)  # Topic link with page number
                news_links += get_links(sub_link, 'h3')

            for sub_link in tqdm(news_links, desc='Crawling'):
                crawl_data(sub_link, news_save_dir)
    except Exception as e:
        print(sys.exc_info()[2])


def crawl_2(max_article: int = 100):
    save_dir = MAIN_DIR / 'data' / 'data_2'

    with open(MAIN_DIR / 'src' / 'crawl' / 'newspaper_link.yaml', 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))
        vietnamese_link = data[0]['Vietnamese']

    print(vietnamese_link)

    for link in vietnamese_link:
        news_name = link.split('//')[1].split('.')[0]
        news_save_dir = save_dir / news_name

        news_paper = newspaper.build(link)

        os.makedirs(news_save_dir, exist_ok=True)

        article_count = 0

        for article in tqdm(list(news_paper.articles), desc='Crawling...'):
            article_count += 1
            if article_count > max_article:
                break

            # print(article.text)

            url = article.url
            # article = newspaper.Article(url)

            article.download()
            article.parse()

            print(article.url)

    # url = 'https://vnexpress.net/kich-ban-nao-cho-duc-o-vong-cuoi-world-cup-2022-4541291.html'
    #
    # article = newspaper.Article(url)
    # article.download()
    # article.parse()
    #
    # print(article.publish_date)



