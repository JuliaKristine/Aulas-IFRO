# a)Desenvolva um algoritmo usando o interpretador Python onde o operador digite “quantos anos um carro foi fabricado”, após, crie uma estrutura condicional que verifique se o carro tem mais que dois anos, se a afirmativa for verdadeira mostre a mensagem “seu carro está ficando antigo”.
"""ano = int(input("Quantos anos um carro foi fabricado?"))
if ano < 2024:
  print("Seu carro está ficando antigo")
"""

# b)Desenvolva um algoritmo usando o interpretador Python onde o operador digita a velocidade máxima que um carro pode alcançar. Crie uma estrutura condicional que verifique se a velocidade ultrapassa a 80 km, se a afirmativa for verdadeira mostre a mensagem “Se dirigir na velocidade informada você será multado”.
"""kmax = int(input("Qual a velocidade maxima do seu carro? "))
if  kmax > 80:
  print(f"Se dirigir na velocidade de {kmax} você será multado")
"""

# c)Desenvolva um algoritmo usando o interpretador Python onde o operador digita o “valor do rendimento médio anual de uma pessoa”. Crie uma estrutura condicional que verifique se o valor digitado é menor ou igual a R$19038, se a afirmativa for verdadeira mostre a mensagem “Sua alíquota de imposto para o ano de 2023 será 0%”.
# Solicita ao operador que digite o valor do rendimento médio anual
"""salario = float(input("Digite o valor do rendimento médio anual: "))
if salario <= 19038:
    print("Sua alíquota de imposto para o ano de 2023 será 0%")
"""

# d)Desenvolva um algoritmo usando o interpretador Python onde o operador digita “dois valores decimais”. Crie uma estrutura condicional que mostre na tela qual o maior valor entre os dois digitados.
"""v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
if v1 > v2:
    print(f"O maior valor é:", v1)
elif v2 > v1:
    print(f"O maior valor é:", v2)
else:
    print("Os dois valores são iguais.")
"""

# e)Desenvolva um algoritmo usando o interpretador Python onde o operador digita “o valor do salário”, e após acrescente 45%. Crie uma estrutura condicional que verifique se o valor digitado acrescido do percentual fixado ficou abaixo de R$ 2.000,00, se a afirmativa for verdadeira, envie a mensagem “você terá aumento dessa vez...”
"""salario = float(input("Digite o valor do salário: "))
maissalario = salario * 1.45
if maissalario < 2000:
    print("Você terá aumento dessa vez...")
else:
    print("Seu salário não terá aumento desta vez.")
"""

# f)Desenvolva um algoritmo usando o interpretador Python onde o operador digita “quantos anos o carro foi fabricado”. Crie uma estrutura de condicional (if e else) que verifique: se o valor digitado é menor ou igual a dois anos, mostre a mensagem “seu carro ainda está novo”, senão, mostre a mensagem “Seu carro não está velhinho...”
"""anos = int(input("Quantos anos o carro foi fabricado? "))
if anos <= 2:
    print("Seu carro ainda está novo.")
else:
    print("Seu carro não está velhinho...")
"""

# g)Desenvolva um algoritmo usando o interpretador Python onde o operador digita a “velocidade máxima que seu carro pode alcançar” e a velocidade máxima que ele costuma andar. Crie uma estrutura condicional que verifique se a velocidade máxima que ele costuma andar ultrapassa a 80km, se sim mostre a mensagem “Se dirigir na velocidade informada você será multado”, senão mostre a mensagem “Parabéns você é um motorista prudente!!!’
'''vmax = float(input('Digite a velocidade máxima que seu carro pode alcançar (em km/h): '))
vanda = float(input('Digite a velocidade máxima que você costuma andar (em km/h): '))
if vanda > 80:
    print('Se dirigir na velocidade informada você será multado.')
else:
    print('Parabéns você é um motorista prudente!!!')
'''

# h)Desenvolva um algoritmo usando o interpretador Python onde o operador digite o valor do “rendimento médio anual de uma pessoa. Crie uma estrutura condicional que verifique se o valor digitado é menor ou igual R$1.903,98, se sim mostre a mensagem “Sua alíquota de imposto para o de 2024 é 0%, senão mostre a mensagem “Sua alíquota de imposto para o ano de 2024 será de 7,5%.
'''rend = float(input('Digite o valor do rendimento médio anual: '))
if rend <= 1903.98:
    print('Sua alíquota de imposto para o ano de 2024 é 0%.')
else:
    print('Sua alíquota de imposto para o ano de 2024 será de 7,5%.')
'''

# i)Desenvolva um algoritmo usando o interpretador Python onde o operador digita o “valor do salário”, após, o valor de 45% será acrescentado ao salário, se o novo valor não ultrapassar R$ 2.000,00, envie a mensagem ‘Você terá aumento esse ano’, senão envie a mensagem ‘Você não terá aumento esse ano’
'''salario = float(input('Digite o valor do salário: '))
maisalario = salario * 1.45
if maisalario <= 2000:
    print('Você terá aumento esse ano.')
else:
    print('Você não terá aumento esse ano.')
'''

