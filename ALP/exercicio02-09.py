'''
    Leandro Pires utf-8 Pt-br 

    Exercico do dia 01/09/2024 
'''

'''
#Importando a coleção Counter
from collections import Counter
'''
'''
#Aplicando Counter sobre um iterável do tipo lista com strings
lista = ['Márcia','Márcia','Alice','Alice','Antonio','Antonio','Pedro','Pedro']
print(f'\nResultado:{Counter(lista)}')
print(f'\nO tipo do resultado é:{type(Counter(lista))}\n')
'''
'''
#Aplicando Counter sobre um iterável do tipo lista com números
lista = [1,1,1,2,2,2,3,3,4,4,4,5,3,45,45,66,42,36,105.19,105.19]
print(f'\nResultado:{Counter(lista)}')
print(f'\nO tipo do resultado é:{type(Counter(lista))}\n')
'''
'''
#Aplicando Counter sobre uma string

frase = ('IFRO Campus Ariquemes')
print(f'\nResultado:{Counter(frase)}')
print(f'\nO tipo de resultado é:{type(Counter(frase))}\n')
'''
'''
#Tentado acessar chaves de um "DefaultDict":
dicionario = {'disciplina':'Algoritmos e Lógica de programação'}
print(f'\nDicionário original:{dicionario}')
print(f'\nAcessando a chave disciplina do dicionário:{dicionario["disciplina"]}')
print(f'\nAcessando a chave curso do dicionário:{dicionario["curso"]}')
'''

'''
#Importando a coleçao defaultdict
from collections import defaultdict
'''

'''
#Criando um dicionário utilizando o modulo collections defaultdict e lambda

dicionario = defaultdict(lambda:'None')
print(f'\nO valor do dicionário é:{dicionario}')
dicionario['disciplina'] = 'Algoritmos e lógica de programação'
print(f'\nO dicionário agora possui o elemento:{dicionario}')
print(f'\nAcessando a chave de disciplina do dicionário:{dicionario["disciplina"]}')
print(f'\nAcessando a chave de curso do dicionário:{dicionario["curso"]}\n')
'''

#                      OrderedDict

'''
#Igualdade de dicionários comuns:

nome_1={'Gustavo':28,'André':33,'João':15,'Alice':9,'Laís':5}
nome_2={'André':33,'João':15,'Gustavo':28,'Laís':5,'Alice':9,}

print(f'\nOs dicionários nome_1 e nome_2 são iguais? {nome_1 == nome_2} \n')
'''
# Importando a coleção OrderedDict
# Dicionários OrderedDict
'''
from collections  import OrderedDict
'''
'''
nome_1=OrderedDict({'Gustavo':28,'André':33,'João':15,'Alice':9,'Laís':5})

print(f'\nO dicionário nome_1 possui os elementos: {nome_1}')
print(f'\nO tipo de dados do dicionário nome_1 é: {type(nome_1)}')

nome_2=OrderedDict({'André':33,'João':15,'Gustavo':28,'Laís':5,'Alice':9,})

print(f'\nO dicionário nome_2 possui os elementos: {nome_2}')
print(f'\nO tipo de dados do dicionário nome_2 é: {type(nome_2)}\n')
print(f'\nOs dicionários nome_1 e nome_2 são iguais e estão na mesma ordem? {nome_1 == nome_2}')
'''

# OrderedDict - metodo move_to_end():

# Move o nome escolhido para o final do dicionario
'''
nome = OrderedDict({'Gustavo':28,'André':33,'João':15,'Alice':9,'Laís':5})
print(f'\nO nome original é:{nome}')
nome.move_to_end('André')
print(f'\nO dicionário foi modificado:{nome} \n')
'''
#OrderedDict - move_to_end(chave,last = false)

#se for aplicado move_to_end( chave, last = False) o elemento é movido o início do dicionário.
'''
nome = OrderedDict({'Gustavo':28,'André':33,'João':15,'Alice':9,'Laís':5})
print(f'\nO nome original é:{nome}')
nome.move_to_end('Laís', last=False)
print(f'\nO dicionário foi modificado:{nome} \n')
'''

