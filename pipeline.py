import os, os.path
from modules import data_quality as dq, file_check as fc

def __get_file_list() -> list:
    gen = os.walk('./unprocessed')
    return list(gen)[0][2]

def process_file(file: str):
    file_check = fc.FileCheck(filename=file)
    if file_check.is_valid():
        file_check.load_csv(location='unprocessed')
        if file_check.df_status:
            quality = dq.Quality(file_check.df)
            quality.separate_invalid_rows(invalid_folder=file_check.invalid_folder)
            quality.clean_fields()
            quality.validate_phone_number()
            quality.write_processed_csv(file_check.processed_folder, file_check.filename)
            print(f"All checks were successfully ran on file {file_check.filename}")
        else:
            print(f"File {file_check.filename} cannot be loaded into pandas DataFrame")
    else:
        if file_check.extension == 'csv':
            target = file_check.move_invalid_file()
            print(f"File has been moved to {target} as it is invalid.")

if __name__ == "__main__":
    file_list = __get_file_list()
    for file in file_list:
        process_file(file)