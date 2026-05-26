import pandas as pd


def clean_data():
    df = pd.read_csv("data/insurance_data.csv")

    df = df.drop_duplicates()

    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    categorical_cols = df.select_dtypes(include=["object"]).columns
    df[categorical_cols] = df[categorical_cols].fillna("Unknown")

    df.to_csv("data/insurance_data_clean.csv", index=False)

    print("Cleaning complete")
    print(df.shape)


if __name__ == "__main__":
    clean_data()