#Criar janela simples
import tkinter as tk

janela = tk.Tk() #criando a janela
janela.title('Star Wars Theme') #titulo da janela
janela.geometry('400x300') #tamanho da janela

label = tk.Label(janela, text="Que a força esteja com voce", font=('Arial', 16))
label.pack(pady=50)

janela.mainloop()