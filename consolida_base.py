import pandas as pd
import os
import caminho
from municipios import lista_municipios

def Consolida_base():
    tabela_despesas = []
    tabela_receitas = []
    for municipio in lista_municipios:
        for _, _, arquivos in os.walk('./arquivos/alterado/' + municipio):
            for arquivo in arquivos:
                if arquivo[0:8] == 'despesas':
                    tabela_despesas.append(pd.read_csv((caminho.alterado + municipio + '/' + arquivo), sep=';', header=[0], encoding="utf-8"))

        #         elif arquivo[0:8] == 'receitas':
        #             ##print(arquivo)
        #             #tabela_receitas.append(pd.read_csv((caminho.alterado + municipio + '/' + arquivo), sep=';', header=[0], encoding="utf-8"))     

        csv_despesa = pd.concat(tabela_despesas, axis=0).reset_index(drop = True)
        # csv_receita = pd.concat(tabela_receitas, axis=0).reset_index(drop = True)

    csv_despesa.to_csv('despesas.csv', index=False)
        # csv_receita.to_csv('receitas.csv', index=False)


if __name__ == "__main__":
    Consolida_base()