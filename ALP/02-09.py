'''
#Importanto a coleção counter
from collections import Counter
'''
'''# Aplicando o Counter sobre um iterável do tipo lista com strings
from collections import Counter
lista = ['Márcia', 'Márcia', 'Alice', 'Alice', 'Antonio', 'Antonio', 'Pedro', 'Pedro']
print(f'\nResultado: {Counter(lista)}')
print(f'\nO tipo do resultado é: {type(Counter(lista))}\n')
'''
'''
# Aplicando o Counter sobre um iterável do tipo lista com números
from collections import Counter
lista = [1, 1, 1, 2, 2, 2, 3, 3,4, 4, 4, 5, 3, 45, 45, 66, 42, 36, 105.19, 105.19]
print(f'\nResultado: {Counter(lista)}')
print(f'\nO tipo do resultado é: {type(Counter(lista))}\n')
'''
'''
# Aplicando Counter sobre uma string
from collections import Counter
frase = ('IFRO Campus Ariquemes')
print(f'\nResultado: {Counter(frase)}')
print(f'\nO tipo do resultado é: {type(Counter(frase))} \n')
'''
'''
# tentando acessar chaves de um DefaultDict
dicionario = {'disciplina': 'Algoritmos e lógica de programação'}
print(f'\nDicionário original: {dicionario}')
print(f'\nAcessando a chave disciplina do dicionário: {dicionario["disciplina"]}')
print(f'\nAcessando a chave curso do dicionário: {dicionario["curso"]}')
'''
'''
# Criando um dicionário utilizando o modulo collections defaultdict e lambda
from collections import defaultdict
dicionario = defaultdict(lambda: 'None')
print(f'\nO valor do dicionário é: {dicionario}')
dicionario['disciplina'] = 'Algoritmos e lógica de programação'
print(f'\no dicionário agora possui o elemento: {dicionario}')
print(f'\nAcessando a chave disciplina do dicionário: {dicionario["disciplina"]}')
print(f'\nAcessando a chave curso do dicionário: {dicionario["curso"]}\n')
'''
'''
# Igualdade de dicionários comuns
nome_1 = {'Gustavo' : 28, 'André': 33, 'João': 15, 'Alice': 9, 'Laís':5}
nome_2 = {'André': 33, 'João': 15, 'Gustavo' : 28, 'Laís': 5, 'Alice': 9,}
print(f'\nos dicionários nome_1 e nome_2 são iguais? {nome_1 == nome_2} \n')
'''
'''
# Dicionários OrderedDict
from collections import OrderedDict
nome_1 = OrderedDict({'Gustavo' : 28, 'André': 33, 'João': 15, 'Alice': 9, 'Laís': 5})
print(f'\no dicionário nome_1 possui os elementos: {nome_1}')
print(f'\nO tipo dos dados do dicionário nome_1 é: {type(nome_1)}')
nome_2 = OrderedDict({'André' : 33, 'João': 15, 'Gustavo' : 28, 'Laís' : 5, 'Alice': 9, })
print('\no dicionário nome_2 possui os elementos: {nome_2}')
print(f'\nO tipo dos dados do dicionário nome_2 é: {type(nome_2)}\n')
print(f'\nos dicionários nome_1 e nome_2 são iguais e estão na mesma ordem? {nome_1 == nome_2}')
'''
'''
# OrderedDict - metodo move_to_end():
from collections import OrderedDict
nome = OrderedDict({'Gustavo' : 28, 'André': 33, 'João': 15, 'Alice': 9, 'Laís': 5})
print(f'\no dicionário original é: {nome}')
nome.move_to_end('André')
print(f'\no dicionário foi modificado: {nome} \n')
'''
'''
# OrderedDict - move_to_end( chave, last = False)
from collections import OrderedDict
nome = OrderedDict({'Gustavo' : 28, 'André': 33, 'João': 15, 'Alice': 9, 'Laís': 5})
print(f'\no dicionário original é: {nome}')
nome.move_to_end('Laís', last = False)
print(f'\no dicionário foi modificado: {nome}\n')
'''
'''
# Tuplas namedtuple - forma_1 de definir:
from collections import namedtuple
animal =  namedtuple('Animal', 'tipo nome raca idade')
'''
'''
# Tuplas namedtuple - Forma_2 de definir:
from  collections import namedtuple
animal =  namedtuple('Animal', 'tipo, nome, raca, idade')
'''
'''
# Tuplas namedtuple - Forma_3 de definir:
from collections  import namedtuple
animal =  namedtuple('Animal', ['tipo nome raca idade'])
'''
'''
# Populando a nametuple animal
from  collections import namedtuple
animal =  namedtuple('Animal', ['tipo', 'nome', 'raca', 'idade'])
cachorros = animal(tipo = 'cachorro', nome='Hatiro', raca='hasa apso?', idade=2)
gatos = animal(tipo = 'gatos', nome='Ravena', raca='Vira latas', idade=1)
print(f'\nCachorro cadastrado: {cachorros}')
print(f'\nOs dados do cachorro foram armazenanos no formato: {type(cachorros)} \n')
print(f'\nGato cadastrado: {gatos}')
print(f'\nOs dados do gato foram armazenanos no formato: {type(gatos)}\n')
'''
'''
# Acessando dados dos animais
from  collections import namedtuple
animal =  namedtuple('Animal', ['tipo', 'nome', 'raca', 'idade'])
cachorros = animal(tipo = 'cachorro', nome='Hatiro', raca='hasa apso?', idade=2)
gatos = animal(tipo = 'gatos', nome='Ravena', raca='Vira latas', idade=1)
print(f'\nTipo: {cachorros[0]}')
print(f'Nome: {cachorros [1]}')
print(f'Raça: {cachorros[2]}')
print(f'ldade: {cachorros[3]} \n')

print(f'Tipo: {gatos[0]}')
print(f'Nome: {gatos[1]}')
print(f'Raça: {gatos[2]}')
print(f'ldade: {gatos[3]} \n')
'''
'''
# Acessando dados dos animais - outra forma
from  collections import namedtuple
animal =  namedtuple('Animal', ['tipo', 'nome', 'raca', 'idade'])
cachorros = animal(tipo = 'cachorro', nome='Hatiro', raca='hasa apso?', idade=2)
gatos = animal(tipo = 'gatos', nome='Ravena', raca='Vira latas', idade=1)
print(f'\nTipo: {cachorros.tipo}')
print(f'Nome: {cachorros.nome}')
print(f'Raça: {cachorros.raca}')
print(f'ldade: {cachorros.idade} \n')
print(f'Tipo: {gatos.tipo}')
print('Nome: (gatos.nome}')
print(f'Raça: {gatos.raca}')
print(f'ldade: {gatos.idade} \n')
'''
'''
# Criando um deque vazio e depois populando-o:
from collections import deque
deq = deque()
deq.append('Ariquemes')
deq.append('Curso de ADS')
deq.appendleft('Campus')
deq.appendleft('IFRO')
print(f'\nOs dados armazenados no deque são: {deq}')
print(f'\nOs dados do deque foram armazenanos no formato: {type(deq)}\n')
'''
'''
# Removendo um elmento no final do deque
from collections import deque
deq = deque()
deq.append('Ariquemes')
deq.append('Curso de ADS')
deq.appendleft('Campus')
deq.appendleft('IFRO')
print(f'\nOs dados armazenados no deque são: {deq}')
print(deq.pop())
print(f'\nOs dados armazenados no deque após o pop() são: {deq}')
'''
'''
# Removendo um elmento no inicio do deque
from collections import deque
deq = deque()
deq.append('Ariquemes')
deq.append('Curso de ADS')
deq.appendleft('Campus')
deq.appendleft('IFRO')
print(f'\nOs dados armazenados no deque são: {deq}')
print(deq.popleft())
print(f'\nOs dados armazenados no deque após o popleft() são: {deq}')
'''
# CRUD (Create, Reader, Update, Delete) - Python / Tkinter e arquivo JSON (JavaScript Object Notation)
import os
import json
import regex as re
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

#Funções modo interative
def valida_campo (campo, tipo_campo):
    if not campo:
        messagebox.showarning('Aviso', f'{tipo_campo} inválido.')
        return False
    if len(campo) > 50:
        messagebox.showarning('Aviso', f'(tipo_campo) muito longo. Deve ter no máximo 50 caracteres.')
        return False
    pattern = r'^[\p{L}\s]{1,50}$'
    if not re.match(pattern, campo):
        messagebox.showwarningl('Aviso', f'{tipo_campo} inválido. Não use números ou caracteres especiais.')
        return False
    preposicoes = ['da', 'de', 'do', 'das', 'dos']
    campo = ''.join([parte.capitalize() if parte not in preposicoes else parte for parte in re.sub(r'\s+',' ',  campo).split()])
    return campo