from selenium import webdriver
import time
from zipfile import ZipFile
import os
from municipios import lista_municipios
import caminho

def Busca_arq():
    url = "https://transparencia.tce.sp.gov.br/sites/default/files/csv/"
    municipios = lista_municipios
    operacoes = ["despesas"]#, "receitas"]
    anos = ['2017', "2018", "2019", "2020", "2021", "2022"]
    ext = ".zip"
    sep = '-'
    # caminho = os.getcwd()
    # caminho_download = caminho + '/arquivos/zip/'
    # caminho_original = caminho + '/arquivos/original/'
    


    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_argument("--headless")
    prefs = {"download.default_directory": caminho.download}
    chromeOptions.add_experimental_option("prefs", prefs)
    navegador = webdriver.Chrome(options=chromeOptions)

    for municipio in municipios:
        if os.path.exists(caminho.original + municipio) == False:
            os.mkdir(caminho.original + municipio)

        for oper in operacoes:
            for ano in anos:
                arquivo = oper + sep + municipio + sep + ano + ext
                link = url + arquivo

                navegador.get(link)
                time.sleep(1)

                z = ZipFile((caminho.download + arquivo), "r")
                z.extractall(caminho.original + municipio)
                z.close()

if __name__ == '__main__':
    Busca_arq()