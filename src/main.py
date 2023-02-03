import os
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()


def run_streamlit() -> None:
    # homepage_path = str(CURRENT_DIR / "app.py")
    homepage_path = "app.py"
    os.system("streamlit run {}".format(homepage_path))


if __name__ == "__main__":
    run_streamlit()
