a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

print('"Já sei!"')

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'

# referente ao teste -> Não é possível usar o sinal de + com int e str, apenas int/float e str/str.