# j)Desenvolva um algoritmo usando o interpretador Python onde o operador digite a distância em Km que um determinado passageiro de um aplicativo deseja percorrer. Calcule o valor da corrida cobrando R$ 0,85 por quilometro de viagem para viagem de até 120 quilometros, e R$ 0,48 para viagens mais longas. Para resolver o problema utilize uma estrutura condicional aplicando ‘if’ e ‘else’
'''distancia = float(input('Digite a distância em km que o passageiro deseja percorrer: '))
if distancia <= 120:
    valor = distancia * 0.85
else:
    valor = distancia * 0.48
print(f'O valor da corrida é R$ {valor:.2f}')
'''

# k)Desenvolva um algoritmo usando o interpretador Python onde o operador digita a “quantidade de internet usada durante um mês”. Crie uma estrutura condicional encadeada seguindo os seguintes critérios de estruturas aninhadas: - Abaixo de 200 gigabytes a empresa cobra R$ 0,10 por gigabytes utilizados; - Entre 201 a 400 gigabytes a empresa cobra R$ 0,18 por gigabytes utilizados; - Acima de 400 a empresa cobra R$ 0,12 por gigabytes utilizados.Apresente na tela o valor que o cliente pagará em reais de acordo com a quantidade de gigabytes digitado pelo operador.
'''quantidade = float(input('Digite a quantidade de gigabytes utilizada durante o mês: '))
if quantidade <= 200:
    valor = quantidade * 0.10
elif quantidade <= 400:
    valor = quantidade * 0.18
else:
    valor = quantidade * 0.12
print(f'O valor a ser pago é R$ {valor:.2f}')
'''

# l) Desenvolva um algoritmo, numa situação em que cinco categorias definem o tipo de cliente e o valor da taxa mensal que ele irá pagar. O algoritmo deve pedir ao operador para “digitar qual categoria um cliente pertence” e a partir dela retornar seu status e a taxa mensal a ser paga conforme a tabela abaixo – use estruturas condicionais aninhadas para resolver o problema: Categoria Status Valor taxa mensal 001 Diamante R$ 0,15; 002 Ouro R$ 8,00; 003 Prata R$ 38,00; 004 Bronze R$ 76,00; 005 Lata R$ 152,00
'''categoria = input('Digite a categoria do cliente (001 a 005): ')
if categoria == '001':
    status = 'Diamante'
    taxa = 0.15
elif categoria == '002':
    status = 'Ouro'
    taxa = 8.00
elif categoria == '003':
    status = 'Prata'
    taxa = 38.00
elif categoria == '004':
    status = 'Bronze'
    taxa = 76.00
elif categoria == '005':
    status = 'Lata'
    taxa = 152.00
else:
    status = 'Categoria inválida'
    taxa = 0.00
if status != 'Categoria inválida':
    print(f'Status: {status}')
    print(f'Taxa Mensal: R$ {taxa:.2f}')
else:
    print('Categoria inválida. Verifique o código digitado.')
'''
# a)Calcule e apresente na tela: resultado = (b + c) * a
'''a = 8
b = 4
c = 3
print((b + c)* a)
'''

#Calcule e apresente na tela: resultado = 3*((4+5) - (25 / 5)) **2
'''a = 2
b = 5
c = 3
d = 4
e = 25
print(f'O resultado da equação: "3*((4+5)-(25/5))**2" é: {c*((d+b)-(e/b))**a}')
'''

#c) Execute os cálculos: divisão de a por b; cociente da divisão de a por b; resto da divisão de a por b - sendo:
'''a = 7
b = 3
print(f'O resultado da divisão de 7 por  3 é: {a//b}')
print(f'O cociente da divisão de 7 por 3 é: {a//b}')
print(f'O resto da divisão de 7 por 3 é: {a%b}')
'''

# d)Calcule e apresente na tela o resultado = (25 ** (1/2)) - (125 ** (1/2)) + 5
'''a = 25
b = 2
c = 125
e = 5
print(f'O resultado do calculo da equação é: {(a ** (1/b)) - (c ** (1/b)) + e}')
'''

# e) Desenvolva um algoritmo, usando o edito IDLE Python para controlar uma registradora. O operador deve digitar o código do produto e a quantidade comprada, conforme a tabela abaixo ou 0 (zero para sair): 
#Código Preço
#1 | 0,50
#2 | 1,00
#3 | 4,00
#4 | 6,00
#5 | 7,00
#6 | 8,00
'''while True:
    codigo = input("Digite o código do produto (1 a 6) ou 0 para sair: ")
    if codigo == "0":
        print("Saindo da registradora...")
        break
    elif codigo == "1":
        preco = 0.50
    elif codigo == "2":
        preco = 1.00
    elif codigo == "3":
        preco = 4.00
    elif codigo == "4":
        preco = 6.00
    elif codigo == "5":
        preco = 7.00
    elif codigo == "6":
        preco = 8.00
    else:
        print("Código de produto inválido. Tente novamente.")
        continue
    quantidade = int(input("Digite a quantidade comprada: "))
    total = preco * quantidade
    print(f"Total da compra: R$ {total:.2f}")
'''