nome = 'Lysandro Luiz'
altura = 1.90
peso = 80
imc = ... 

# IMC = Peso / (Altura x Altura)

imc = (80 / (1.90 * 1.90))
print(imc)

print(nome, altura, peso, imc)
print(nome)
print(altura)
print(peso)
print(imc)

# Lysandro luiz tem 1.90 de altura,
# pesa 80 quilos e seu IMC é
# 22.1606648199446
# f-strings (o qual o f significa formatação)


linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)