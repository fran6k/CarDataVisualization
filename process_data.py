import numpy as np
import pandas as pd
from pandas import DataFrame

dataset_path = "./dataset/SportsCars.csv"


def split_in_brand(df: DataFrame, output):
    # 1 按照不同品牌切割数据集
    grouped = df.groupby('brand')
    for name, group in grouped:
        # 'Audi' -> Audi
        name = name[1:-1]
        group.to_csv(f'{output}/{name}_data.csv', index=False)  # 按分类名生成文件


def data_clean(df: DataFrame, output):
    """
    数据清洗
    :return:
    """
    df.replace('?', np.nan, inplace=True)
    cleaned_df = df.dropna()
    cleaned_df.to_csv(f"{output}/data_clean.csv", index=False)

if __name__ == "__main__":
    # 1.使用pandas库读取数据集
    df = pd.read_csv(dataset_path, encoding="utf-8")

    data_clean(df,"./dataset")
    split_in_brand(df, "./dataset/brand")
