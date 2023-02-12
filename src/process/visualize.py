import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def show_wordcount_summary(df):
    df['summary'].str.len().hist()


def show_wordcount_original(df):
    df['original'].str.len().hist()


def show_word_cloud(data):
    word_cloud = WordCloud(
        background_color='white',
        max_words=100,
        max_font_size=30,
        scale=3,
        random_state=1)

    word_cloud = word_cloud.generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')

    plt.imshow(word_cloud)
    plt.show()


if __name__ == "__main__":
    df = pd.DataFrame()
    show_word_cloud(df)
