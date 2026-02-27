# EXERCÍCIO 02

# peça ao usuário o faturamento
faturamento = input("Faturamento (apenas números): ")
print(faturamento)

# peça ao usuário o custo
custo = input("custo (apenas o custo) : ")
print(custo)

#converta valores para float
faturamento = float(faturamento)
print (f"R${faturamento:.3f}")

custo = float(custo)
print (f"R${custo:.3f}")

#calcule o lucro (faturamento - custo)
lucro = faturamento - custo

print(f"O lucro foi de R${lucro:.3f}")














