-- tabela de deputados
CREATE TABLE IF NOT EXISTS deputados (
    id_deputado INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sigla_partido VARCHAR(30) NOT NULL,
    sigla_uf CHAR(2) NOT NULL,
    email VARCHAR(150),
    id_legislatura INTEGER NOT NULL,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_deputados_partido
    ON deputados(sigla_partido);

CREATE INDEX idx_deputados_uf
    ON deputados(sigla_uf);

-- tabela de partidos 
CREATE TABLE IF NOT EXISTS partidos (
    id_partido INTEGER PRIMARY KEY,
    sigla VARCHAR(30) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

-- tabela de proposições
CREATE TABLE IF NOT EXISTS proposicoes (
    id_proposicao INTEGER PRIMARY KEY,
    sigla_tipo VARCHAR(10),
    numero INTEGER,
    ano INTEGER,
    ementa TEXT,
    data_apresentacao DATE,
    status_descricao TEXT,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


