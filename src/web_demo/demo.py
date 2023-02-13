from pathlib import Path

import pandas as pd
import streamlit as st
from newspaper import Article
from utils import get_user_favorite, get_user_read, get_user_unread, read_article, unread_article


MAIN_PATH = Path(__file__).parent.parent.parent.resolve()


def write():
    st.title("Newest")

    data_dir = MAIN_PATH / 'data' / 'data_1' / 'vnexpress'
    summarize_dir = MAIN_PATH / 'data' / 'summarized_1' / 'vnexpress'

    username = 'ADH'
    news_items = []

    # Create list of news item
    favorite_topics = get_user_favorite(username)
    unread_dict = get_user_unread(username)

    for topic in favorite_topics:
        index_filepath = data_dir / topic / '_Index.csv'
        df = pd.read_csv(index_filepath, header=None)

        for filename in unread_dict[topic]:
            row = df[df[1] == filename]
            url = row.iloc[0, 2]

            with open(Path(summarize_dir, topic, filename), 'r', encoding='utf-8') as f:
                summary = "".join(f.readlines())

            article = Article(url)
            article.download()
            article.parse()

            news_item = {"url": url, "summary": summary, "image_url": article.top_image,
                         "topic": topic, "filename": filename}

            news_items.append(news_item)

    # Loop through the news items and display them in a row
    if news_items:
        for i in range(min(len(news_items), 10)):
            item = news_items[::-1][i]

            st.image(item["image_url"], width=500)
            st.write(item["summary"])
            st.write("Read more:", item["url"])
            st.button("Đã đọc", key=str(i), on_click=read_article,
                      args=(username, item["topic"], item["filename"]))
            st.write("---")
    else:
        st.write("Bạn đã đọc hết các bài viết mới")


# def recommend():
#     st.title("Recommend for you")
#     st.write("This is the second page, displaying recommendations based on your preferences.")
#
#
# def favorite():
#     st.title("Favorite")
#     st.write("This is the third page, displaying your favorite newspaper.")


def already_read():
    st.title("Already Read")

    data_dir = MAIN_PATH / 'data' / 'data_1' / 'vnexpress'
    summarize_dir = MAIN_PATH / 'data' / 'summarized_1' / 'vnexpress'

    username = 'ADH'
    news_items = []

    # Create list of news item
    favorite_topics = get_user_favorite(username)
    read_dict = get_user_read(username)

    for topic in favorite_topics:
        index_filepath = data_dir / topic / '_Index.csv'
        df = pd.read_csv(index_filepath, header=None)

        for filename in read_dict[topic]:
            row = df[df[1] == filename]
            url = row.iloc[0, 2]

            with open(Path(summarize_dir, topic, filename), 'r', encoding='utf-8') as f:
                summary = "".join(f.readlines())

            article = Article(url)
            article.download()
            article.parse()

            news_item = {"url": url, "summary": summary, "image_url": article.top_image,
                         "topic": topic, "filename": filename}

            news_items.append(news_item)

    # Loop through the news items and display them in a row
    if news_items:
        for i in range(min(len(news_items), 10)):
            item = news_items[::-1][i]

            st.image(item["image_url"], width=500)
            st.write(item["summary"])
            st.write("Read more:", item["url"])
            st.button("Chưa đọc", key=str(i+20), on_click=unread_article,
                      args=(username, item["topic"], item["filename"]))
            st.write("---")
    else:
        st.write("Bạn chưa đọc bài viết nào")


def main():
    st.sidebar.title("Navigation")
    # selection = st.sidebar.radio("Go to", ("Newest", "Recommend for you", "Favorite", "Already Read"))
    selection = st.sidebar.radio("Go to", ("Newest", "Already Read"))

    if selection == "Newest":
        write()
    # elif selection == "Recommend for you":
    #     recommend()
    # elif selection == "Favorite":
    #     favorite()
    elif selection == "Already Read":
        already_read()


if __name__ == "__main__":
    main()
