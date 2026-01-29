nome = "Thales Willian"
altura = 1.8
peso = 95
imc = peso/altura ** 2

# F string serve para usar variavel dentro de uma cadeia de texto

linha_1 = f"{nome}\n{altura:.2f} altura\n{peso} kg\n{imc:.2f} imc "
print(linha_1)

print("{}, {}, {}".format(nome2 = nome, altura1 =altura,peso1 = peso))

