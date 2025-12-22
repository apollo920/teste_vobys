from src.transform.deputados import DeputadoTransformer


def test_transform_deputado_completo():
    deputado_raw = [{
        "id": 123,
        "nome": " João da Silva ",
        "siglaPartido": "ABC",
        "siglaUf": "SP",
        "email": "joao@camara.leg.br",
        "idLegislatura": 57
    }]

    resultado = DeputadoTransformer.transform(deputado_raw)

    assert len(resultado) == 1
    deputado = resultado[0]

    assert deputado["id_deputado"] == 123
    assert deputado["nome"] == "João da Silva"
    assert deputado["sigla_partido"] == "ABC"
    assert deputado["sigla_uf"] == "SP"
    assert deputado["email"] == "joao@camara.leg.br"
    assert deputado["id_legislatura"] == 57


def test_transform_falha_sem_campo_obrigatorio():
    deputado_raw = [{
        "nome": "Sem ID",
        "siglaPartido": "XYZ",
        "siglaUf": "RJ"
    }]

    try:
        DeputadoTransformer.transform(deputado_raw)
        assert False
    except ValueError as e:
        assert "Campo obrigatório ausente" in str(e)
