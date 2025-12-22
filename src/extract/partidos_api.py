import requests
from typing import List, Dict


class PartidosAPIClient:
    BASE_URL = "https://dadosabertos.camara.leg.br/api/v2/partidos"

    def fetch_all(self) -> List[Dict]:
        partidos = []
        pagina = 1

        while True:
            params = {
                "pagina": pagina,
                "itens": 100
            }

            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()

            data = response.json()
            dados = data.get("dados", [])

            if not dados:
                break

            partidos.extend(dados)
            print(f"Página {pagina} processada ({len(dados)} registros)")
            pagina += 1

        return partidos
