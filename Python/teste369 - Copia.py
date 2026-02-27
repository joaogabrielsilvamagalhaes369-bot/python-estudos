faturamento = 1000
custo = 600

lucro = faturamento - custo

texto = f"O lucro foi de {lucro} e o faturamento foi de {faturamento}"

print(texto)


email = " JOAOTESTE@gmail.com "

email = email.strip()         # ajustar espaços vazios
email = email.lower()         # Colocar em letra minusculas
print(email)

# tamanho
print(len(email))

# posicao

posicao = email.find("J")
print(posicao)

# pedaços do texto
servidor = email[posicao:]

print(servidor)

