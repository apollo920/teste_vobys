import requests
from typing import List, Dict

class DeputadosAPIClient:
    BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"
    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def _get(self, endpoint: str, params: Dict = None) -> Dict:
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, params=params, timeout=self.timeout)
        if response.status_code != 200:
            raise RuntimeError(
                f"Erro ao acessar {url} | Status: {response.status_code}"
            )
        return response.json()
    def get_deputados(self) -> List[Dict]:
        deputados: List[Dict] = []
        pagina = 1

        while True:
            params = {
                "pagina": pagina,
                "itens": 100,
                "ordem": "ASC",
                "ordenarPor": "nome"
            }

            data = self._get("/deputados", params=params)
            dados_pagina = data.get("dados", [])

            if not dados_pagina:
                break

            deputados.extend(dados_pagina)
            print(f"Página {pagina} processada ({len(dados_pagina)} registros)")
            pagina += 1

        return deputados
    
    def fetch_all(self) -> List[Dict]:
        return self.get_deputados()