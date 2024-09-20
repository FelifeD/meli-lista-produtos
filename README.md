# meli-lista-produtos

## Resumo do conteúdo
Arquivo com a classe e funções python para puxar os dados de produtos da API do mercadolivre (SearchProducts.py)
Arquivo Jupiter Notebook que utiliza as funções acima e exemplifica uma análise exploratória dos dados
## Documentação das funções SearchProducts.py
### função getSearchIds(self, termos_buscas):
  Essa função retorna os IDs da lista de termos a se buscar na API
  **parâmetros**:
    termos_buscas: list
  
  **exemplo**: getSearchIds(["Google Home", "Apple TV", "Amazon fire", "Chromecast"])
 **retorna**:
    objeto list com os IDs de produtos da busca
### função getProductsDetails(self, IDs_list, attributes):
  Essa função  usa uma lista de IDs para buscar detalhes desses IDs na API. 
  Adicionalmente ela pode buscar valores dentro do objeto "attributes" que é retornado normalmente
  
  **parâmetros**:
     IDs_list: list
     attributes: list (opcional)
  
  **exemplo**: getProductsDetails(self, ['MLA915561586', 'MLA1141052441'], ["BRAND", "RAM_MEMORY", "STORAGE_CAPACITY"])
  **retorna**:
    objeto list com dicionários de cada produto dentro
### função sendResultsCSV(self, filename):
  Essa função envia os dados gerados para um arquivo CSV
  
  **parâmetros**:
     filename: str
     
  
  **exemplo**: sendResultsCSV(self, 'produtos.csv')
  **retorna**:
    grava um arquivo CSV no storage local
    
