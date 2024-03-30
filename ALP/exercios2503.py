# a) Desenvolva um algoritmo em Python 3.x, usando um editor de códigos, que solicita ao usuário a entrada da média de um aluno. Baseado nessa média, o algoritmo deve categorizar o status acadêmico do aluno conforme os seguintes critérios: Se a média for maior ou igual a 60, exiba a mensagem “Aprovado”. Se a média for menor que 60 e maior que 40, exiba a mensagem “Recuperação”. Se a média for menor ou igual a 40 e maior que 20, exiba a mensagem “Exame”. Se a média for menor ou igual a 20, exiba a mensagem “Reprovado”
'''media = float(input('Digite a média do aluno(a): '))
if media >= 60:
    print('\nAprovado!\n')
elif 40 < media < 60:
  print('\nRecuperação!\n')
elif 20 < media <= 40:
  print('\nExame!\n')
else:
  print('\nReprovado!\n')
'''
# b) Desenvolva um algoritmo no mesmo editor de códigos, em que o usuário insira três números inteiros. Utilizando uma estrutura condicional, o algoritmo deve identificar e exibir o maior número entre os três, com a mensagem: 'O maior número entre os digitados é: {numero}'
'''n1 = int(input('Digite o  primeiro número: '))
n2 = int(input('Digite o  segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
  print(f'O maior número entre os digitados é:  {n1}')
elif n2 > n1 and  n2 > n3:
  print(f'O maior número entre  os digitados é:  {n2}')
else:
  print(f'O maior número entre os digitados é:  {n3}')
'''

# c) Desenvolva um algoritmo em Python 3X que solicite ao usuário a entrada de um número inteiro. Utilize uma estrutura condicional para determinar se o número inserido é positivo ou negativo. Caso seja positivo, o programa deve exibir a mensagem "O número é positivo: {numero}". Se for negativo, deve mostrar "O número é negativo: {numero}"
'''n = int(input("Digite um número inteiro: "))
if n > 0:
    print(f"O número é positivo: {n}")
elif n < 0:
    print(f"O número é negativo: {n}")
else:
    print("O número é zero.")
'''

# d) Desenvolva um algoritmo em Python que solicita ao usuário a entrada de uma temperatura em Fahrenheit. O programa deve então converter essa temperatura para graus Celsius, utilizando a fórmula c = 5 * ((f – 32) / 9). Uma vez obtida a temperatura em Celsius, o algoritmo deve exibir mensagens distintas conforme os seguintes critérios: Se a temperatura em Celsius for maior ou igual a 26º, exiba: 'Está muito calor melhor se proteger: {temperatura_celsius}'. Se a temperatura em Celsius estiver entre 18º e 26º, exiba: 'O clima está agradável, que tal fazer um passeio? {temperatura_celsius}'; Se a temperatura em Celsius for menor que 18º, exiba: 'Está ficando frio melhor se agasalhar:{temperatura_celsius}'
'''fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
if celsius >= 26:
    print(f"Está muito calor melhor se proteger: {celsius}°C")
elif 18 <= celsius < 26:
    print(f"O clima está agradável, que tal fazer um passeio? {celsius}°C")
else:
    print(f"Está ficando frio melhor se agasalhar: {celsius}°C")
'''

# e) Desenvolva um algoritimo, usando um editor de c’doigos, em Python para calcular o valor a ser pago pelo fornecimento de energia elétrica. O programa deve solicitar ao usuário a quantidade de energia consumida em kWh e o tipo de instalação, que pode ser 'R' para residências, 'I' para indústrias ou 'C' para comércios. O valor é calculado com base na tabela de preços Abaixo. Se o tipo de instalação informado não esteja listado na tabela, o programa deve exibir a mensagem: 'Tipo de instalação desconhecido'. Assegure-se de seguir as tarifas e faixas de consumo especificadas:
'''preco = 0
if tipo == 'R':
    if consumo <= 700:
        preco = 0.42
    else:
        preco = 0.50
elif tipo == 'C':
    if consumo <= 1400:
        preco = 0.55
    else:
        preco = 0.65
elif tipo == 'I':
    if consumo <= 5100:
      preco = 0.58
    else:
      preco = 0.69
else:
    preco = 0
    print(f'Erro!!!! Tipo de instalação desconhecido...')
if preco > 0:
    custo = consumo * preco
    print(f'O tipo de instalação é: {tipo} e o valor a pagar é de: R${custo:.2f}.')
else:
    print(f'Não foi possivel calcular o custo devido ao tipo de instalação desconhecido.')
'''

# f) Desenvolva um script, em Python 3.x, que seja capaz de apresentar na tela números de 1 a 100 usando a estrutura de repetição while.
'''n = 1
while n <= 100:
  print(n)
  n += 1
'''

