import requests
from typing import List, Dict


class ProposicoesAPIClient:
    BASE_URL = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def fetch_all(self) -> List[Dict]:
        proposicoes = []
        pagina = 1

        while True:
            params = {
                "pagina": pagina,
                "itens": 100,
                "ordem": "DESC",
                "ordenarPor": "ano"
            }

            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()

            data = response.json()
            dados = data.get("dados", [])

            if not dados:
                break

            proposicoes.extend(dados)
            print(f"Página {pagina} processada ({len(dados)} registros)")
            pagina += 1

        return proposicoes
