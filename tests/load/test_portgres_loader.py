from load.postgres_deputados import PostgresDeputadoLoader


def test_upsert_lista_vazia_nao_falha(mocker):
    engine_mock = mocker.Mock()
    loader = PostgresDeputadoLoader(engine_mock)

    loader.upsert([])

    assert True
