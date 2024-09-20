# meli-lista-produtos

## Resumo do conteúdo
Arquivo com a classe e funções python para puxar os dados de produtos da API do mercadolivre (SearchProducts.py)
Arquivo Jupiter Notebook que utiliza as funções acima e exemplifica uma análise exploratória dos dados <br />


## Documentação das funções SearchProducts.py 


### - função getSearchIds(self, termos_buscas):
  Essa função retorna os IDs da lista de termos a se buscar na API <br />
  <br />
  **parâmetros**: <br />
    termos_buscas: list <br />
  <br />
  **exemplo**: getSearchIds(["Google Home", "Apple TV", "Amazon fire", "Chromecast"]) <br />
 **retorna**:<br />
    objeto list com os IDs de produtos da busca<br />
<br />
<br />
### - função getProductsDetails(self, IDs_list, attributes):
  Essa função  usa uma lista de IDs para buscar detalhes desses IDs na API. <br />
  Adicionalmente ela pode buscar valores dentro do objeto "attributes" que é retornado normalmente<br />
  <br />
  **parâmetros**:  <br />
     IDs_list: list  <br />
     attributes: list (opcional)  <br />
  <br />
  **exemplo**: getProductsDetails(self, ['MLA915561586', 'MLA1141052441'], ["BRAND", "RAM_MEMORY", "STORAGE_CAPACITY"]) <br />
  **retorna**: <br />
    objeto list com dicionários de cada produto dentro <br />

<br />
<br />
    
### - função sendResultsCSV(self, filename):
  Essa função envia os dados gerados para um arquivo CSV <br />
  <br /> 
  **parâmetros**: <br />
     filename: str  <br />
     
  
  **exemplo**: sendResultsCSV(self, 'produtos.csv') <br />
  **retorna**: <br />
    grava um arquivo CSV no storage local <br />
<br />
<br />

## Diagrama de alto nível do funcionamento das funções da API

LInk [https://miro.com/app/board/uXjVLcof1UQ=/](https://miro.com/app/board/uXjVLcof1UQ=/?share_link_id=781556096560)
![meli_retrieve_products_diagrama](https://github.com/user-attachments/assets/9174bb95-36f0-4a90-b525-54e2d5276f2c)



