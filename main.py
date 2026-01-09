from fastapi import FastAPI, UploadFile, HTTPException
import pandas as pd
import logging

# -------------------------
# Configuração do Logging
# -------------------------
logging.basicConfig(
    filename='app.log',             # arquivo de log
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -------------------------
# Inicializa a API
# -------------------------
app = FastAPI(title="API de Análise de Vendas")

# -------------------------
# Função para processar arquivos
# -------------------------
def process_file(file):
    """
    Lê CSV ou XLSX, limpa, valida e padroniza dados.
    Retorna um DataFrame pandas.
    """
    # Leitura
    try:
        if hasattr(file, "read"):
            # Arquivo enviado via UploadFile
            df = pd.read_csv(file) if file.filename.endswith('.csv') else pd.read_excel(file)
        else:
            raise ValueError("Arquivo inválido")
    except Exception as e:
        logger.error(f"Erro ao ler arquivo: {str(e)}")
        raise ValueError("Erro ao ler arquivo. Formato inválido ou corrompido.")

    # Colunas obrigatórias
    required_columns = [
        'id_transacao', 'data_venda', 'valor_final', 'subtotal',
        'desconto_percent', 'canal_venda', 'forma_pagamento'
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória faltando: {col}")

    # Limpeza de nulos
    df.dropna(subset=['valor_final'], inplace=True)

    # Validação de tipos
    df['valor_final'] = pd.to_numeric(df['valor_final'], errors='coerce')
    df['subtotal'] = pd.to_numeric(df['subtotal'], errors='coerce')
    df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')

    # Padronização de textos
    df['canal_venda'] = df['canal_venda'].str.lower()
    df['forma_pagamento'] = df['forma_pagamento'].str.lower()

    return df

# -------------------------
# Endpoint de upload
# -------------------------
@app.post("/upload")
async def upload_file(file: UploadFile):
    if not file:
        logger.error("Nenhum arquivo enviado")
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado")

    logger.info(f"Upload iniciado: {file.filename}")
    try:
        df = process_file(file.file)
        # Armazena em memória para outros endpoints
        app.state.data = df
        logger.info(f"Upload concluído: {len(df)} linhas processadas")
        return {"status": "sucesso", "linhas_processadas": len(df)}
    except ValueError as e:
        logger.error(f"Erro de validação: {str(e)}")
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error(f"Erro interno: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

# -------------------------
# Endpoint de teste
# -------------------------
@app.get("/")
async def root():
    return {"message": "API de Análise de Vendas ativa!"}

