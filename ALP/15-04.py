#a) Faça um script que mostra na tela os números de 0 a 100, usando o laço de repetição for(), com passagens de 5 em 5.
'''for num in range(0, 101, 5):
  print(num)
'''

#b) Faça um script que tenha uma estrutura de repetição for() aninhados que: - Utilize tenha for aninhados e a função range(). - Tenha um iterador em for() i que conte até 5.    - Tenha outro iterador em for() j que conte até 5. - Apresente o valor do iterador i e do iterador j até esgotar o range.
'''for i in range(1, 6):
    for j in range(1, 6):
        print(f"i: {i}, j: {j}")
'''

#c) Faça uma estrutura de repetição usando for() e range() que: - Apresente a tabuada de um número que o operador digitar. - Atenção o primeiro multiplicador deve ser 1.
'''num = int(input("Digite um número: "))
for mult in range(1, 11):
    result = num * mult
    print(f"{num} x {mult} = {result}")
'''

#d) Complexidade algorítmica: faça uma estrutura de repetição usando for() e range() que apresente a tabuada completa entre 1 e 10:
# Solicita ao usuário para digitar um número
'''num = int(input("Apresentando a tabuada do "))
for mult in range(1, 11):
  result = num * mult
  print(f"{num} x {mult}: é {mult} = {result}")
'''

#e) Faça uma estrutura de repetição usando for() e range() que apresente todos os números ímpares entre 1 e 100.
'''for num in range(1, 101, 2):
    print(f"Número: {num}")
'''

#f) 1ª Criando uma lista vazia
'''list1 = list()
print(f'\nLista criada: {list1}')
print(f'\nO tipo de váriavel list1n é: {type(list1)}')
'''

#g) Criando uma lista vazia - 2ª forma:
'''list2 = []
print(f'\nLista criada: {list2} \n')
print(f'O tipo da variável list2 é: {type(list2)} \n')
'''

#h) Criando e Inserindo elementos dentro da lista criada de forma direta:
'''list3 = ['Curso', 98, 'Análise', 11, 'e Desenvolvimento', 27, 'de Sistemas']
print(f'\nOs elementos que estão dentro da lista criada são: {list3}')
print(f'\nA quantidade de elementos que estão dentro da list3 é: {len(list3)}')
'''

#i) Inserindo elementos no final de uma lista criada – 1ª Forma
'''list4 = []
list4.append('IFRO')
list4.append('Campus')
list4.append('Ariquemes')
list4.append('2024')
print(f'\nOs elementos que estão na list4 são: {list4} \n')
print(f'\nA quantidade de elementos que estão dentro da list4 é: {len(list4)}')
print(f'\nO tipo da variável list4 é: {type(list4)}')
'''

#j) Inserindo elementos no final de uma lista criada – 2ª Forma
'''list5 = []
list5.append(input(f'\nDigite um dado: '))
list5.append(input(f'\nDigite outro dado: '))
list5.append(int(input(f'\nDigite mais um valor: ')))
print(f'\nOs elementos que estão na list5 são: {list5}')
print(f'\nA quantidade de elementos que estão dentro da list5 é: {len(list5)}')
print(f'\nO tipo da variável list5 é: {type(list5)}')
'''

#k) Inserindo elementos no final de uma lista criada – 3ª Forma
'''list6 = []
variavel = input(f'\nDigite um dado: ')
list6.append(variavel)
variavel = input(f'\nDigite outro dado: ')
list6.append(variavel)
variavel = int(input(f'\nDigite mais um valor: '))
list6.append(variavel)
print(f'\nOs elementos que estão na list6 são: {list6}')
print(f'\nA quantidade de elementos que estão dentro da list6 é: {len(list6)}')
print(f'\nO tipo da variável list6 é: {type(list6)}')
'''

#L) Apresentando os elementos que estão na lista
'''list7 = ['Algoritimos', 'e Lógica', 'de Programação', '2024-1']
print(f'\nA lista possui os seguintes elementos: {list7}')
print(f'\nO elemento que está no índicie 3 da list7 é: {list7[3]}')
print(f'\nO elemento que está no índicie 0 da list7 é: {list7[0]}')
print(f'\nO elemento que está no índicie 2 da list7 é: {list7[2]}')
'''


#TKINTER
## Definindo uma janela simples no tkinter
'''from tkinter import *
app = Tk()
app.mainloop()
'''

# Usando o sistema de gerenciamento de layout grid para trabalhar:
'''from tkinter import *
import tkinter.font as tkFont
app = Tk()
app.geometry("500x500")
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
font_size = max(10, int(screen_height * 0.02))
font = tkFont.Font(size=font_size)
label = Label(app, text="Algoritimo e Lógica de Programação", font=font)
label.grid(sticky="NSEW")
app.mainloop()
'''

#m)Implementando e posicionando um frame dentro de uma janela:
'''from tkinter import *
import tkinter.font as tkFont
def resize_font(event):
  new_size = max(10, int(frame.winfo_height() * 0.05))
  font.configure(size=new_size)
app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.configure(background='#F8E0E6')
app.grid_rowconfigure(0, weight=4)
app.grid_rowconfigure(1, weight=6)
app.grid_columnconfigure(0, weight=1)
frame = LabelFrame(app, text='Castro', borderwidth=1, relief='solid', background='#E0F2F7')
frame.grid(row=0, column=0,  sticky='NSEW', padx=3, pady=3)
frame.bind('<Configure>', resize_font)
font =  tkFont.Font(size=10)
app.minsize(width=800, height=480)
app.mainloop()
'''

# Implementando e posicionando um Label e entry dentro do Frame:
'''from tkinter import *
import tkinter.font as tkFont

def resize_font(event):
    new_size = max(10, int(frame.winfo_height() * 0.05))
    font.configure(size=new_size)
    label.config(font=font)
    entry.config(font=font)
    display_label.config(font=font)
    submit_button.grid(font=font)
    submit_button.config(font=font)

def adicionar():
    name=entry.get()
    display_label.config(text='O nome digitado foi:"{}"'.format(name))

app = Tk()

app.title('Análise e Desenvolvimento de Sistemas')

app.configure(background='#F8E0E6')

app.grid_rowconfigure(0, weight=4)

app.grid_rowconfigure(1, weight=6)

app.grid_columnconfigure(0, weight=1)

frame = LabelFrame(app, text='Cadastro', borderwidth=1, relief='solid', background='#E0F2F7')
frame.grid(row=0, column=0, sticky='NSEW', padx=3, pady=3)

frame.bind('<Configure>', resize_font)

font = tkFont.Font(size=18)

label = Label(frame, text='Digite um Nome:', font=font, background='#E0F2F7')
label.grid(row=0, column=0, sticky='W', padx=(3, 20))

entry = Entry(frame, font=font)
entry.grid(row=0, column=1, sticky='EW', padx=(10))

submit_button = Button(frame, text='Adicionar', command=adicionar, font=font)
submit_button.grid(row=1, column=1, sticky='S', pady=10)

display_label = Label(frame, text='', font=font, background='white')
display_label.grid(row=2, column=0, columnspan=2, sticky='W', padx=3)

frame.grid_columnconfigure(1, weight=1)

app.minsize(width=800, height=480)

app.mainloop()
'''
