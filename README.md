# 📊 VOBYS — Painel Analítico da Câmara dos Deputados

## 📌 Visão Geral

Projeto completo de **engenharia de dados e analytics**, que implementa uma **pipeline ETL automatizada** para coletar, transformar, armazenar e visualizar dados públicos da **Câmara dos Deputados do Brasil**, utilizando tecnologias modernas e amplamente adotadas no mercado.

O projeto vai **além do escopo básico solicitado**, incorporando:
- Orquestração com **Apache Airflow**
- Persistência em **PostgreSQL**
- Visualização interativa com **Streamlit**
- Ambiente totalmente conteinerizado com **Docker**
- Organização baseada em **SOLID**, **Clean Code** e boas práticas de versionamento

---

## 🏗️ Arquitetura Geral

```
API Câmara dos Deputados
        ↓
    ETL (Python)
        ↓
PostgreSQL (camara)
        ↓
┌───────────────┐
│ Apache Airflow│ → Orquestração diária
└───────────────┘
        ↓
┌───────────────┐
│   Streamlit   │ → Painel Analítico
└───────────────┘
```

Toda a infraestrutura é reproduzível via **Docker Compose**, garantindo portabilidade entre ambientes.

---

## 🗄️ Escolha do Banco de Dados — PostgreSQL

### ✅ Por que PostgreSQL?

O PostgreSQL foi escolhido por ser um banco **relacional robusto**, amplamente utilizado em pipelines de dados e ambientes corporativos.

### Pontos Positivos
- 🧱 Confiável e maduro
- 📈 Excelente para consultas analíticas
- 🔐 Forte suporte a integridade e transações
- 🐳 Fácil integração com Docker
- ⚙️ Compatível nativamente com Airflow, SQLAlchemy e Pandas

### Pontos Negativos
- ❌ Não é ideal para ingestão massiva em tempo real (streaming)
- ❌ Escala horizontal exige mais configuração do que bancos NoSQL

➡️ Para o contexto do projeto (ETL batch diário + análises), o PostgreSQL é a **melhor escolha custo-benefício**.

---

## 🧠 Metodologia Utilizada

### 🔁 ETL (Extract, Transform, Load)

A pipeline foi separada em **camadas bem definidas**:

```
src/
├── extract/     # Coleta via API
├── transform/   # Limpeza e padronização
├── load/        # Persistência no banco
└── etl/         # Orquestração do fluxo
```

Cada etapa é:
- Testável
- Independente
- Reutilizável

---

## 🧼 SOLID e Clean Code

O projeto segue princípios de **engenharia de software**, não apenas scripts isolados.

### Aplicações práticas:
- **Single Responsibility**: cada módulo tem uma função clara
- **Open/Closed**: fácil extensão de novas fontes ou tabelas
- **Dependency Injection**: conexões e configurações desacopladas
- Código legível, previsível e organizado

Isso facilita:
- Manutenção
- Escalabilidade
- Colaboração entre desenvolvedores

---

## ⏱️ Orquestração com Apache Airflow

O **Airflow** é responsável por:
- Executar o ETL automaticamente
- Agendar a atualização diária dos dados
- Monitorar falhas e execuções

### DAG principal:
- Execução diária às **06:00**
- Sem `catchup`
- Logs persistidos via volume Docker

A execução do ETL ocorre dentro de um **container dedicado**, garantindo isolamento e consistência.

---

## 📊 Visualização com Streamlit

O Streamlit foi utilizado como um **painel analítico completo**, contendo:

- Métricas gerais (cards)
- Gráficos por partido, UF e ano
- Evolução temporal das proposições
- Tabelas interativas
- Interface limpa e responsiva

Isso transforma o projeto em um **produto final utilizável**, e não apenas uma pipeline técnica.

---

## 🐳 Docker e Conteinerização

Todo o projeto é executado via **Docker Compose**, incluindo:

- PostgreSQL
- Airflow (init, webserver, scheduler)
- ETL
- Streamlit

### Benefícios:
- 🔁 Reprodutibilidade total
- 🧩 Isolamento de dependências
- 🚀 Deploy simples em qualquer ambiente

---

## 🔐 Configuração de Ambiente (.env)

O projeto utiliza **um único `.env` na raiz**, centralizando credenciais e configurações sensíveis.

Exemplo (`.env.example`):

```env
DB_HOST=postgres
DB_PORT=5432
DB_NAME=camara
DB_USER=postgres
DB_PASSWORD=senha_segura

AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres:senha_segura@postgres:5432/airflow

AIRFLOW_ADMIN_USER=admin
AIRFLOW_ADMIN_PASSWORD=admin
AIRFLOW_ADMIN_EMAIL=admin@local
```

---

## ▶️ Como Rodar o Projeto

### 🔧 Pré-requisitos
- Docker
- Docker Compose
- Git

### 🪟 Windows | 🐧 Linux | 🍎 macOS
Os passos são idênticos para todos os sistemas.

### Clonar o repositório
```bash
git clone https://github.com/apollo920/vobys.git
cd vobys
```
### Criar o venv
```bash
py -3.10 -m venv venv
```
### Ativar o venv
```bash
venv/Scripts/activate
```

### Instalar as bibliotecas dentro do venv
```bash
pip install -r requirements.txt
```

### Criar o .env
```bash
cp .env.example .env
```
Ajuste as variáveis conforme necessário.

### Subir toda a stack
```bash
docker-compose up -d --build
```

### Acessos

| Serviço    | URL                    |
|------------|------------------------|
| Streamlit  | http://localhost:8501  |
| Airflow    | http://localhost:8080  |
| PostgreSQL | localhost:5432         |

**Credenciais do Airflow:**
```
Usuário: admin
Senha: admin
```

### 🔄 Execução Manual do ETL (opcional)
```bash
docker exec -it etl python -m src.etl.run_etl
```

---

## 📁 Versionamento com Git

- `.env` ignorado via `.gitignore`
- Código organizado por domínio
- Commits incrementais e semânticos
- Separação clara entre infraestrutura, backend e visualização

---

## 🚀 Conclusão

Este projeto demonstra domínio em:

- Engenharia de Dados
- Orquestração de pipelines
- Containers e deploy
- Visualização analítica
- Boas práticas de código
- Arquitetura escalável
