import scrapy


class G1GloboSpider(scrapy.Spider):
    name = "g1_globo"
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/"]

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

            #  yield {
            #     'titulo' : noticia.css('.c-main-headline__title ::text').get().replace('\n', '').strip(),
            #     'sub-titulo' : noticia.css('.c-main-headline__standfirst ::text').get().replace('\n', '').strip(),
            #     'link' :  noticia.css('a ::attr(href)').get(),
            #     'img' : noticia.css('.c-main-headline__image ::attr(data-src)').get(),
            #     'img_info' : noticia.css('.c-main-headline__image ::attr(alt)').get(),# .bstn-fd-picture-image
            #     'datetime' : datetime.strftime(datetim,'%d-%m-%Y %H:%M')
            #     }

    
