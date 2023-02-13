import os
from pathlib import Path

from tqdm import tqdm

from .processor import Processor

MAIN_DIR = Path(__file__).parent.parent.parent.resolve()  # Main directory


def process_1():
    processor = Processor()

    read_path_1 = MAIN_DIR / 'data' / 'data_1'
    save_path_1 = MAIN_DIR / 'data' / 'summarized_1'

    os.makedirs(read_path_1, exist_ok=True)
    os.makedirs(save_path_1, exist_ok=True)

    for web_path in read_path_1.glob("*/"):
        web_name = web_path.name

        for topic_path in Path(read_path_1, web_name).glob("*/"):
            topic_name = topic_path.name

            sub_save_path = save_path_1 / web_name / topic_name
            os.makedirs(sub_save_path, exist_ok=True)

            for file_path in tqdm(list(Path(read_path_1, web_name, topic_name).glob("*.txt")),
                                  desc="{}/{}".format(web_name, topic_name)):
                file_name = file_path.name

                with open(file_path, 'r', encoding='utf-8') as file:
                    content_lines = file.readlines()
                    content = "".join(content_lines)

                    summarized_text = processor.summarize(content)

                with open(Path(sub_save_path, file_name), 'w', encoding='utf-8') as file:
                    file.write(summarized_text)


