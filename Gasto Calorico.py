print("========================================")
print("========CALCULAR GASTO CALÓRICO=========")
print("========================================")
print()

sexo = str(input("Você é homem ou Mulher? \n \
     \
     \n [ H ] HOMEM 🧔 \
     \n [ M ] MULHER 👩\
     \n \nEscolha uma opção:  "

                 ))
print("")

idade = int(input("Por favor, me diga sua idade: "))
print()
peso = int(input("Digite seu peso "))
print("")


# Calculo Criança de 0 a 3 anos de idade
gasto_0a3_anos_mulher = 58.317 * peso - 31.1
gasto_0a3_anos_homem = (59.512 * peso) - 30.4

# Calculo criança de 3 a 10 anos de idade
gasto_3a10_anos_mulher = (20.315 * peso) + 485.9
gasto_3a10_anos_homem = (22.706 * peso) + 504.3

# Calculo criança de 10 a 18 anos de idade
gasto_10a18_anos_mulher = (13.384 * peso) + 692.6
gasto_10a18_anos_homem = (17.686 * peso) + 658.2

# Calculo  Adulto de 18 a 30 anos de idade
gasto_18a30_anos_mulher = (14.818 * peso) + 486.6
gasto_18a30_anos_homem = (15.57 * peso) + 692.2

# Calculo Adulto de 30 a 60 anos de idade
gasto_30a60_anos_mulher = (8.126 * peso) + 845.6
gasto_30a60_anos_homem = (8.126 * peso) + 845.6

# Calculo Adulto maior que 60 anos de idade
gasto_maior_que_60_anos_mulher = (9.82 * peso) + 658.5
gasto_maior_que_60_anos_homem = (11.711 * peso) + 587.7

# 0 a 3 anos
if sexo == 'F' or 'f' and idade >= 0 and idade <= 3:
    print(
        f"Gasto Calórico Aproximado: {gasto_0a3_anos_mulher:.0f} Kcal Diárias.")

elif sexo == 'M' or 'm' and idade >= 0 and idade <= 3:
    print(
        f"Gasto Calórico Aproximado: {gasto_0a3_anos_homem:.0f} Kcal Diárias.")

# 3 a 10 anos
elif sexo == 'F' or 'f' and idade > 3 and idade <= 10:
    print(
        f"Gasto Calórico Aproximado: {gasto_3a10_anos_mulher:.0f} Kcal Diárias.")

elif sexo == 'M' or 'm' and idade > 3 and idade <= 10:
    print(
        f"Gasto Calórico Aproximado: {gasto_3a10_anos_homem:.0f} Kcal Diárias.")

# 10 a 10 anos
elif sexo == 'F' or 'f' and idade > 10 and idade <= 18:
    print(
        f"Gasto Calórico Aproximado: {gasto_10a18_anos_mulher:.0f} Kcal Diárias.")

elif sexo == 'M' or 'm' and idade > 10 and idade <= 18:
    print(
        f"Gasto Calórico Aproximado: {gasto_10a18_anos_homem:.0f} Kcal Diárias.")

# 18 a 30 anos
elif sexo == 'F' or 'f' and idade > 18 and idade <= 30:
    print(
        f"Gasto Calórico Aproximado: {gasto_18a30_anos_mulher:.0f} Kcal Diárias.")

elif sexo == 'M' or 'm' and idade > 18 and idade <= 30:
    print(
        f"Gasto Calórico Aproximado: {gasto_18a30_anos_homem:.0f} Kcal Diárias.")

# 30 a 60 anos
elif sexo == 'F' or 'f' and idade > 30 and idade <= 60:
    print(
        f"Gasto calórico estimado: {gasto_30a60_anos_mulher:.0f} Kcal Diárias.")

elif sexo == 'M' or 'm' and idade > 30 and idade <= 60:
    print(
        f"Gasto Calórico Aproximado: {gasto_30a60_anos_homem:.0f} Kcal Diárias.")

# Maior que 60 anos de idade
elif sexo == 'F' or 'f' and idade > 60:
    print(
        f"Gasto Calórico Aproximado: {gasto_maior_que_60_anos_mulher:.0f} Kcal Diárias.")

elif sexo == 'M' or 'm' and idade > 60:
    print(
        f"Gasto calórico Aproximado: {gasto_maior_que_60_anos_homem:.0f} Kcal Diárias.")
