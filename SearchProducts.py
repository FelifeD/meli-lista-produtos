import json
import requests
import pandas as pd

class getSearchProducts:

    def __init__(self):
        self.dados_produtos = [] 
        self.lista_final_ids = [] 
    
    def getSearchIds(self, termos_buscas):
        lista_final_ids = []  
        
        for termo in termos_buscas:
            busca = termo.replace(' ', '%20')
            api_url = "https://api.mercadolibre.com/sites/MLA/search?q=" + busca + "&limit=50#json"
            
            try:
                response = requests.get(api_url)
                dados_busca = response.json()
                busca_ids = [item['id'] for item in dados_busca.get('results', [])]
                for id in busca_ids:
                    lista_final_ids.append(id)

            except Exception as erro:
                print("Erro: ", erro)

        return lista_final_ids

    def getAttribute(self, attributes, id):
        for attribute in attributes:
            if attribute.get('id') == id:
                return attribute.get('value_name')
        return None

    def getProductsDetails(self, IDs_list, attributes):
        for id in IDs_list:
            api_url = "https://api.mercadolibre.com/items/" + id
            dados_detalhes = self.getResults(api_url)  # Você precisa definir getResults
           # print(dados_detalhes)
           
            produto = {'id': dados_detalhes.get('id'),
                      'title': dados_detalhes.get('title'),
                      'price': dados_detalhes.get('price'),
                      'available_quantity': dados_detalhes.get('available_quantity'),
                      'sold_quantity': dados_detalhes.get('sold_quantity'),
                      'condition': dados_detalhes.get('condition')
                      }

            # Adiciona as informações padrão como parte dos atributos
            for attr in attributes:
                valor = self.getAttribute(dados_detalhes.get('attributes', []), attr)
                produto[attr] = valor  # Adiciona o valor ao dicionário com o nome do atributo

            self.dados_produtos.append(produto)

        return self.dados_produtos

    def getResults(self, api_url):
        # Implementar a função para buscar os dados do API
        try:
            response = requests.get(api_url)
            return response.json()
        except Exception as erro:
            print("Erro ao buscar dados:", erro)
            return None
        
    def sendResultsCSV(self, filename):
        
        df = pd.DataFrame(self.dados_produtos)
        df.to_csv(filename, index=False)
        print(f"Resultados exportados para {filename}")
       
