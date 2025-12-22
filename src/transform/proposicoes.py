from typing import List, Dict
from datetime import datetime


class transform_proposicoes:

    @staticmethod
    def transform(raw: List[Dict]) -> List[Dict]:
        now = datetime.utcnow()
        proposicoes = []

        for p in raw:
            proposicoes.append({
                "id_proposicao": p.get("id"),
                "sigla_tipo": p.get("siglaTipo"),
                "numero": p.get("numero"),
                "ano": p.get("ano"),
                "ementa": p.get("ementa"),
                "data_apresentacao": p.get("dataApresentacao"),
                "status_descricao": (
                    p.get("statusProposicao", {}).get("descricaoSituacao")
                ),
                "data_atualizacao": now
            })

        return proposicoes
