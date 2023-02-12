import os
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()

def run_crawler():
    pass


def run_processor():
    pass


def run_demo():
    # homepage_path = str(CURRENT_DIR / "app.py")
    homepage_path = "web_demo/app.py"
    os.system("streamlit run {}".format(homepage_path))


if __name__ == "__main__":
    run_crawler()
    # run_processor()
    # run_demo()
