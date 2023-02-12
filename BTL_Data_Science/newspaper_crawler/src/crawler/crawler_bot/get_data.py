import yaml
from newspaper import Article


def get_data():
    pass


if __name__ == '__main__':
    link_filepath = r'D:\OneDrive - Hanoi University of Science and Technology\Tuan Anh\Workspace\University Project\newspaper_crawler\src\crawler\crawler_bot\demo_link.txt'

    with open(link_filepath, 'r') as file:
        content = file.read()
        links = content.split('\n')

    save_path = r'D:\OneDrive - Hanoi University of Science and Technology\Tuan Anh\Workspace\University Project\newspaper_crawler\data\vietnamese'

    for link in links:
        article = Article(link)
        article.download()
        article.parse()

        print(article.title)
