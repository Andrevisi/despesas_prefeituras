import os
import caminho
from municipios import lista_municipios

def Tratamentos():
    for municipio in lista_municipios:
        if os.path.exists(caminho.alterado + municipio) == False:
            os.mkdir(caminho.alterado + municipio)
        for _, _, arquivos in os.walk('./arquivos/original/' + municipio):
            for arquivo in arquivos:
                text = open((caminho.original  + municipio + '/' + arquivo), "r", encoding='iso-8859-1')
                text = ''.join([i for i in text]) \
                    .replace(",", ".")
                text = ''.join([i for i in text]) \
                    .replace("/", "-")
                x = open((caminho.alterado + municipio + '/' + arquivo),"w")
                x.writelines(text)
                x.close()

if __name__ == '__main__':
    Tratamentos()