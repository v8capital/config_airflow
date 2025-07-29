from v8_utilities.anbima_calendar import Calendar
from config import Config

class SingulareConfig(Config):
    def __init__(self, path, fund_list = None, date_list = None):
        super().__init__(path)
        if fund_list is None:
            fund_list = ["BS_PLUS_NP",
                         "FIRMA",
                         "FIRMA_I_FIDC_SUB_JN",
                         "FIRMA_I_FIDC_SENIOR_1",
                         "FIRMA_I_FIDC_SENIOR_2",
                         "FIRMA_I_FIDC_SENIOR_3",
                         "FIRMA_I_FIDC_SENIOR_4",
                         "FIRMA_I_FIDC_SUBORDINADA_MEZANINO_1",
                         "FIRMA_I_FIDC_SUBORDINADA_MEZANINO_2",
                         "FIRMA_I_FIDC_SUBORDINADA_MEZANINO_3",
            ]
        self.fund_list = fund_list

        if date_list is None:
            calendar_handle = Calendar(folder = ".")
            start_date = calendar_handle.today(-4)
            end_date = calendar_handle.today(-1)
            date_list = calendar_handle.list_dates_between(start_date, end_date, ascending=False)
        self.date_list = date_list