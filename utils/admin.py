from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from utils.fingerprint import enroll
from utils.handle_data import *

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
        janela_restrita.geometry('800x600')

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
        email = StringVar()
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
        label_enroll_email = ttk.Label(label_enroll_main, text="email")
        label_enroll_email.grid(column=0, row=1, padx=10)
        entry_email = ttk.Entry(label_enroll_main, textvariable=email)
        entry_email.grid(column=1, row=1, pady=10)

        def capturar_digital():
            fingerprint = enroll()
            new_person.append(fingerprint)

        def cadastrar():
            new_person.append(nome.get())
            new_person.append(telefone.get())
            salvar_pessoas(new_person)
            nome.set("")
            telefone.set("")
            new_person.clear()
            atualizar_treeview()

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


        def editar_selecionado():
            item_selecionado = treeview.focus()
            valores_atuais = treeview.item(item_selecionado, 'values')

            def salvar_edicao():
                # Atualiza os valores na Treeview
                novos_valores = [entry.get() for entry in entry_vars]
                treeview.item(item_selecionado, values=novos_valores)
                # Salva as alterações no arquivo ou banco de dados, se necessário
                list_old = carregar_pessoas()
                for i, item in enumerate(list_old):
                    if item[1] == valores_atuais[0]:
                        list_old[i][1]=novos_valores[0]
                        list_old[i][2]=novos_valores[1]
                        sobrescrever(list_old)

                # Fecha a janela de edição
                janela_edicao.destroy()

            # Cria uma nova janela para edição
            janela_edicao = Toplevel()
            janela_edicao.title("Editar Funcionário")

            # Adiciona Entry para cada coluna
            entry_vars = []
            for i, valor_atual in enumerate(valores_atuais):
                ttk.Label(janela_edicao, text=f"{treeview.heading(i)['text']}").grid(row=i, column=0, padx=5, pady=5)
                novo_valor = StringVar(value=valor_atual)
                entry_vars.append(novo_valor)
                ttk.Entry(janela_edicao, textvariable=novo_valor).grid(row=i, column=1, padx=5, pady=5)

            # Adiciona um botão "Salvar"
            ttk.Button(janela_edicao, text="Salvar", command=salvar_edicao).grid(row=len(valores_atuais), columnspan=2, pady=10)

        # Adiciona o evento de duplo clique na Treeview
        treeview.bind("<Double-1>", lambda event: editar_selecionado())

        # ... (seu código existente)
        def atualizar_treeview():
            for item in treeview.get_children():
                treeview.delete(item)
            people = list_treeview()
            for person in people:
                treeview.insert('', END, values=person)

        atualizar_treeview()
        treeview.grid(column=0, row=0)

        # opção 2 do notebook
        f2 = ttk.Frame(main_notebook)
        main_notebook.add(f2, text="Configurar intervalos de verificação")

    else:
        messagebox.showerror("Senha Incorreta", "A senha inserida está incorreta.")
