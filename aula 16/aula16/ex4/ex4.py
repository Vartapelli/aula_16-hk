import tkinter as tk
from tkinter import simpledialog, messagebox

janela = tk.Tk()
janela.title('Profile theme')
janela.geometry('400x300')

nome = simpledialog.askstring("Começando ao seu Cadastro", "Qual seu nome?")


if nome:
   messagebox.showinfo(
      'Seu Cadastro',
      f'Que a força esteja com voce{nome}\n'
   )

