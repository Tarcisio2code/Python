"""
Interface gráfica com botão
20-11-20: Tarcisio Silva
"""
from tkinter import *

def funcClicar():
    print("Botão pressionado")
    texto["bg"] = "blue"

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Janela Gráfica com botão")
texto.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar())
botao.pack()

janelaPrincipal.mainloop()
