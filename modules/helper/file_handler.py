import os
import pandas as pd

class FileHandler:

    def __init__(self, filename):
        self.filename = filename
        self.processed_folder = os.getcwd() + '/processed/'
        self.unprocessed_folder = os.getcwd() + '/unprocessed/'
        self.failed_folder = os.getcwd() + '/invalid/'
        self.extension = filename.rsplit('.', 1)[-1]

    def load_csv(self, location: str) -> pd.DataFrame:
        if location == 'processed':
            filepath = self.processed_folder + self.filename
        elif location == 'unprocessed':
            filepath = self.unprocessed_folder + self.filename
        
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            print("File not found.")
            self.df_status = False
        except pd.errors.ParserError:
            print("There was a parser error")
            self.df_status = False
        else:
            self.df_status = True
            self.df = df