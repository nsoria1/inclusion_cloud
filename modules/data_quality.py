import time
import pandas as pd
from .helper.data_quality_helper import get_non_nulls, get_nulls, clean_reviews_list, clean_special_chars, process_phone

class Quality():

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.__non_null_columns = ['name', 'phone', 'location']
        self.__clean_columns = ['address', 'reviews_list']

    def write_processed_csv(self, process_folder: str, filename: str):
        self.df.to_csv(process_folder + filename, index=False)

    def separate_invalid_rows(self, invalid_folder: str) -> bool:
        filename = invalid_folder + 'invalid_file_' + time.strftime("%Y%m%d_%H%M%S") + '.csv'
        try:
            df_nulls = get_nulls(self.df, self.__non_null_columns)
            df_nulls.to_csv(filename, index=False)
            self.df = get_non_nulls(self.df, self.__non_null_columns)
            return True
        except Exception as e:
            print(e)
            return False

    def clean_fields(self) -> bool:
        try:
            for c in self.__clean_columns:
                if c == 'reviews_list':
                    self.df[c] = self.df[c].apply(clean_reviews_list)
                    print(f"Cleaned the column list {c}")
                else:
                    self.df[c] = self.df[c].apply(clean_special_chars)
                    print(f"Cleaned column {c}")
            return True
        except Exception as e:
            print(e)
            return False
                

    def validate_phone_number(self) -> bool:
        phone_target = ['phone_1', 'phone_2']
        try:
            self.df[phone_target] = self.df.apply(process_phone, axis=1)
            return True
        except Exception as e:
            print(e)
            return False