from extract.deputados_api import CamaraAPIClient

def test_get_deputados():
    client = CamaraAPIClient()
    deputados = client.get_deputados()

    assert isinstance(deputados, list)
    assert len(deputados) > 0

def test_estrutura_basica_deputado():
    client = CamaraAPIClient()
    deputados = client.get_deputados()

    deputado = deputados[0]

    assert "id" in deputado
    assert "nome" in deputado
    assert "siglaPartido" in deputado
    assert "siglaUf" in deputado
