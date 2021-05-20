"""
Interface gráfica com imagem
20-11-20: Tarcisio Silva
"""

from tkinter import *

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Janela Gráfica com imagem")
texto.pack() # centraliza o objeto mais proximo do topo

pic = PhotoImage(file="lindas.png") # cria o objeto com a imagem
logo = Label(master = janelaPrincipal, image = pic) # cria um label com a imagem
logo.pack()

janelaPrincipal.mainloop()
