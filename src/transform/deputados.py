from typing import Dict, List
from datetime import datetime

class transform_deputados:

    @staticmethod
    def transform(deputados_raw: List[Dict]) -> List[Dict]:
        deputados_transformados = []

        for deputado in deputados_raw:
            deputado_transformado = transform_deputados._transform_single(deputado)
            deputados_transformados.append(deputado_transformado)

        return deputados_transformados
    
    @staticmethod
    def _transform_single(deputado: Dict) -> Dict:
        required_fields = ["id", "nome", "siglaPartido", "siglaUf"]

        for field in required_fields:
            if field not in deputado:
                raise ValueError(f"Campo obrigatório ausente: {field}")

        return {
            "id_deputado": deputado["id"],
            "nome": deputado["nome"].strip(),
            "sigla_partido": deputado["siglaPartido"].strip(),
            "sigla_uf": deputado["siglaUf"].strip(),
            "email": deputado.get("email"),
            "id_legislatura": deputado.get("idLegislatura"),
            "data_atualizacao": datetime.utcnow()
        }