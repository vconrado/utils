import requests
import re

#Definindo para baixar tudo que for SC.zip
padrao = re.compile("href=\"([\w]*36_SC.zip)")

#Página onde estão os arquivos para baixar
url="http://www.dsr.inpe.br/topodata/data/geotiff/"
#Pasta que serão salvos os arquivos
dest="./dest"

r = requests.get(url)
if r.status_code != 200:
    print("Erro ao obter pagina princial")

texto = r.text
ocorrencias = re.finditer(padrao, texto)
for ocorrencia in ocorrencias:
        nome = texto[ocorrencia.start()+6:ocorrencia.end()]
        #print("\t{}, {}-{} ({})".format(ocorrencia.group(), ocorrencia.start(), ocorrencia.end(), nome))
        url_file = "{}/{}".format(url,nome)
        print("Baixando arquivo {}".format(nome))
        file = requests.get(url_file)
        with open("{}/{}".format(dest,nome), 'wb') as output:
            output.write(file.content)
