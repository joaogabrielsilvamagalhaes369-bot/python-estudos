produtos = ["notbook", "pc", "celular", "Televisao"]  #Lista de produto

novo_produto = input("Digite o nome do produto:").lower() #Oque o usuário digitar 

if novo_produto in produtos:  # se o usuário digitar oque estiver dentro da lista então entregue "True"
    print("True")
else:                         # Caso ao contrário entregue "false"
    print("False")
    print("Produto inválido")

#Exercicio 

numero = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

novo_numero = int(input("Digite o número:"))

if novo_numero in numero:
    print("Número válido")
else:
    print("Número inválido")

# segundo exercicio
          
nome = ["joao", "maria", "carlos"]  #<<<<< Lista de nomes >>>>>>

novo_nome = input("digite o nome:").lower() #para o usuário digitar
    
#condição com comparação "in"            
if novo_nome in nome:          
    print("Acesso permitido.")  #se o nome que o usuário colocar estiver dentro da lista então ele irá imprimir "Acesso permitido."
else:
    print("Acesso negado.")     # caso seja false então vai mostrar "Acesso negado"

# terceiro exercicio