#Importando a coleção namedtuple
'''
from collections import namedtuple
'''
#Tuplas namedtuple - forma_1 de definir:
'''
animal = namedtuple('animal','tipo nome raça idade')
'''
#Tuplas namedtuple - forma_2 de definir:
'''
animal = namedtuple('animal','tipo, nome, raça, idade')
'''
#Tuplas namedtuple - forma_2 de definir:
'''
animal = namedtuple('animal',['tipo', 'nome', 'raça', 'idade'])
'''
#Populando a nametuple animal
'''
cachorros = animal(tipo='cachorro', nome='Hatiro', raça='hasa apso?', idade=2)

gatos = animal(tipo='gatos', nome='Ravena', raça='Vira latas', idade=1)

print(f'\nChachorros cadastrados:{cachorros}')
print(f'\nOs dados do cachorro foram armazenados no formato:{type(cachorros)}\n')

print(f'\nGatos cadastrados:{gatos}')
print(f'\nOs dados do gato foram armazenados no formato:{type(gatos)}\n')
'''
#Acessando os dados dos animais 
'''
print(f'\nTipo:{cachorros[0]}')
print(f'\nNome:{cachorros[1]}')
print(f'\nRaça:{cachorros[2]}')
print(f'\nIdade:{cachorros[3]}\n')

print(f'\nTipo:{gatos[0]}')
print(f'\nNome:{gatos[1]}')
print(f'\nRaça:{gatos[2]}')
print(f'\nIdade:{gatos[3]}\n')
'''
#Acessando os dados dos animais - de outra forma
'''
print(f'\nTipo:{cachorros.tipo}')
print(f'Nome:{cachorros.nome}')
print(f'Raça:{cachorros.raça}')
print(f'Idade:{cachorros.idade}\n')

print(f'Tipo:{gatos.tipo}')
print(f'Nome:{gatos.nome}')
print(f'Raça:{gatos.raça}')
print(f'Idade:{gatos.idade}\n')
'''

#Criando um deque vazio e depois populando-o:
'''
from collections import deque

deq = deque()

deq.append('Ariquemes')

deq.append('Curso de ADS')

deq.appendleft('Campus')

deq.appendleft('IFRO')
'''
#Com o elemento no inici do deque:
'''
print(f'\nOs dados armazenados no deque são:{deq}')

print(f'\nOs dados do deque foram armazenados no formato:{type(deq)}\n')
'''
#Removendo um elemento no final do deque:
'''
print(f'\nOs dados armazenados no deque são:{deq}')

print(deq.pop())

print(f'\nOs dados armazenados no deque após o pop() são:{deq}')
'''
#Removendo um elemento no inicio do deque:
'''
print(f'\nOs dados armazenados no deque são:{deq}')

print(deq.popleft())

print(f'\nOs dados armazenados no deque após o popleft() são:{deq}')
'''
'''
#CRUD (Create, Reader, Update, Delete)- Ptyhon/ Tkinter e arquivo JSON(JavaScript Object Notation)
'''

import os
import json
import regex as re
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

#Funções - modo interativo

def valida_campo(campo, tipo_campo):
    if not campo :
        messagebox.showwarning('Aviso'f'{tipo_campo} invalido.')
        return False
    if len(campo) > 50:
        messagebox.showwarning('Aviso',f'{tipo_campo} muito longo , Deve ter no máximo 50 caracteres.')
        return False
    
    pattern = r'^[\p{L}\s]{1,50}$'
    if not re.match(pattern, campo):
        messagebox.showwarning('Aviso', f'{tipo_campo} Inválido. Não use números ou caracteres especiais.')
        return False
 
    preprosiçoes = ['da' 'de' 'do' 'das' 'dos']
    campo = ' '.join([parte.capitalize() if parte not in  preprosiçoes else parte for parte in re.sub (r'\s+',' ', campo).split()])
    return campo

