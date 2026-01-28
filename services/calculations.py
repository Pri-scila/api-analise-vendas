import pandas as pd

# -------------------------
# Cálculos de Vendas
# -------------------------
def calcular_vendas(df: pd.DataFrame) -> dict:
    total_vendas = float(df['valor_final'].sum())
    numero_transacoes = int(len(df))
    media_por_transacao = float(total_vendas / numero_transacoes) if numero_transacoes > 0 else 0

    return {
        "total_vendas": total_vendas,
        "numero_transacoes": numero_transacoes,
        "media_por_transacao": media_por_transacao
    }

# -------------------------
# Cálculos Financeiros
# -------------------------
def calcular_financeiro(df: pd.DataFrame) -> dict:
    df['custo_total'] = df['subtotal'] * (1 - df['margem_lucro'] / 100)
    receita_liquida = float(df['valor_final'].sum())
    custo_total = float(df['custo_total'].sum())
    lucro_bruto = float(receita_liquida - custo_total)

    return {
        "receita_liquida": receita_liquida,
        "custo_total": custo_total,
        "lucro_bruto": lucro_bruto
    }
