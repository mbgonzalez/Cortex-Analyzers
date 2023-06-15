#!/usr/bin/env python3
from cortexutils.analyzer import Analyzer
import requests

class IPLocation(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)

    def run(self):
        Analyzer.run(self)
        if self.data_type == "ip":
            observable = self.get_data()
            url = f"https://api.iplocation.net/?ip={observable}"
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                return respuesta.json()
            else:
                print("No se pudo realizar la consulta IP Location.")
                return None
        else:
            self.notSupported()

  
if __name__ == '__main__':
    IPLocation().run()
