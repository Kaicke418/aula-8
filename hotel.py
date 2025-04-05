cliente1 = input('digite seu nome>>')
idade1 = int(input('digite sua idade>>'))
cliente2 = input('digite seu nome>>')
idade2 = int(input('digite sua idade>>'))
cliente3 = input('digite seu nome>>')
idade3 = int(input('digite sua idade>>'))

print(f'bem vindos {cliente1}, {cliente2}, {cliente3}')

quartos = {'simples': 15.00,
            'duplo':40.00, 
            'luxuoso': 100.00}
print('qual quarto vai escolher?\n  simples R$15.00 || duplo R$40.00 || luxuoso R$100.00 ')
escolha1 = input(f'oque o cliente {cliente1} escolheu?>>')
escolha2 = input(f'oque o cliente {cliente2} escolheu?>>')
escolha3 = input(f'oque o cliente {cliente3} escolheu?>>')

if escolha1 == 1:
    print(f'o cliente {cliente1} escolheu o quarto simples')
elif escolha1 == 2:
    print(f'o cliente {cliente1} escolheu o quarto duplo')
elif escolha1 == 3:
    print(f'o cliente {cliente1} escolheu o quarto luxuoso')

if escolha2 == 1:
    print(f'o cliente {cliente2} escolheu o quarto simples')
elif escolha2 == 2:
    print(f'o cliente {cliente2} escolheu o quarto duplo')
elif escolha2 == 3:
    print(f'o cliente {cliente2} escolheu o quarto luxuoso')

if escolha3 == 1:
    print(f'o cliente {cliente3} escolheu o quarto simples')
elif escolha3 == 2:
    print(f'o cliente {cliente3} escolheu o quarto duplo')
elif escolha3 == 3:
    print(f'o cliente {cliente3} escolheu o quarto luxuoso ')

dias_cliente1 = int(input(f'quantos dias você terá de estádia? (R$10/dia){cliente1}>>'))
dias_cliente2 = int(input(f'quantos dias você terá de estádia? (R$10/dia){cliente2}>>'))
dias_cliente3 = int(input(f'quantos dias você terá de estádia? (R$10/dia){cliente3}>>'))

valor_cliente1 = quartos[escolha1] * (dias_cliente1 * 10)
print(f'o cliente {cliente1} irá pagar R${valor_cliente1}')
valor_cliente2 = quartos[escolha2] * (dias_cliente2 * 10)
print(f'o cliente {cliente2} irá pagar R${valor_cliente2}')
valor_cliente3 = quartos[escolha3] * (dias_cliente3 * 10)
print(f'o cliente {cliente3} irá pagar R${valor_cliente3}')

# - ***Desafio 1:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*

# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente.*

# *Regras Adicionais:
# Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*

# ***O sistema não deve usar loops (for, while) nem funções.**
# O código deve considerar todos os casos possíveis de escolha dos clientes.*