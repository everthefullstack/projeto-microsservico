# Projeto Microsserviço

Este projeto é uma aplicação web desenvolvida com FastAPI. Abaixo estão as instruções para configurar e executar a aplicação.

## Principais tecnologias utilizados

**Back-end:** Python, FastApi, SqlModel, Dynaconf, PostgreSQL, Pytest, Httpx, Uvicorn, Pydantic

## Estrutura do Projeto

```
projeto_microsservico
├── app
    ├── application        # Lógica do negócio
    ├── domain             # Regras de negócio
    ├── infra              # Dependências externas
    ├── presentation       # Exposição da aplicação
│   ├── create_app.py      # Criação do app
├── tests
|       ├── integration    # Testes de integração
|       ├── unit           # Testes unitários
│       └── conftest.py    # Fixtures dos testes
|── .gitignore             # Arquivos ignorados pelo git
├── .python-version        # Versão do python utilizada pelo uv
├── docker-compose.yml     # Construtor dos containers
├── Dockerfile-app         # Instruções para construir a imagem Docker da aplicação
├── Dockerfile-app         # Instruções para construir a imagem Docker do banco de dados
├── main.py                # Ponto de entrada da aplicação
├── pyproject.toml         # Lista de dependências do projeto
|── README.md              # Documentação do projeto
|── run_tests.py           # Configura e executa a bateria de testes
|── settings.toml          # Configurações usadas pelo Dynaconf baseado no ambiente em que a aplicação está rodando
└── uv.lock                # Lista detalhada de dependências do projeto gerada pelo uv
```


## Explicação sobre o desenvolvimento da solução

O desenvolvimento inicial da aplicação não tem complicações, visto que é um microsserviço com apenas dois endpoints.
Fiz a utilização da Clean Architecture pois facilita a separação do domínio da aplicação dos módulos utilizados.
Para a manutenção é muito bom, pois caso exista a necessidade de trocar de tecnologia, é possível fazer facilmente, visto que praticamente tudo é desacoplado.
A dificuldade surgiu nas tarefas bônus.
Na primeira, onde devemos ordenar pela localização, pesquisei fórmulas que pudessem me ajudar a calcular e escolhi a de Haversine,
que tem uma boa precisão, uma performance rápida e ja é amplamente utilizada para geolocalização. Sobre seu funcionamento, em resumo
ela é uma equação para calcular a distancia entre dois pontos em uma esfera com base na latitude e longitude. 
Na segunda, onde devemos buscar documentos não mais por palavra chave, e sim por expressão, tive de pesquisar como isso era feito e descobri o Full Text Search.
Em resumo, é um mecanismo que permite buscar palavras, frases ou expressões em grandes volumes de texto, performando muito melhor que o LIKE ou o ILIKE.
Esse mecanismo entende as variações linguísticas, logo, se fizer uma busca por um termo "Matemática", pode encontrar também "Matemático", "Matematicamente", etc.
No banco de dados Postgresql(que eu utilizei), existe todo um aparato para fazer esse tipo de mecanismo de busca.

## Pré-requisitos

- Python 3.13 ou superior
- Docker

## Instalação

Clone o projeto

```bash
git clone https://github.com/everthefullstack/projeto_microsservico
```

## Executando a Aplicação

Para construir e executar a aplicação usando Docker, siga os passos abaixo:

Escolha qual ambiente você quer usar. Baseado no ambiente, algumas configurações são diferentes.
As configurações em default, serão válidas para todos os ambientes.
Dentro do arquivo settings.toml existem as configurações que serão usadas para cada ambiente.
Por exemplo, se usar o development, o banco de dados é X, se for production é Y.
Para isso, altere o valor da variável dentro do arquivo Dockerfile-app, como por exemplo:

```bash
ENV ENV_FOR_DYNACONF=production
```

Ou

```bash
ENV ENV_FOR_DYNACONF=development
```

Construa as imagem Docker com docker compose:

```bash
docker-compose up --build -d
```

Para deletar tudo:

```bash
docker-compose down -v
```

A aplicação estará disponível em `http://localhost:8000`.\
A documentação estará disponível em `http://localhost:8000/docs`.

Para fazer uma carga de dados inicial:
```bash
python tests/carga_inicial.py
```


## Possíveis melhorias

Esta aplicação não utiliza conceitos de autenticação, logo, seria interessante criar um para a mesma.\
Utilizaria uma autenticação baseada em JWT.\
Para uma aplicação tão pequena, poderia também ter sido feita com MVC.\
Para uma melhor performance, seria interessante refatorar o código para uma metodologia async.\
A utilização de logs para observabilidade também seria interessante, a modo de gerar métricas e/ou tomada de ações.