def grava_dados_arquivo(pessoa):
    arquivo_json = "cadastro.json"
    dados = []
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json,'r') as arquivo:
            dados = json.load(arquivo)

    dados.append(pessoa)
    with open(arquivo_json,'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


def carregar_dados_arquivo():
    arquivo_json = "cadastro.json"
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            return [(linha['nome'], linha['sobrenome'], linha['genero']) for linha in json.load(arquivo)]
        
# Funçoes Tkinter
def configurar_app():
    global mensagem_var

    app.title('Ánalise e Desenvolvimento de Sistemas')
    app.geometry('1024x600')
    app.configure(background='#F8F8FF')
    app.resizable(True,True)
    app.maxsize(width=1024, height=600)

    mensage_var = StringVar()
    mensage_label = Label(app, textvariable=mensage_var, fg='red', font=('Arial', 14, 'bold'), bg='white')
    mensage_label.place(x=100, y=265, width=700, height=20)


def criar_frame():
    frame = LabelFrame(app, text='Cadastro', borderwidth=1, relief='solid')
    frame.place(x=10, y=10, width=1000, height=200)
    return frame

def criar_labels(frame):
    lb_1 = Label(frame, text='Contatos:', fg='red', font=('Arial', 14, 'italic', 'bold'))
    lb_1.place(x=15, y=10, width=70, height=20 )
    lb_nome = Label(frame, text='Digite um nome: ', font=('Arial', 14))
    lb_nome.place(x=20, y=35, width=120, height=20)
    lb_sobrenome = Label(frame, text='Digite um sobrenome: ', font=('Arial', 14))
    lb_sobrenome.place(x=20, y=65, width=180, height=20)

def criar_entry(frame):
    global nome, sobrenome
    nome = Entry(frame, font=('Arial', 14) )
    nome.place(x=200, y=35, width=400, height=20)
    sobrenome = Entry(frame, font=( 'Arial', 14))
    sobrenome.place(x=200, y=65, width=400, height=20)
    return nome, sobrenome

def criar_checkbutton (frame) :
    global genero_var
    genero_var = StringVar()
    generos = ['Masculino', 'Feminino', 'Outros' ]
    y_pos = 95
    for gen in generos:
        Radiobutton(frame, text=gen, variable=genero_var, value=gen, font=('Arial', 14)).place(x=200, y=y_pos)
        y_pos += 30
    return genero_var

def criar_botao():
    global btn_captura
    style = ttk. Style()
    style.configure('Green. TButton', font=( 'Arial', 14, 'bold'), background='#90EE90')
    style.configure( 'Blue. TButton', font=('Arial', 14, 'bold'), background='#ADD8E6')
    style.configure( 'Red. TButton', font=( 'Arial', 14, 'bold'), background='#FFB6C1' )

    btn_captura = ttk.Button(app, text='Inserir dados', style='Green. TButton', command=capturar)
    btn_captura.place(x=20, y=220, width=155, height=40)

    btn_pesquisar = ttk. Button(app, text='Pesquisar dados', style='Blue. TButton', command=mostrar_campo_pesquisa)
    btn_pesquisar.place(x=185, y=220, width=155, height=40)

    btn_atualizar = ttk.Button(app, text='Atualizar dados', style='Green. TButton', command=salvar_edicao)
    btn_atualizar.place(x=350, y=220, width=155, height=40)

    btn_apagar = ttk. Button(app, text='Apagar registro', style='Red. TButton', command=lambda: excluir_registro(btn_captura, mensagem_var) )
    btn_apagar.place(x=515, y=220, width=155, height=40)

    btn_sair = ttk.Button(app, text='Sair', style='Red. TButton', command=app.quit)
    btn_sair.place(x=685, y=220, width=155, height=40)

def criar_campo_pesquisa():
    global campo_pesquisa, btn_fechar_pesquisa, lb_pesquisar
    lb_pesquisar = Label(app, text='Digite o nome a pesquisar: ', font=('Arial', 14), bg='white' )
    lb_pesquisar.place(x=10, y=270, width=220, height=20)
    campo_pesquisa = Entry(app, font=('Arial', 14))
    campo_pesquisa.place(x=230, y=270, width=370, height=20)
    campo_pesquisa.bind('<KeyRelease>', filtrar_dados)

    btn_fechar_pesquisa = ttk.Button(app, text='Fechar pesquisa', style='Blue. TButton', command=fechar_pesquisa)
    btn_fechar_pesquisa.place(x=610, y=265, width=155, height=30)

def fechar_pesquisa():
    lb_pesquisar.destroy ()
    campo_pesquisa.destroy()
    btn_fechar_pesquisa.destroy()
    for i in tree.get_children():
        tree. delete(i)
    for pessoa in carregar_dados_arquivo():
            tree. insert ('', 'end', values=pessoa)

def criar_treeview():
    global tree
    colunas = ('nome', 'sobrenome', 'genero')
    tree = ttk. Treeview(app, columns=colunas, show='headings')
    tree. heading ('nome', text='Nome')
    tree.heading ('sobrenome', text='Sobrenome')
    tree. heading ('genero', text='Gênero')
    tree. column ('nome', minwidth=0, width=250)
    tree. column ('sobrenome', minwidth=0, width=250)
    tree. column ('genero', minwidth=0, width=100)
    tree.place(x=10, y=300, width=1000, height=290)
    tree.bind("<Double-1>", on_item_double_click)

    return tree

def on_item_double_click(event):
    editar_registro()
    btn_captura['state'] = tk.DISABLED
    mensagem_var.set('Clique no botão << ATUALIZAR DADOS >> ou << APAGAR REGISTRO >> para excluir')

#Funções para editar ou excluir registros
def editar_registro():
    global pessoa_selecionada
    try:
        tree_selection = tree.selection()[0]
        pessoa_selecionada = tree.item(tree_selection, 'values' )
        nome.delete(0, END)
        sobrenome.delete(0, END)
        nome.insert (0, pessoa_selecionada [0])
        sobrenome.insert (0, pessoa_selecionada [1])
        genero_var.set (pessoa_selecionada [2])
    except IndexError:
        messagebox.showwarning ('Aviso', 'Selecione um registro para editar!')

def salvar_edicao():
    global pessoa_selecionada
    entrada_nome = valida_campo(nome.get(), 'Nome' )
    entrada_sobrenome = valida_campo(sobrenome.get(), 'Sobrenome')
    genero_selecionado = genero_var.get()

    if not entrada_nome or not entrada_sobrenome or not genero_selecionado:
        return

    nova_pessoa = {
        'nome': entrada_nome,
        'sobrenome': entrada_sobrenome,
        'genero': genero_selecionado
    }

    if nova_pessoa == pessoa_selecionada:
        messagebox.showinfo('Aviso', 'Nenhuma alteração detectada ... ')
        return
    
    dados = []
    arquivo_json = "cadastro.json"
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
    
    for i, pessoa in enumerate(dados):
        if pessoa['nome'] == pessoa_selecionada[0] and pessoa['sobrenome'] == pessoa_selecionada[1] and pessoa['genero'] == pessoa_selecionada[2]:
            dados [i] = nova_pessoa
            break

    with open(arquivo_json, 'w') as arquivo:
        json.dump (dados, arquivo, indent=4)

    for i in tree.get_children():
        tree.delete(i)
    for pessoa in dados:
        tree.insert('', 'end', values=(pessoa['nome'], pessoa['sobrenome'], pessoa['genero']))

    nome.delete(0, 'end')
    sobrenome.delete(0, 'end')
    genero_var.set(None)
    pessoa_selecionada = None
    btn_captura['state'] = NORMAL
    mensagem_var.set("")

def excluir_registro(btn_captura, mensagem_var):
    try:
        tree_selection = tree.selection() [0]
        pessoa_selecionada = tree.item(tree_selection, 'values' )
        confirm = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este registro?")
        if confirm:
            dados = []
            arquivo_json = "cadastro. json"
            if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
                with open(arquivo_json, 'r') as arquivo:
                    dados = json. load (arquivo)

            dados = [pessoa for pessoa in dados if not (pessoa['nome'] == pessoa_selecionada[0] and pessoa['sobrenome'] == pessoa_selecionada[1] and pessoa['genero'] == pessoa_selecionada[2])]

            with open(arquivo_json, 'w') as arquivo:
                json.dump (dados, arquivo, indent=4)
            
            tree.delete(tree_selection)
    except IndexError:
        messagebox. showwarning('Aviso', 'Selecione um registro para excluir!')
    finally:
        btn_captura['state'] = 'normal'
        mensagem_var.set ("")

def capturar():
    entrada_nome = valida_campo(nome.get(), 'Nome' )
    entrada_sobrenome = valida_campo(sobrenome.get(), 'Sobrenome' )
    genero_selecionado = genero_var.get()

    # Verifica o gênero selecionado
    if genero_selecionado not in ['Masculino', 'Feminino', 'Outros'] :
        messagebox.showwarning( 'Aviso', 'Selecione um gênero. ' )
        return

    if not entrada_nome or not entrada_sobrenome:
        return

    pessoa = {
        'nome': entrada_nome,
        'sobrenome': entrada_sobrenome,
        'genero' : genero_selecionado
    }

    grava_dados_arquivo(pessoa)
    tree.insert('', 'end', values=(pessoa['nome'], pessoa['sobrenome'], pessoa['genero']))

    nome.delete(0, 'end')
    sobrenome.delete(0, 'end')
    genero_var.set(None)

def mostrar_campo_pesquisa():
    mensagem_var.set('')
    criar_campo_pesquisa()

def filtrar_dados(event):
    for i in tree.get_children():
        tree.delete(i)
    termo_pesquisa = campo_pesquisa.get()
    dados_filtrados = [pessoa for pessoa in carregar_dados_arquivo() if termo_pesquisa. lower() in pessoa[0]. lower ()]
    for pessoa in dados_filtrados:
        tree. insert('', 'end', values=pessoa)
    
#Configuraçoes iniciais do Tkinter

if __name__ == '_main_':
    app = Tk()
    configurar_app()
    frame = criar_frame()
    criar_labels(frame)
    nome, sobrenome = criar_entry(frame)
    genero_var = criar_checkbutton(frame)
    criar_botao( )
    tree = criar_treeview( )
    for pessoa in carregar_dados_arquivo() :
        tree. insert('', 'end', values=pessoa)
    app.mainloop()

