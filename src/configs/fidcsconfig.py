from config import Config
from datetime import datetime

class FidcsConfig(Config):
    def __init__(self, path, folder_root = "", fidcs_list=None, date=None):
        super().__init__(path, folder_root)

        if fidcs_list is None:
            fidcs_list = []  # caso seja vazio eu uso a função da classe Extractor
        self.fidcs_list = fidcs_list

        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()

        if date is None:
            date = self.today

        date = date.replace(day=1)

        self.date = date

        class_name = self.__class__.__name__.lower()
        date_ = self.date.strftime("%Y_%m_%d")
        self.filename = f"{class_name}_{date_}.json"