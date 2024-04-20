# Definindo uma janela simples no tkinter:
'''
from tkinter import *
app = Tk()
app.mainloop()
'''
# Uma nova janela com elementos extras na janela
'''
from tkinter import *
app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.geometry('800x480')
app.configure(background='#ffffff')
app.resizable(True, True)
app.maxsize(width=1360, height=670)
app.minsize(width=800, height=480)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
label =  Label(app, text="Bem-vindo ao Curso de Análise e Desenvolvimento de Sistemas", bg='#fa5882')
label.grid(sticky='NSEW')
app.mainloop()
'''