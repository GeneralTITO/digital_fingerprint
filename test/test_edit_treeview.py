import tkinter as tk
from tkinter import ttk, simpledialog

def adicionar_item():
    nome = nome_entry.get()
    idade = idade_entry.get()
    tree.insert("", "end", values=(nome, idade))
    nome_entry.delete(0, "end")
    idade_entry.delete(0, "end")

def excluir_item():
    selecao = tree.selection()
    for item in selecao:
        tree.delete(item)

def editar_item():
    selecao = tree.selection()
    if selecao:
        nome_atual, idade_atual = tree.item(selecao[0], "values")
        novo_nome = simpledialog.askstring("Editar Nome", "Novo Nome:", initialvalue=nome_atual)
        if novo_nome is not None:
            nova_idade = simpledialog.askinteger("Editar Idade", "Nova Idade:", initialvalue=idade_atual)
            if nova_idade is not None:
                tree.item(selecao[0], values=(novo_nome, nova_idade))

def obter_itens_selecionados():
    selecao = tree.selection()
    for item in selecao:
        print(tree.item(item)["values"])

janela = tk.Tk()
janela.title("Exemplo de Treeview com Edição por Dialog")

# Crie o Treeview
tree = ttk.Treeview(janela, columns=("Nome", "Idade"), show='headings')
tree.heading("#1", text="Nome")
tree.heading("#2", text="Idade")
tree.grid(row=0, column=0, columnspan=2)

# Entradas
nome_label = tk.Label(janela, text="Nome:")
idade_label = tk.Label(janela, text="Idade:")
nome_entry = tk.Entry(janela, width=20)
idade_entry = tk.Entry(janela, width=10)

nome_label.grid(row=1, column=0, sticky=tk.E)
idade_label.grid(row=2, column=0, sticky=tk.E)
nome_entry.grid(row=1, column=1)
idade_entry.grid(row=2, column=1)

# Botões
adicionar_button = tk.Button(janela, text="Adicionar Item", command=adicionar_item)
excluir_button = tk.Button(janela, text="Excluir Item", command=excluir_item)
editar_button = tk.Button(janela, text="Editar Item", command=editar_item)
obter_selecionados_button = tk.Button(janela, text="Obter Selecionados", command=obter_itens_selecionados)

adicionar_button.grid(row=3, column=0)
excluir_button.grid(row=3, column=1)
editar_button.grid(row=4, column=0)
obter_selecionados_button.grid(row=4, column=1)

# Configurar colunas
tree.column("#1", width=100)
tree.column("#2", width=100)

janela.mainloop()
