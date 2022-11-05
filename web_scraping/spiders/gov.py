import scrapy


class GovSpider(scrapy.Spider):
    name = 'gov'
    # allowed_domains = ['www.gov.br']
    start_urls = ['https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude']

    def parse(self, response):
        for link in response.css('.internal-link'):
            
            titulo = link.css('::text').get()
            arquivo = response.urljoin(
                    link.css('::attr(href)').get()
            )
            
            if titulo[:5] == 'Anexo':
                print('>>>>',titulo)
                print('>>>>',arquivo)
                yield{
                    'Title':titulo,
                    'file_urls':[arquivo]
                }