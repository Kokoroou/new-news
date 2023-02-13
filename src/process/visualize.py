from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

MAIN_DIR = Path(__file__).parent.parent.parent.resolve()  # Main directory


def show_wordcount_summary(df):
    df['summary'].str.len().hist()
    plt.show()


def show_wordcount_original(df):
    df['original'].str.len().hist()
    plt.show()


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


def visualize(site, topic):
    df = pd.DataFrame(columns=["file", "original", "summary"])

    file_dir = MAIN_DIR / 'data' / 'data_1' / site / topic
    summary_dir = MAIN_DIR / 'data' / 'summarized_1' / site / topic

    for filepath in file_dir.glob("*.txt"):
        filename = filepath.name
        summary_filepath = summary_dir / filename

        with open(filepath, 'r', encoding="utf-8") as f:
            original = "".join(f.readlines())

        with open(summary_filepath, 'r', encoding="utf-8") as f:
            summary = "".join(f.readlines())

        new_df = pd.DataFrame({"file": str(filepath), "original": original, "summary": summary}, index=[0])

        df = pd.concat([df, new_df])

    show_wordcount_original(df)
    show_wordcount_summary(df)
    show_word_cloud(df["original"])
    show_word_cloud(df["summary"])


if __name__ == "__main__":
    visualize('vnexpress', 'SucKhoe')
