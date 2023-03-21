import pandas as pd

in_csv = 'loocker_despesa.csv'

numero_linhas = sum(1 for linha in (open(in_csv)))

tamanho_arquivo = 700000

for i in range(0,numero_linhas, tamanho_arquivo):
    tabela = pd.read_csv(in_csv, header=None, nrows=tamanho_arquivo, skiprows= i)

    out_csv = 'input' + str(i) + '.csv'

    tabela.to_csv(out_csv, index=False, header=False, mode='a', chunksize=tamanho_arquivo)