## O que é o DataNewsHub:
O DataNewsHub é um projeto que visa raspar uma serie de sites de notícias brasileiros e disponibilizar dados das ultimas 24hrs.

A ideia por trás disso é utilizar algoritmos para classificar e listar as noticias por grau de relevância, seja por ter similaridade de noticias entre os sites ou algum outro parâmetro.


## Como utilizar o DataNewsHub:

Crie uma pasta chamada datanewshub

- entre na pasta via terminal executando: 
``` console
cd .\datanewshub\
```
- Clone o repositorio executando:
``` console
git clone https://github.com/peddrogomes/DataNewsHub.git
```
 
- Crie uma env chamada scrapy_env: 
``` console
python -m venv scrapy_env
```

- Inicie a env (se for no windows): 
``` console
scrapy_env\Scripts\activate.ps1
```

- Se tudo deu certo até aqui no terminal estará aparecendo sua env ativada e seu terminal aparecerá assim:
``` console
(scrapy_env) PS C:\datanewshub\:
```
* Nem sempre ativar a env é algo direto, talvez você precise mudar as permissões de execução do powershell para executar o activate.ps1

- Após todo esse processo é necessário instalar os requeriments:
``` console
pip install -r requirements.txt
```
- Para testar se deu tudo certo execute os comandos:
``` console
cd .\scrapy_proj\
scrapy list
```
* O retorno previsto será uma lista dos spiders do projeto.

- Para executar os Scripts de raspagem execute:
``` console
scrapy crawl <nome_do_raspador> -s LOG_FILE=log.txt -o <arquivo_de_saida>.json
```

## Sites de notícias que ja possuem raspadores:

- Folha de S.Paulo (https://www.folha.uol.com.br/): A Folha de S.Paulo é um dos principais jornais impressos do Brasil e também possui uma versão online com notícias atualizadas.

## Sites de noticia que estão no radar para serem raspados:

- G1 (https://g1.globo.com/): O G1 é o portal de notícias da Globo, uma das maiores emissoras de televisão do Brasil.

- UOL (https://www.uol.com.br/): O UOL é um portal de notícias que abrange uma variedade de assuntos, incluindo notícias, esportes, entretenimento e tecnologia.

- Estadão (https://www.estadao.com.br/): O Estadão é outro jornal de grande circulação no Brasil, com uma versão online que cobre uma ampla gama de assuntos.

- R7 (https://noticias.r7.com/): O R7 é o portal de notícias da Rede Record, uma das principais redes de televisão do país.

- Terra (https://www.terra.com.br/): O Terra é um portal que oferece notícias, esportes, entretenimento e outros conteúdos variados.