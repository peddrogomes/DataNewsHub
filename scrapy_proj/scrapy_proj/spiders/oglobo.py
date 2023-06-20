import scrapy


class OgloboSpider(scrapy.Spider):
    name = "oglobo"
    allowed_domains = ["oglobo.globo.com"]
    start_urls = ["https://oglobo.globo.com/ultimas-noticias/"]

    def parse(self, response):

        for noticia in response.css('.feed-post-body'):
            yield {
                'titulo': noticia.css('.feed-post-link ::text').get(),#.strip(),
                'sub-titulo': noticia.css('.feed-post-body-resumo ::text').get(),#.strip(),
                'datetime': noticia.css('.feed-post-datetime ::text').get()#.strip()
            }   

        next_page = response.css('.load-more a ::attr(href)').get()
        if next_page:
            #yield response.follow(next_page,callback=self.parse)
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

#curadoria          
# problema: busca uma quantidade imensa de dados (de semanas atras), preciso fazer uma contagem de paginação (retornar apenas as ultimas 10)