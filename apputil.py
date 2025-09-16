import seaborn as sns
import pandas as pd


# update/add code below ...
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def to_binary(n):
    """
    Converts an Integer into a Binary String
    0(0) 1(1) 2(10) 3(11) 4(100) 5(101) 6(110) 7(111) 8(1000) 9(1001) ...
    """   
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)
     

def task_1(df: pd.DataFrame):
    """
    Return a list of all column names in df_bellevue
    Sorted by the number of NA values in each column, from fewest NA values to most NA values.
    """
    return df.isna().sum().sort_values().index.tolist()

def task_2(df: pd.DataFrame):
    """
    Return total number of entries for each year：
    - year
    - total_admissions
    """
    output = (
        df
        .dropna(subset=["year"])                # year is NaN for some rows
        .groupby("year", as_index=False)
        .size()
        .rename(columns={"size": "total_admissions"})
        .sort_values("year")
        .reset_index(drop=True)
    )
    return output

def task_3(df: pd.DataFrame):
    """
    Return the average age of genders "m" and "w"
    as a Series indexed by
    """
    tmp = df.copy()
    tmp["age"] = pd.to_numeric(tmp["age"], errors="coerce")
    tmp["gender"] = tmp["gender"].str.lower().str.strip() # normalize
    tmp.loc[~tmp["gender"].isin(["m", "w"]), "gender"] = pd.NA # only keep "m" and "w", set others to NA
    return tmp.groupby("gender")["age"].mean()

def task_4(df: pd.DataFrame):
    """
    Return TOP 5 profession
    """
    return (
        df["profession"]
        .dropna()
        .astype(str)
        .str.strip()
        .value_counts()
        .head(5)
        .index
        .tolist()
    )