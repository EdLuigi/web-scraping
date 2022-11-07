from bs4 import BeautifulSoup as bs
import requests
import zipfile

DOMAIN = 'https://www.gov.br/pt-br'
URL = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

# Abrir arquivo zipado
zipAll = zipfile.ZipFile('Anexos.zip', 'w')

# Scrape dos elementos com classe "internal-link"
for link in get_soup(URL).find_all("a", {"class": "internal-link"}):
    titulo = link.text
    arquivo = link.get('href')

    if titulo[:5] == 'Anexo':
        
        # Definir título dos arquivos
        if titulo[titulo.find('.'):] == '.xlsx)':
            titulo = titulo+'.xlsx'
        else:
            titulo = titulo+'.pdf'
        
        # Baixar e salvar arquivos
        with open (titulo, 'wb') as file:
            response = requests.get(arquivo)
            file.write(response.content)
            zipAll.write(titulo)

# Fechar arquivo zipado
zipAll.close()