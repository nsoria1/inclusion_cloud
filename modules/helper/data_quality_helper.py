import pandas as pd
import numpy as np
import re
import ast

phone_target = ['phone_1', 'phone_2']

def clean_special_chars(series: str) -> str:
    if series is not None:
        series = series.encode("utf8",errors='replace').decode().replace('\n', ' ').replace('\r', '').replace('??????????.', '')
        series = re.sub(r'\\[tn]', '', series)
        series = re.sub(r'\\x..', '', series)
        series = ''.join(c for c in series if ord(c) < 128)
    return series

def clean_reviews_list(data: str) -> str:
    data = clean_special_chars(data)
    data = ast.literal_eval(data)
    for tup in data:
        tmp = list(tup)
        for idx, v in enumerate(tmp):
            tmp[idx] = clean_special_chars(v)
        tup = tuple(tmp)
    return str(data)

def process_phone(row: pd.Series) -> tuple:
    empty_tuple = []
    empty_tuple.append(np.NaN)
    empty_tuple.append(np.NaN)
    phone = row['phone'].strip()
    if phone in ('na', 'nan') or phone is None:
        return pd.Series(empty_tuple)
    else:
        split = phone.split('\r\n', 1)
        for idx, s in enumerate(split):
            s = re.sub(r'[^0-9]', '', s).replace('+', '')
            split[idx] = s if len(s) != 0 else np.NaN
    if len(split) == 0:
        return pd.Series(empty_tuple)
    elif len(split) == 1:
        split.append(np.NaN)
    return pd.Series(split)

def get_non_nulls(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df.replace('nan', np.NaN, inplace=True)
    df.replace('na', np.NaN, inplace=True)
    return df[df[columns].notnull().all(1)]

def get_nulls(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df.replace('nan', np.NaN, inplace=True)
    df.replace('na', np.NaN, inplace=True)
    cols = columns.copy()
    for idx, l in enumerate(cols):
        cols[idx] = l + '.isna()'
    filter = ' or '.join(cols)
    return df.query(filter, engine='python')