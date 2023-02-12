from newspaper import Article
import nltk


def download_dependencies():
    nltk.download('punkt')


if __name__ == '__main__':
    download_dependencies()

    url = 'https://vtc.vn/nhat-ban-thua-dau-costa-rica-bang-tu-than-them-hap-dan-ar716735.html'
    article = Article(url)
    article.download()

    # print(article.html)
    article.parse()

    # print(article.__dir__())
    # print(article.top_image)

    # print(article.authors)
    # print(article.publish_date)
    # print(article.text)

    article.nlp()

    print(article.summary)
