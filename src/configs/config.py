import json
import os
import pandas as pd
from abc import ABC
from datetime import date, datetime
from v8_utilities.anbima_calendar import Calendar

class Config(ABC):
    def __init__(self, path: str, folder_root = ""):
        self.path = path  # Diretório onde o JSON será salvo
        self.folder_root = folder_root # Lugar onde a saída da rotina será salva
        self.consumed = False  # Indica se o arquivo já foi consumido

        calendar_handle = Calendar(folder = ".")
        self.today = calendar_handle.today().date()

    def safe_serialize(self, value):
        if isinstance(value, list):
            return [self.safe_serialize(v) for v in value]
        if isinstance(value, (datetime, date, pd.Timestamp)):
            return value.isoformat()
        return value

    def generate_config_file(self):
        # Gera o nome do arquivo no formato NomeDaClasse_YYYY-MM-DD.json
        filepath = os.path.join(self.path, self.filename)

        # Cria o diretório se não existir
        os.makedirs(self.path, exist_ok=True)

        # Prepara os dados (excluindo 'path')
        data = {
            k: self.safe_serialize(v)
            for k, v in self.__dict__.items()
            if k != "path"
        }

        # Escreve o JSON no arquivo
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)