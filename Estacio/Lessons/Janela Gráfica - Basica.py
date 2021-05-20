"""
Meu Primeiro promama com interface gráfica
20-11-20: Tarcisio Silva
"""

from tkinter import * # importa o módulo de interface gráfica

janelaPrincipal = Tk() # cria o objeto Janela.
# código para exibir o conteúdo na janela.
texto = Label(master = janelaPrincipal, text = "Minha primeira Janela Gráfica") # o elemento Label exibe os textos
texto.place(x=10, y=100)
janelaPrincipal.mainloop() # metodo que exibe o objeto janela.

