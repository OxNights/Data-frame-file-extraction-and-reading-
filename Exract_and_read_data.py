import pandas as pd

data = pd.read_csv(
    r"E:\Oxnights\Data Science\Data sets\Sales Data.csv",
    encoding="latin1"
)

data.dropna(axis=0, inplace=True)

print(data)
print(data.info())
