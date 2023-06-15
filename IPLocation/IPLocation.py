#!/usr/bin/env python3
from cortexutils.analyzer import Analyzer
import requests

class IPLocation(Analyzer):

    def summary(self, raw):
        taxonomies = []
        level = 'safe'
        namespace = 'IPLocation'
        predicate = 'Pais'
        value = "N/A"
        if "country_name" in raw:
            value = "{}".format(raw["country_name"])
        taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))
        return {'taxonomies': taxonomies}

    def run(self):
        Analyzer.run(self)

        observable = self.get_data()
        query = f"https://api.iplocation.net/?ip={observable}"
        respuesta = requests.get(query)

        if respuesta.status_code == 200:
            self.report(respuesta.json())


        else:
            self.report("No se pudo obtener la información")

if __name__ == '__main__':
    IPLocation().run()
