from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def acessar_parte_restrita(senha_entry):
    senha_correta = "123"
    senha_inserida = senha_entry.get()

    if senha_inserida == senha_correta:
        messagebox.showinfo("Acesso Permitido", "Você acessou a parte restrita do programa.")
        janela_restrita = Toplevel()
        janela_restrita.title("Parte Restrita")

        mainframe = ttk.Frame(janela_restrita, padding=10)
        mainframe.grid(row=0, column=0)

        main_notebook = ttk.Notebook(mainframe, style="TNotebook.Tab")
        main_notebook.grid(row=0, column=0, sticky="nsew")

        f1 = ttk.Frame(main_notebook)
        f2 = ttk.Frame(main_notebook)
        main_notebook.add(f1, text='Funcionários')
        main_notebook.add(f2, text='Configurar intervalos de verificação')

    else:
        messagebox.showerror("Senha Incorreta", "A senha inserida está incorreta.")

