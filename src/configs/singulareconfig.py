from config import Config

class SingulareConfig(Config):
    def __init__(self, path, folder_root = "", fund_list = None, date_list = None):
        super().__init__(path, folder_root)
        if fund_list is None:
            fund_list = ["BS_PLUS_NP",
                         "FIRMA",
                         #"FIRMA_I_FIDC_SUB_JN",
                         #"FIRMA_I_FIDC_SENIOR_1",
                         #"FIRMA_I_FIDC_SENIOR_2",
                         #"FIRMA_I_FIDC_SENIOR_3",
                         #"FIRMA_I_FIDC_SENIOR_4",
                         #"FIRMA_I_FIDC_SUBORDINADA_MEZANINO_1",
                         #"FIRMA_I_FIDC_SUBORDINADA_MEZANINO_2",
                         #"FIRMA_I_FIDC_SUBORDINADA_MEZANINO_3",
            ]
        self.fund_list = fund_list
        self.date_list = date_list

        class_name = self.__class__.__name__.lower()
        self.filename = f"{class_name}.json"