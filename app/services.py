import csv

def ler_vendas():
    vendas = []
    with open("data/vendas.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            linha["quantidade"] = int(linha["quantidade"])
            linha["valor"] = float(linha["valor"])
            vendas.append(linha)
    return vendas

