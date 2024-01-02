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
        janela_restrita = Toplevel()
        janela_restrita.title("Parte Restrita")

        # cria o frame principal
        mainframe = ttk.Frame(janela_restrita, padding=10)
        mainframe.grid(row=0, column=0, sticky=(N, S, W, E))

        # frame da parte 1
        f1 = ttk.Frame(mainframe, padding=10)

        f1.grid(row=0, column=0, sticky=(N, S, W, E))

        nome = StringVar()
        email = StringVar()
        new_person = []

        label_enroll_main = ttk.Labelframe(
            f1, text="Cadastrar funcionários", padding=10
        )
        label_enroll_main.grid(column=0, row=0, sticky=(N, S, W, E))

        label_enroll_name = ttk.Label(label_enroll_main, text="Nome")
        label_enroll_name.grid(column=0, row=0, pady=10)
        entry_name = ttk.Entry(label_enroll_main, textvariable=nome, width=50)
        entry_name.grid(column=1, row=0, sticky=(E, W))
        label_enroll_email = ttk.Label(label_enroll_main, text="Email")
        label_enroll_email.grid(column=0, row=1, padx=10)
        entry_email = ttk.Entry(label_enroll_main, textvariable=email, width=50)
        entry_email.grid(column=1, row=1, pady=10, sticky=(E, W))

        def capturar_digital():
            fingerprint = enroll()
            new_person.append(fingerprint)

        def cadastrar():
            if len(new_person) == 1:
                new_person.append(nome.get())
                new_person.append(email.get())
                if len(new_person) == 3:
                    salvar_pessoas(new_person)
                    nome.set("")
                    email.set("")
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
            label_enroll_main,
            text="Cadastrar",
            padding=10,
            command=cadastrar,
        )

        button_enroll.grid(column=0, row=4, columnspan=2, pady=10)

        # parte 2
        label_alredy_enrolled = ttk.Labelframe(
            f1, text="Funcionários cadastrados", padding=10
        )
        label_alredy_enrolled.grid(row=1, column=0)

        treeview = ttk.Treeview(
            label_alredy_enrolled, columns=("Nome", "Email"), show="headings"
        )
        treeview.heading("Nome", text="Nome")
        treeview.heading("Email", text="Email")

        def excluir_selecionado():
            item_selecionado = treeview.focus()
            valores_atuais = treeview.item(item_selecionado, "values")

            confirma_exclusao = messagebox.askokcancel(
                "Confirmar Exclusão",
                f"Tem certeza que deseja excluir o funcionário {valores_atuais[0]}?",
            )

            if confirma_exclusao:
                treeview.delete(item_selecionado)

                list_old = carregar_pessoas()
                for i, item in enumerate(list_old):
                    if item[1] == valores_atuais[0]:
                        del list_old[i]
                        sobrescrever(list_old)

        def editar_selecionado():
            item_selecionado = treeview.focus()
            valores_atuais = treeview.item(item_selecionado, "values")

            def salvar_edicao():
                novos_valores = [entry.get() for entry in entry_vars]
                treeview.item(item_selecionado, values=novos_valores)

                list_old = carregar_pessoas()
                for i, item in enumerate(list_old):
                    if item[1] == valores_atuais[0]:
                        list_old[i][1] = novos_valores[0]
                        list_old[i][2] = novos_valores[1]
                        sobrescrever(list_old)

                janela_edicao.destroy()

            janela_edicao = Toplevel()
            janela_edicao.title("Editar Funcionário")

            entry_vars = []
            for i, valor_atual in enumerate(valores_atuais):
                ttk.Label(janela_edicao, text=f"{treeview.heading(i)['text']}").grid(
                    row=i, column=0, padx=5, pady=5
                )
                novo_valor = StringVar(value=valor_atual)
                entry_vars.append(novo_valor)
                ttk.Entry(janela_edicao, textvariable=novo_valor).grid(
                    row=i, column=1, padx=5, pady=5
                )

            ttk.Button(janela_edicao, text="Salvar", command=salvar_edicao).grid(
                row=len(valores_atuais), columnspan=2, pady=10
            )

        def atualizar_treeview():
            for item in treeview.get_children():
                treeview.delete(item)
            people = list_treeview()
            for person in people:
                treeview.insert("", END, values=person)

        button_excluir = ttk.Button(
            label_alredy_enrolled,
            text="Excluir",
            command=excluir_selecionado,
            padding=2,
        )
        button_excluir.grid(column=0, row=2, pady=10, sticky=(W))

        button_editar = ttk.Button(
            label_alredy_enrolled,
            text="Editar",
            command=editar_selecionado,
            padding=2,
        )
        button_editar.grid(column=0, row=2, pady=10, sticky=(E))

        atualizar_treeview()
        treeview.grid(column=0, row=0)
    else:
        messagebox.showerror("Senha Incorreta", "A senha inserida está incorreta.")
