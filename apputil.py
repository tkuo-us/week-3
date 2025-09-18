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
     

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df = pd.read_csv(url)

df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
df["year"] = df["date_in"].dt.year

def task_1():
    """
    Return a list of all column names in df_bellevue
    Sorted by the number of NA values in each column, from fewest NA values to most NA values.
    """
    tmp = df.copy()

    g = (tmp["gender"].astype(str).str.lower().str.strip()) # clean gender
    tmp.loc[~g.isin(["m", "w"]), "gender"] = pd.NA

    cols = [c for c in tmp.columns if c != "year"] # clen year
    
    ordered = tmp[cols].isna().sum().sort_values().index.tolist()

    return ordered


def task_2():
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

def task_3():
    """
    Return the average age of genders "m" and "w"
    as a Series indexed by
    """
    tmp = df.copy()
    tmp["age"] = pd.to_numeric(tmp["age"], errors="coerce")
    tmp["gender"] = tmp["gender"].str.lower().str.strip() # normalize
    tmp.loc[~tmp["gender"].isin(["m", "w"]), "gender"] = pd.NA # only keep "m" and "w", set others to NA
    return tmp.groupby("gender")["age"].mean()

def task_4():
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