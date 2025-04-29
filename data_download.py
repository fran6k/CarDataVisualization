import kagglehub

if __name__ == "__main__":
    # 下载数据集
    path = kagglehub.dataset_download("adilshamim8/sports")
    print("Path to dataset files:", path)
