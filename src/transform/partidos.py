from typing import List, Dict
from datetime import datetime


def transform_partidos(raw_partidos: List[Dict]) -> List[Dict]:
    transformed = []
    now = datetime.utcnow()

    for p in raw_partidos:
        transformed.append({
            "id_partido": p.get("id"),
            "sigla": p.get("sigla"),
            "nome": p.get("nome"),
            "data_atualizacao": now
        })

    return transformed
