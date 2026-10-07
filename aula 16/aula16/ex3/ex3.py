
import tkinter as tk
from tkinter import simpledialog, messagebox

janela = tk.Tk()
janela.withdraw()

# Pedir texto
nome = simpledialog.askstring("Cadastro Jedi", "Qual é o seu nome, jovem Padawan?")

# Pedir número inteiro
poder = simpledialog.askinteger(
    "Nível de Força",
    "Qual seu nível de Força? (1 a 100)",
    minvalue=1,
    maxvalue=100
)

# Pedir número decimal
midichlorians = simpledialog.askfloat(
    "Midi-chlorians",
    "Contagem de midi-chlorians:"
)

if nome and poder:
    messagebox.showinfo(
        "Ficha Jedi",
        f"Nome: {nome}\n"
        f"Nível de Força: {poder}\n"
        f"Midi-chlorians: {midichlorians}"
    )

janela.destroy()
