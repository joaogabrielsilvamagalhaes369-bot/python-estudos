vendas = [10, 20, 30, 40, 50, 60, 80, 90, 100]

          #0   #1  #2  #3  #4  #5  #6  #7  #8
             #posição dos itens da lista.

qtde_vendas = len(vendas)                                 # tamanho do item
soma_vendas = sum(vendas)                                     # soma de todos os itens
maior_venda = max(vendas)                                   # maximo de vendas
menor_venda = min(vendas)                                 # minimo de vendas
media_venda = soma_vendas / qtde_vendas              #divisão entre a soma de todos os itens e o tamanho do item.

print(f"Posição:{vendas [6]}")
print(f"Quantidade:{qtde_vendas}")                # tamanho do item
print(f"Maior venda:{maior_venda}")             # valor máximo do item
print(f"Menor venda:{menor_venda}")              #valor minimo do item
print(f"Media:{media_venda:.2f}")                    # média  do item
print(f"Soma:{soma_vendas}")                     #soma do item

#encontrar um elemento

lista_produto = ["celular", "tablet", "xbox", "pc_game"]

print("celular" in lista_produto)    # "in" serve para ver ser o elemento está ou não está na lista.

# achar o posição do item

posicao = lista_produto.index("celular")

print(posicao)

#editar um item
               #0      #1     #2    #3
lista_preco = [1000,  3000,  4000,  5000]
novo_preco = lista_preco[0]  * 1.1
                #1000
print(novo_preco)

#Remover um item da lista
#lista_produto.remove("celular")

lista_produto.pop(0)

print(lista_produto)








