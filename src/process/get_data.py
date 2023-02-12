import concurrent.futures
import glob
import zipfile
from pathlib import Path

import pandas as pd
import wget
from datasets import *
from vncorenlp import VnCoreNLP


def check_resource(file_path):
    return Path(file_path).is_file()


def download_resource():
    save_path_1 = "./master.zip"
    save_path_2 = "./master"
    if not check_resource(save_path_1):
        wget.download('https://github.com/ThanhChinhBK/vietnews/archive/master.zip', save_path_1)
    with zipfile.ZipFile(save_path_1, 'r') as zip_ref:
        zip_ref.extractall(save_path_2)

    # save_path_1 = "./ViMs.zip"
    # save_path_2 = "./ViMs"
    # if not check_resource(save_path_1):
    #     wget.download('https://github.com/CLC-HCMUS/ViMs-Dataset/raw/master/ViMs.zip', save_path_1)
    # with zipfile.ZipFile(save_path_1, 'r') as zip_ref:
    #     zip_ref.extractall(save_path_2)

    # Download VnCoreNLP-1.1.1.jar & its word segmentation component (i.e. RDRSegmenter)
    os.makedirs("./vncorenlp/models/wordsegmenter", exist_ok=True)
    if not check_resource("./vncorenlp/VnCoreNLP-1.1.1.jar"):
        wget.download("https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/VnCoreNLP-1.1.1.jar",
                  "./vncorenlp/VnCoreNLP-1.1.1.jar")
    if not check_resource("./vncorenlp/models/wordsegmenter/vi-vocab"):
        wget.download("https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/wordsegmenter/vi-vocab",
                  "./vncorenlp/models/wordsegmenter/vi-vocab")
    if not check_resource("./vncorenlp/models/wordsegmenter/wordsegmenter.rdr"):
        wget.download("https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/wordsegmenter/wordsegmenter.rdr",
                  "./vncorenlp/models/wordsegmenter/wordsegmenter.rdr")


def list_paths(path):
    file_paths = list()
    for file_path in glob.glob(path):
        file_paths.append(file_path)
    return file_paths


def read_content(file_path):
    """
  Input: Path of txt file
  Output: A dictionary has keys 'original' and 'summary'
  """
    with open(file_path) as f:
        rows = f.readlines()
        original = ' '.join(''.join(rows[4:]).split('\n'))
        summary = ' '.join(rows[2].split('\n'))

    return {'file': file_path,
            'original': original,
            'summary': summary}


def get_dataframe(file_paths):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        data = executor.map(read_content, file_paths)

    # Make blank dataframe
    data_df = list()
    for d in data:
        data_df.append(d)
    data_df = pd.DataFrame(data_df)
    data_df.dropna(inplace=True)
    data_df = data_df.sample(frac=1).reset_index(drop=True)

    return data_df


def train_model():
    train_paths = list_paths('/master/vietnews-master/data/train_tokenized/*')
    train_df = get_dataframe(train_paths)

    print(train_df.head())
    print(train_df.info())
    
    read_content(train_paths[0])


def validate_model():
    val_paths = list_paths('/master/vietnews-master/data/val_tokenized/*')
    val_df = get_dataframe(val_paths)

    print(val_df.head())
    print(val_df.info())


def test_model():
    test_paths = list_paths('/master/vietnews-master/data/test_tokenized/*')
    test_df = get_dataframe(test_paths)

    print(test_df.head())
    print(test_df.info())


if __name__ == "__main__":
    download_resource()
    rdrsegmenter = VnCoreNLP("./vncorenlp/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx2g')

