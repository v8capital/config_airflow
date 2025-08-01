from config import Config
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FidcsConfig(Config):
    def __init__(self, path, folder_root = "", fidcs_list=None, date=None):
        super().__init__(path, folder_root)

        if fidcs_list is None:
            fidcs_list = []  # caso seja vazio eu uso a função da classe Extractor
        self.fidcs_list = fidcs_list
        self.result_fidcs_list = []

        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()

        if date is None:
            date = self.today

        date = date.replace(day=1)

        date_last_month = date - relativedelta(months=1) # sempre pegando 1 mes antes

        self.date = date_last_month

        class_name = self.__class__.__name__.lower()
        date_ = self.date.strftime("%Y_%m_%d")
        self.filename = f"{class_name}_{date_}.json"