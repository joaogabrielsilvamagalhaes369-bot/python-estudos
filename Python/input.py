faturamento = input("preencha com o faturamento (apenas números)")
faturamento = faturamento.replace("R$", "").replace(",",".")
faturamento = float(faturamento)
custo = 600

lucro = custo - faturamento
print(lucro)

vendas_dia1 = float(input("Vendas dia 1:"))
vendas_dia2 = float(input("Vendas dia 2:"))

print(vendas_dia1 + vendas_dia2)




