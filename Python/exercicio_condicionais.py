# 01 exercicio

numero = int(input("Digite um número:"))

if numero == 0: 
      print("ZERO") 

elif numero % 2 != 0:
    print("Numero impar")       
              
else:
    print("Numero Par")     

# 02 exercicio

numero = int(input("digite um numero:"))

if numero == 0:
     print("Zero")

elif numero > 0:
     print("positivo")

else:
     print("Negativo")


if numero != 0:      
    if numero % 2 != 0:
         print("Numero impar") 

else:
    print("Numero Par")   

# 03 exercicio

numero_1 = int(input("digite o primeiro número:"))

numero_2 = int(input("digite o segundo número:"))

if numero_1 == numero_2:
     print("Igual")

elif numero_1 > numero_2:
     print("maior")

else:
     print("Menor")


# 04 exercicio 

numero_1 = int(input("Digite o primeiro número:"))
numero_2 = int(input("Digite o segundo número:"))
numero_3 = int(input("Digite o terceiro número:"))


if numero_1 == numero_2 and numero_2 == numero_3:         #primeiro uso da ferramenta "and"
         print("todos iguais")

elif numero_1 > numero_2 and numero_1 > numero_3:
     print("Maior:", numero_1)

elif numero_2 > numero_1 and numero_2 > numero_3: 
     print("Maior:", numero_2)

else:
     print("Maior", numero_3)

# 05 exercicio                                               # ----------->EM ANALISE<----------
num1 = int(input("Digite o primeiro número: "))
operacao = input("Digite a operação:")
num2 = int(input("Digite o segundo número: "))


if operacao == 1:
    print(f"Resultado: {num1 + num2}")    

elif operacao == 2:
    print(f"Resultado: {num1 - num2}")                  

elif operacao == 3:
    print(f"Resultado: {num1 * num2}")                          

elif operacao == 4:
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(f"Resultado: {num1 / num2}")

else:
    print("Opção inválida")


# 06 exercicios
                                                               # Em analise...   
faturamento = float(input("Digite o Faturamento:"))
custo = float(input("Digite o valor do custo:"))

lucro = faturamento - custo 
                                                   #se o faturamento foi maior que o custo então terá lucro.                                                  
if faturamento > custo:                            
    print(f"Teve lucro de R$ {lucro}")
elif faturamento < custo:                          # se o faturamento for menor que o custo então terá prejuizo.
    print(f"Teve prejuízo de R$ {abs(lucro)}")
else:
    print("Não teve lucro nem prejuízo")

# 07 exercicios
#primeiro criei a variável "idade" nela amarzenei int(input("Digite a sua idade:")) depois fui para decisões, se a "idade" 
# for maior ou igual a 60, então é "idoso" primeiro tratei a maior idade, agora vamos para a "Adulto" se "idade" for maior ou igual a 18, então será "Adulto"
#e o else? será o criança, por quê? porque se não for ">" será "<" então se não for maior que essas duas decisões então claramente seria menos.

idade = int(input("Digite a sua idade:"))                                                      
if idade < 0:
     print("Idade inválida.")           
elif idade >= 60:
     print("Idoso")             
elif idade >= 18:
     print("Adulto")
elif idade >= 12:
     print("Adolescente")
else: 
     print("Criança")

# 07 exercicio
nota = int(input("Digite a nota:"))

if nota >= 7:
     print("aprovado")
     print("Parabéns pelo esforço!")
elif 5 <= nota < 7:
     print("Recuperação")
     print("você consegue!")
else:
     print("Reprovado")
     print("Se esforce mais!")








