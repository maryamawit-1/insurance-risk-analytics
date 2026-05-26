import pandas as pd


def convert_raw_to_csv():
    df = pd.read_csv("data/MachineLearningRating_v3.txt", sep="|")
    df.to_csv("data/insurance_data.csv", index=False)

    print("Conversion complete")
    print(df.shape)


if __name__ == "__main__":
    convert_raw_to_csv()