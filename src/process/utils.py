from pathlib import Path

import pandas as pd


def read_file(file_path):
    file_path = Path(file_path)

    folder_name = file_path.parent.resolve().name

    print(file_path)

    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        title = lines[0].strip()
        content = ''.join(line.strip() for line in lines[1:])
        return pd.DataFrame({'label': [folder_name], 'title': [title], 'content': [content]})


if __name__ == "__main__":
    df = read_file("D:/OneDrive - Hanoi University of Science and Technology/Tuan Anh/Workspace/University "
                   "Project/new-news/data/data_1/vnexpress/SucKhoe/news1.txt")
    # print(df)
    

