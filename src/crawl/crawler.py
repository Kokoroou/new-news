import csv
import os
from pathlib import Path
import sys

import pandas as pd
import requests
import tqdm
from bs4 import BeautifulSoup


def get_links(topic_link=None, title_tag='h2'):
    """Get news URLs from topic link"""
    try:
        response = requests.get(topic_link)
        soup = BeautifulSoup(response.content, "html.parser")
        titles = soup.find_all(title_tag, class_='title-news')
        links = [link.find('a').attrs["href"] for link in titles]

        return links
    except Exception as e:
        print('Exception {} has happened when get links from URL: {}'.format(type(e).__name__, topic_link))


def find_topic(soup=None):
    # A part of HTML which store topic of news
    t = soup.find('ul', class_='breadcrumb')  

    # Topic of news (VD: KhoaHoc)
    topic = (t.find('a').attrs["data-medium"])[5:]
    
    return topic


def find_date(soup=None):
    t = soup.find(class_='header-content')  
    
    date = t.find(class_="date").get_text().split(", ")[1]

    return date


def find_header(soup=None):
    header = soup.find(class_='title-detail').get_text()
    return header


def find_tag(link):
   response = requests.get(link)
   soup = BeautifulSoup(response.content, "html.parser")
   header = soup.find(class_='title-detail').get_text()
   return header


def crawl_data(link=None, data_dir=Path('./data')):
    """Get data from URL and save to file"""
    try:
        if not Path(data_dir).is_dir():
            os.mkdir(data_dir)

        # Get HTML source code from link
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        topic = find_topic(soup)

        # Create new directory if this topic is not crawled
        topic_dir = data_dir / topic
        if not topic_dir.is_dir():
            os.mkdir(topic_dir)

        # Index file which stores URL of all crawled news in the same topic
        index_filename = '_Index.csv'.format(topic)  
        index_filepath = topic_dir / index_filename

        date = find_date(soup)
        #header = find_header(soup)

        # Text file which stores content of the news in link
        if not index_filepath.is_file():
            # If Index file is not exist
            index = 1
        else:
            df = pd.read_csv(index_filepath, header=None, index_col=None)
            index = int(df.iloc[-1, 0]) + 1

            # Stop if this link is crawled
            for crawled_link in df.iloc[:, 2]:
                if link == crawled_link:
                  return None

        text_filename = 'news{}.txt'.format(index)
        text_path = topic_dir / text_filename

        # Add new URL to Index file of the topic
        with open(index_filepath, mode='a+') as file:
            writer = csv.writer(file)
            writer.writerow([index, text_filename, str(link), date])

        # Write content to file
        with open(text_path, 'w', encoding='UTF-8') as f:
          # Write title of news
          f.write(soup.find('h1', class_='title-detail').text + '\n\n')

          # Write description of news
          f.write(soup.find('p', class_='description').text)

          # Write all content of news
          contents = soup.findAll('p', class_='Normal')
          for i in range(0, len(contents) - 1):
              f.write('\n' + contents[i].text)

    except Exception as e:
        print('Exception {} has happened when crawl data from URL: {}'.format(type(e).__name__, link))

