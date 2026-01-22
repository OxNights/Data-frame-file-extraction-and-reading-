import pandas as pd

d = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Nairobi", "London", "New York"]
}

df = pd.DataFrame(d)
print(df)
