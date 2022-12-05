import os
from .helper.file_handler import FileHandler

class FileCheck(FileHandler):
    def __check_existence(self) -> bool:
        return os.path.exists(self.processed_folder + self.filename)

    def __check_empty(self) -> bool:
        if os.path.exists(self.unprocessed_folder + self.filename):
            return os.stat(self.unprocessed_folder + self.filename).st_size == 0
        else:
            return True

    def __check_file_extension(self) -> bool:
        return True if self.extension == 'csv' else False

    def is_valid(self) -> bool:
        extension = self.__check_file_extension()
        empty = self.__check_empty()
        exists = self.__check_existence()

        return True if extension is True and empty is False and exists is False else False