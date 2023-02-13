import os
from pathlib import Path

from crawl.crawl import crawl_1, crawl_2
from process.process import process_1
from process.visualize import visualize

CURRENT_DIR = Path(__file__).parent.resolve()


def run_crawler():
    crawl_1(max_page=2)
    # crawl_2(max_article=30)


def run_processor():
    process_1()
    # visualize('vnexpress', 'SucKhoe')


def run_demo():
    # homepage_path = str(MAIN_DIR / "app.py")
    homepage_path = "web_demo/demo.py"
    os.system("streamlit run {}".format(homepage_path))


if __name__ == "__main__":
    run_crawler()
    run_processor()
    run_demo()
