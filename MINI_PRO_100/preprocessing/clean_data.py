import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(path):

    df = pd.read_csv(path)

    # Convert text columns to numbers
    enc = LabelEncoder()

    df["file_type"] = enc.fit_transform(df["file_type"])
    df["owner_type"] = enc.fit_transform(df["owner_type"])
    df["data_category"] = enc.fit_transform(df["data_category"])

    # Features and label
    X = df.drop("label", axis=1)
    y = df["label"]

    return X, y