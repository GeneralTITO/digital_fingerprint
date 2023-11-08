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
        # cria a janela
        janela_restrita = Toplevel()
        janela_restrita.title("Parte Restrita")

        # cria o frame principal
        mainframe = ttk.Frame(janela_restrita, padding=10)
        mainframe.grid(row=0, column=0)

        # cria o notebook
        main_notebook = ttk.Notebook(mainframe, style="TNotebook.Tab")
        main_notebook.grid(row=0, column=0, sticky="nsew")

        # opção 1 do notebook
        f1 = ttk.Frame(main_notebook, padding=10)
        main_notebook.add(f1, text="Funcionários")

        nome = StringVar()
        telefone = StringVar()
        new_person = []

        # parte 1 da opção 1
        label_enroll_main = ttk.Labelframe(
            f1, text="Cadastrar funcionários", padding=10
        )
        label_enroll_main.grid(column=0, row=0)

        label_enroll_name = ttk.Label(label_enroll_main, text="Nome")
        label_enroll_name.grid(column=0, row=0, pady=10)
        entry_name = ttk.Entry(label_enroll_main, textvariable=nome)
        entry_name.grid(column=1, row=0)
        label_enroll_phone = ttk.Label(label_enroll_main, text="telefone")
        label_enroll_phone.grid(column=0, row=1, padx=10)
        entry_phone = ttk.Entry(label_enroll_main, textvariable=telefone)
        entry_phone.grid(column=1, row=1, pady=10)

        def capturar_digital():
            fingerprint = enroll()
            new_person.append(fingerprint)
            print(new_person)

        def cadastrar ():
            new_person.append(nome.get())
            new_person.append(telefone.get())
            print(new_person)
            nome.set('')
            telefone.set('')
            new_person.clear()
        # def cadastrar():
        #     nome1 = nome.get()
        #     telefone1= telefone.get()
        #     new_person.appen(nome1)
        #     new_person.append(telefone1)
        #     print(new_person)
        #     nome.set('')
        #     telefone.set('')
        #     new_person = []

        button_capture = ttk.Button(
            label_enroll_main,
            text="Capturar digital",
            command=capturar_digital,
            padding=3,
        )
        button_capture.grid(column=0, row=3, columnspan=2, pady=5)

        button_enroll = ttk.Button(
            label_enroll_main, text="Cadastrar", padding=10, command=cadastrar
        )
        button_enroll.grid(column=0, row=4, columnspan=2, pady=10)

        # parte 2 da opção 1
        label_alredy_enrolled = ttk.Labelframe(
            f1, text="Funcionários cadastrados", padding=10
        )
        label_alredy_enrolled.grid(row=0, column=2)

        treeview = ttk.Treeview(
            label_alredy_enrolled, columns=("Nome", "Telefone"), show="headings"
        )
        treeview.heading("Nome", text="Nome")
        treeview.heading("Telefone", text="Telefone")

        treeview.grid(column=0, row=0)

        # opção 2 do notebook
        f2 = ttk.Frame(main_notebook)
        main_notebook.add(f2, text="Configurar intervalos de verificação")

    else:
        messagebox.showerror("Senha Incorreta", "A senha inserida está incorreta.")
