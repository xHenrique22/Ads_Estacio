import tkinter as tk
from tkinter import messagebox


janelaPrincipal = tk.Tk()
janelaPrincipal.title("Minha primeira janela")
janelaPrincipal.geometry("300x200")

texto = tk.Label(janelaPrincipal, text="Minha janela exibida", font=("Arial", 16))

def clicar_botao():
    messagebox.showinfo("Mensagem", "Você clicou no botão!")

botao = tk.Button(janelaPrincipal, text="Clique aqui", command=clicar_botao, font=("Arial", 12))

botao.place(x=100, y=150)

janelaPrincipal.mainloop()
    
