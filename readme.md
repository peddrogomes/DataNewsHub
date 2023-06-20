### Como utilizar o DataNewsHub:

- Crie uma pasta chamada datanewshub
- no terminal execute: 
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

- se tudo deu certo até aqui no terminal estará aparecendo sua env ativada e seu terminal aparecerá assim:
``` console
(scrapy_env) PS C:\datanewshub\:
```
* Nem sempre ativar a env é algo direto, talvez você precise mudar as permissões de execução do powershell para executar o adtivate.ps1

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


Sites de noticia com mais acesso:

G1 (https://g1.globo.com/): O G1 é o portal de notícias da Globo, uma das maiores emissoras de televisão do Brasil.

UOL (https://www.uol.com.br/): O UOL é um portal de notícias que abrange uma variedade de assuntos, incluindo notícias, esportes, entretenimento e tecnologia.

Folha de S.Paulo (https://www.folha.uol.com.br/): A Folha de S.Paulo é um dos principais jornais impressos do Brasil e também possui uma versão online com notícias atualizadas.

Estadão (https://www.estadao.com.br/): O Estadão é outro jornal de grande circulação no Brasil, com uma versão online que cobre uma ampla gama de assuntos.

R7 (https://noticias.r7.com/): O R7 é o portal de notícias da Rede Record, uma das principais redes de televisão do país.

Terra (https://www.terra.com.br/): O Terra é um portal que oferece notícias, esportes, entretenimento e outros conteúdos variados.