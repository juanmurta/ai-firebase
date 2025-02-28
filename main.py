import requests
import json
import pprint

link = 'https://python-772f4-default-rtdb.firebaseio.com/'


# criar uma venda (POST)
dados = {'cliente': 'Ariany', 'preco': 150, 'produto': 'teclado'}
requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# criar um novo produto (POST)
dados = {'nome': 'teclado', 'preco': 150, 'quantidade': 80}
requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)


# Editar a venda (PATCH)
dados = {'cliente': 'Hiago'}
requisicao = requests.patch(f'{link}/Vendas/-O4M2YmXA_Wd3vzaN-1S/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)


# pegar uma venda especifica ou todas as vendas (GET)
requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
pprint.pprint(dic_requisicao)
id_hiago = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == 'Hiago':
        print(id_venda)
        id_hiago = id_venda


# deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{id_hiago}/.json')
print(requisicao)
print(requisicao.text)