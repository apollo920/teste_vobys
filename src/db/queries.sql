-- SELECT

-- total de deputados
SELECT COUNT(*) AS total_deputados
FROM deputados;

-- deputados por partido
SELECT sigla_partido, COUNT(*) AS total 
FROM deputados
GROUP BY sigla_partido
ORDER BY total DESC;

-- deputados por estado (UF)
SELECT sigla_uf, COUNT(*) AS total
FROM deputados
GROUP BY sigla_uf
ORDER BY total DESC;

-- deputados do partido PL
SELECT nome, sigla_uf
FROM deputados
WHERE sigla_partido = 'PL';

-- deputados do ceará
SELECT nome, sigla_uf 
FROM deputados 
WHERE sigla_uf = 'CE';

-- INSERT

INSERT INTO deputados (
    id_deputado, 
    nome,
    sigla_partido,
    sigla_uf,
    email,
    id_legislatura
)
VALUES (
    99999,
    'João da Silva',
    'PL',
    'SP',
    'joao.silva@camara.gov.br',
    56
);


-- DELETE 

DELETE FROM deputados
WHERE id_deputado = 99999;