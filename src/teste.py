import sys
sys.path.insert(0, "C:\\GitHub\\utilities")

from singulareconfig import SingulareConfig
from fidcsconfig import FidcsConfig
from datetime import date
from v8_utilities.anbima_calendar import Calendar

config = SingulareConfig(path=".")
config.generate_config_file()

config = FidcsConfig(path = ".")
config.generate_config_file()