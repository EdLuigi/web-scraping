# web-scraping-gov.br

![](https://img.shields.io/badge/Python-blue)

Projeto de web scraping com Python para raspagem de arquivos específicos do site https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude

O script baixa os arquivos em .pdf e .xlsx disponíveis na página e cria um arquivo compactado .zip com eles dentro.

## Como executar
```sh
cd web-scraping/
python3 web-scraping.py
```

## Bibliotecas necessárias
- BeautifulSoup
