# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = float(input('digite um número>>'))

if numero == 0:
    print("você digitou zero.")
elif numero < 0:
    print('numero é negativo')
elif numero > 0:
    print('numero é positivo')

print(numero)
# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input('digite sua idade>>'))
if idade == 18:
    print("teu voto é obrigatório")
elif idade >= 16 and idade <= 17:
    print("teu voto éopcional")
else: 
    print("voê não vota")
# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
number = 33
if number % 2 == 0:
    print('é par')
else:
    print('é impar')
# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
print('lembre-se que as somas tem que ser igual a 180')
lado1 = float(input('digite um número para o triângulo retângulo'))
lado2 = float(input('digite um outro para o triângulo retângulo'))
ponta = float(input('digite um número para a ponta do triângulo retângulo'))

if lado1 + lado2 > ponta and lado1 + lado2 + ponta == 180:
    print('é um triângulo retângulo')
    if lado1 == lado2 == ponta:
        print('é equilátero')
    elif lado1 == lado2 != ponta or lado1 == ponta != lado2:
        print('é isoceles')
    elif lado1 != lado2 != ponta:
        print('é escaleno')
else:
    print("não é um triângulo")

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.
digito = float(input('digite um número'))
if digito % 5 == 0:
    print('é multiplo de 5')
elif digito % 7 == 0:
    print('é multiplo de 7')
    
# 6*

# Verifique se um número é positivo e maior que 10
if digito > 10:
    print('é maior que 10')
elif digito <= 10:
    print('é menor ou igual a 10')

# 7*

# Verifique se um número é divisível por 3 ou 5.
conta = float(input('digite um número>>'))

if conta % 3 == 0:
    print('é divisivel por 3')
elif conta % 5 == 0:
    print('é divisivel por 5')

    