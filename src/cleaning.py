import pandas as pd
import numpy as np
import re

def reg_digit(x):
    return re.findall(r'\d+', x)

def convert_to_int_if_error_return_zero(x):
    try:
        return int(x)
    except:
        return 0

def price_clean(df):
    df["price_int"] = df["price"].apply(lambda x: "".join(reg_digit(x)))
    df["price_int"] = df["price_int"].apply(convert_to_int_if_error_return_zero)
    df["price"] = df["price_int"]
    df = df.drop("price_int", axis=1)
    return df

def postcode_split(df):
    df["postcode"] = df["postcode"].str.split()
    df["postcode"] = df["postcode"].apply(lambda x: x[-1])
    return df

def postcode_dummy(df):
    df = pd.get_dummies(df)
    return df

if __name__ == "__main__":
    df = pd.read_csv("zoopla_rentals.csv", index_col=0)
    df = price_clean(df)
    df = postcode_split(df)
    df = postcode_dummy(df)
    df.to_csv("zoopla_clean_df.csv")