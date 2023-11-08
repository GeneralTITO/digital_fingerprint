from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from utils.fingerprint import enroll


def acessar_parte_restrita(senha_entry):
    senha_correta = "123"
    senha_inserida = senha_entry.get()

    if senha_inserida == senha_correta:
        messagebox.showinfo(
            "Acesso Permitido", "Você acessou a parte restrita do programa."
        )
        janela_restrita = Toplevel()
        janela_restrita.title("Parte Restrita")

        mainframe = ttk.Frame(janela_restrita, padding=10)
        mainframe.grid(row=0, column=0)

        main_notebook = ttk.Notebook(mainframe, style="TNotebook.Tab")
        main_notebook.grid(row=0, column=0, sticky="nsew")

        f1 = ttk.Frame(main_notebook, padding=10)
        main_notebook.add(f1, text="Funcionários")

        nome = StringVar()
        telefone = StringVar()

        label_enroll_main = ttk.Labelframe(f1, text='Cadastrar funcionários', padding=10)

        label_enroll_name = ttk.Label(label_enroll_main, text="Nome")
        label_enroll_name.grid(column=0, row=0, pady=10)
        entry_name = ttk.Entry(label_enroll_main, textvariable=nome)
        entry_name.grid(column=1, row=0)
        label_enroll_phone = ttk.Label(label_enroll_main, text="telefone")
        label_enroll_phone.grid(column=0, row=1, padx=10)
        entry_phone = ttk.Entry(label_enroll_main, textvariable=telefone)
        entry_phone.grid(column=1, row=1, pady=10)

        button_capture = ttk.Button(label_enroll_main, text='Capturar digital', command=enroll, padding=3)
        button_capture.grid(column=0, row=3, columnspan=2, pady=5)

        button_enroll = ttk.Button(label_enroll_main, text='Cadastrar', padding=10)
        button_enroll.grid(column=0, row=4, columnspan=2, pady=10)

        label_enroll_main.grid(column=0, row=0)



        f2 = ttk.Frame(main_notebook)
        main_notebook.add(f2, text="Configurar intervalos de verificação")

    else:
        messagebox.showerror("Senha Incorreta", "A senha inserida está incorreta.")
