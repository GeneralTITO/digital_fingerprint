#funcoes/admin.py

from tkinter import messagebox
from tkinter import Toplevel
from tkinter import Label

def acessar_parte_restrita(senha_entry, ):
    senha_correta = "123"  # Substitua pela senha real
    senha_inserida = senha_entry.get()
    
    if senha_inserida == senha_correta:
        messagebox.showinfo("Acesso Permitido", "Você acessou a parte restrita do programa.")
         # Crie uma nova janela para a parte restrita
        janela_restrita = Toplevel()
        janela_restrita.title("Parte Restrita")
        
        # Adicione widgets ou elementos à nova janela restrita
        label = Label(janela_restrita, text="Bem-vindo à parte restrita!")
        label.pack()
    else:
        messagebox.showerror("Senha Incorreta", "A senha inserida está incorreta.")