import json
from pathlib import Path

import pandas as pd

CURRENT_DIR = Path(__file__).parent.resolve()


def get_list_news(topic_path):
    topic_path = Path(topic_path)

    index_filepath = topic_path / '_Index.csv'
    if not index_filepath.is_file():
        return None

    df = pd.read_csv(index_filepath, header=None)

    return df.iloc[:, 0]


def get_user(username: str = ""):
    user_filepath = CURRENT_DIR / 'user.json'

    with open(user_filepath, 'r') as f:
        data = json.load(f)

    user_data = None
    for i in range(len(data["user"])):
        if data["user"][i]["username"] == username:
            user_data = data["user"][i]
            break

    return user_data


def set_user(username: str = "", new_user_data: dict = None):
    user_filepath = CURRENT_DIR / 'user.json'

    with open(user_filepath, 'r') as f:
        data = json.load(f)

        for i in range(len(data["user"])):
            if data["user"][i]["username"] == username:
                data["user"][i] = new_user_data
                break

    with open(user_filepath, 'w') as f:
        json.dump(data, f, indent=2)


def get_user_read(username: str = ""):
    user_data = get_user(username)

    return user_data["read"]


def add_user_read(username: str = "", topic: str = "", news_filename: str = ""):
    user_data = get_user(username)

    if topic not in user_data["read"].keys():
        user_data["read"][topic] = []

    if news_filename not in user_data["read"][topic]:
        user_data["read"][topic].append(news_filename)

    set_user(username, user_data)


def del_user_read(username: str = "", topic: str = "", news_filename: str = ""):
    user_data = get_user(username)

    if topic not in user_data["read"].keys():
        return

    if news_filename in user_data["read"][topic]:
        user_data["read"][topic].remove(news_filename)

    set_user(username, user_data)


def get_user_unread(username: str = ""):
    user_data = get_user(username)

    return user_data["unread"]


def add_user_unread(username: str = "", topic: str = "", news_filename: str = ""):
    user_data = get_user(username)

    if topic not in user_data["unread"].keys():
        user_data["unread"][topic] = []

    if news_filename not in user_data["unread"][topic]:
        user_data["unread"][topic].append(news_filename)

    set_user(username, user_data)


def del_user_unread(username: str = "", topic: str = "", news_filename: str = ""):
    user_data = get_user(username)

    if topic not in user_data["unread"].keys():
        return

    if news_filename in user_data["unread"][topic]:
        user_data["unread"][topic].remove(news_filename)

    set_user(username, user_data)


def get_user_favorite(username: str = ""):
    user_data = get_user(username)

    return user_data["favorite"]


def add_user_favorite(username: str = "", topic: str = ""):
    user_data = get_user(username)

    if topic not in user_data["favorite"]:
        user_data["favorite"].append(topic)

    set_user(username, user_data)


def del_user_favorite(username: str = "", topic: str = ""):
    user_data = get_user(username)

    if topic in user_data["favorite"]:
        user_data["favorite"].remove(topic)

    set_user(username, user_data)


def read_article(username: str = "", topic: str = "", news_filename: str = ""):
    add_user_read(username, topic, news_filename)
    del_user_unread(username, topic, news_filename)


def unread_article(username: str = "", topic: str = "", news_filename: str = ""):
    add_user_unread(username, topic, news_filename)
    del_user_read(username, topic, news_filename)