# g) Desenvolva um algoritmo, usando o interpretador Python onde a estrutura de repetição mostre a contagem regressiva para o lançamento de um ônibus espacial nave e ordem decrescente.
# Definindo o tempo inicial para a contagem regressiva
'''tempor = 10
print('Contagem regressiva para o lançamento do ônibus espacial:')
while tempor > 0:
    print(tempor)
    tempor -= 1
print("Lançamento do ônibus espacial!")
'''

# h) Num cenário onde temos que imprimir números inteiros entre 1 e um valor digitado pelo operador.
'''numero = int(input('Digite o último numero que será apresentado na tela: '))
n = 1
while n <= numero:
  print(n)
  n += 1
'''

# i) Em um outro cenário onde devemos imprimir apenas os números pares entre 0 (zero) e um número digitado pelo usuário. Vale lembrar que um número é par quando é zero ou múltiplo de dois. Quando é múltiplo de 2, temos o resto da divisão desse número por 2 é 0 (zero). Em Python escrevemos esse teste usando a seguinte sintaxe:
'''n = int(input("Digite um número inteiro: "))
print("Números pares entre 0 e", n, ":")
for i in range(n + 1):
    if i % 2 == 0:
        print(i)
'''

# j) Desenvolva um algoritmo, usando o interpretador Python e estrutura de repetição while onde o operador digita um número inteiro e o algoritmo mostra a tabuada desse número
'''numero = int(input("Digite um número inteiro para ver a sua tabuada: "))
contador = 1
print(f"Tabuada do {numero}:")
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
'''

# k) Desenvolva um algoritmo, usando o interpretador Python e estrutura de repetição while e estrutura condicional onde o operador digita a nota inteira de um aluno e se a nota digitada estiver fora do intervalo 0 a 100 emita a mensagem “Nota inválida” e peça para o operador digitar a nota novamente. Para sair o operador deve digitar -1
'''while True:
    nota = int(input("Digite a nota do aluno (-1 para sair): "))
    if nota == -1:
        print("Saindo do programa.")
        break
    if nota < 0 or nota > 100:
        print("Nota inválida. Digite novamente.")
    else:
        print(f"Nota válida: {nota}")
'''

#1) Explique qual as duas boas razões para quebrar uma regra?
'''R: Quando a adoção de uma regra tornaria o código menos legível, mesmo para alguém acostumado com essas regras, quando se deseja ser consistente com outro código que acompanha aquele em desenvolvimento e que também viola as regras.
'''
# 2) Na parte de Formatação do Código em Python, sintetize os seguintes assuntos...
'''R: Indentação: Use 4 espaços por nível de indentação.
Tabulações ou espaços: Espaços são preferidos ao invés de tabulações.
Comprimento máximo de linhas: Limite todas as linhas a um máximo de 79 caracteres.
Linhas em branco: Separe as funções de nível superior e as definições de classe com duas linhas em branco. Definições de métodos dentro de uma classe são separadas por uma linha em branco.
Import: As importações devem estar em linhas separadas e no topo do arquivo depois de quaisquer comentários ou docstrings.
Espaços em expressões e instruções: Evite espaços extras em situações listadas no PEP 8.
Outras recomendações: Consulte o PEP 8 para outras recomendações.
Comentários: Use comentários de linha que sejam completos, começando com uma letra maiúscula e terminando com um ponto.
Docstrings: Use docstrings para módulos, funções, classes e métodos públicos.
Controle de Versão: Evite arquivos que são específicos do seu projeto ou ambiente.
Nomes e Identificadores: Use nomes que reflitam o significado da variável ou função.
Estilos de nomes: Evite usar nomes que sejam muito diferentes do estilo Python.
Convenções para Nomes: As convenções de nomes do Python são descritas no PEP 8.
Nomes a evitar: Evite usar nomes de variáveis que sejam palavras-chave do Python ou que mascarem funções incorporadas.
Nomes de Módulos: Os nomes de módulos devem ter letras minúsculas e sublinhados para melhorar a legibilidade.
Nomes de Classes: Os nomes de classes devem normalmente usar a convenção CapWords.
Nomes de Exceptions: As classes de exceção devem terminar com “Error”.
Nomes de Funções: Os nomes de funções devem ser minúsculos, com palavras separadas por sublinhados.
Variáveis Globais: Se uma variável é destinada a ser usada como uma variável global, torne isso explícito usando o módulo global.
Nomes de Métodos: Use a função de convenção de nomenclatura, com a exceção de que você deve usar self como o nome do primeiro argumento do método (para instância e métodos de classe).
Herança: Sempre decida se os métodos e atributos da classe serão públicos ou não-publicos. Se duvidar, escolha não-público; é mais fácil tornar algo público mais tarde do que torná-lo não-público.
Atributos privados: Use um sublinhado único para indicar que algo é privado.
Atributos públicos: Os atributos públicos não devem ter sublinhados.
'''