# API de Análise de Vendas

Esta API permite analisar dados de vendas de forma rápida e interativa.

## Funcionalidades
- Endpoints para consultar vendas
- Relatórios básicos
- Documentação interativa via Swagger (/docs)

## Como rodar localmente

1. Clone o repositório:
   git clone https://github.com/Pri-scila/api-analise-vendas.git
   cd api-analise-vendas

2. Instale as dependências:
   pip install fastapi uvicorn pandas

3. Rode a API:
   uvicorn main:app --reload

4. Acesse a documentação interativa no navegador:
   http://127.0.0.1:8000/docs

## Estrutura do projeto
- app/ → Código da API (routes, services, __init__.py)  
- data/ → Arquivos de dados (vendas.csv)  
- main.py → Arquivo principal que roda a API  
- README.md → Este arquivo  
- .gitignore → Arquivos que não vão para o GitHub  

## Observações
- Arquivos de cache do Python (__pycache__) são ignorados pelo .gitignore.
- Atualize este README conforme novas funcionalidades forem adicionadas.