import scrapy

from datetime import date, datetime

class FolhaSpSpider(scrapy.Spider):
    name = "folha_sp"
    start_urls = ["https://www1.folha.uol.com.br/ultimas-noticias/#10"]
    now = datetime.now()

    def parse(self, response):

        noticia = response.css('.u-list-unstyled')[0]
        if noticia.css('.c-main-headline__title ::text').get() is not None:
            
            str_date = noticia.css('.c-headline__dateline ::text').get().replace('\n', '').strip().lower()
            datetim = datetime.strptime(str_date, "%d.%b.%Y às %Hh%M")
            
            yield {
                'titulo' : noticia.css('.c-main-headline__title ::text').get().replace('\n', '').strip(),
                'sub-titulo' : noticia.css('.c-main-headline__standfirst ::text').get().replace('\n', '').strip(),
                'link' :  noticia.css('a ::attr(href)').get(),
                'img' : noticia.css('.c-main-headline__image ::attr(data-src)').get(),
                'img_info' : noticia.css('.c-main-headline__image ::attr(alt)').get(),# .bstn-fd-picture-image
                'datetime' : datetime.strftime(datetim,'%d-%m-%Y %H:%M')
                }
        
        
        for noticia in response.css('.c-headline--newslist'):#__content a'):

            if noticia.css('.c-headline__title ::text').get() is not None :

                str_date = noticia.css('.c-headline__dateline ::text').get().replace('\n', '').strip().lower()
                datetim = datetime.strptime(str_date, "%d.%b.%Y às %Hh%M")
                
                if datetim.day != self.now.day: 
                    return 0


                yield{
                    'titulo' : noticia.css('.c-headline__title ::text').get().replace('\n', '').strip(),
                    'sub-titulo' : noticia.css('.c-headline__standfirst ::text').get().replace('\n', '').strip(),
                    'link' : noticia.css('a ::attr(href)').get(),
                    'img' : noticia.css('.c-headline__image ::attr(data-src)').get(),
                    'img_info' : noticia.css('.c-headline__image ::attr(alt)').get(),
                    'datetime' : datetime.strftime(datetim,'%d-%m-%Y %H:%M')
                }


#melhorias: incluir link de imagem e link da reportagem !