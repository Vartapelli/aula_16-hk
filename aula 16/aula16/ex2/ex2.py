import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
#janela.withdraw
messagebox.showinfo('Star wars', 'A força esteja contigo') #tipo info
messagebox.showwarning('Alerta', 'O lado sombrio é periogoso')
messagebox.showerror('Erro', 'Falha no HiperDriver!')

janela.mainloop()