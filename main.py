from tkinter import *
from tkinter import ttk
from utils.admin import acessar_parte_restrita
from utils.relogio import atualizar_hora
from utils.fingerprint import *

root = Tk()
root.title("Fingerprint")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


frame_interval_info = ttk.Frame(root)
frame_interval_info.grid(column=0, row=0, pady=2)
label_interval_info = ttk.Label(
    frame_interval_info, text="intervalo de verificação:<<<9:00 - 9:15>>> ", padding=10
)
label_interval_info.grid(column=0, row=0)

frame_horario_atual = ttk.Frame(root)
frame_horario_atual.grid(column=0, row=1, pady=10)
label_horario_atual = ttk.Label(frame_horario_atual, padding=10)
label_horario_atual.grid(column=0, row=0)
atualizar_hora(label=label_horario_atual, root=root)


frame_button = ttk.Frame(root)
frame_button.grid(column=0, row=3, pady=10)

name_var = StringVar()


def verify_func():
    name = verify()
    if name == "Digital não cadastrada":
        return name_var.set("Digital não cadastrada")
    name_var.set(f"{name}, digital verificada")


button_verication = ttk.Button(
    frame_button, text="Verificar digital", padding=10, command=verify_func
)
button_verication.grid(column=0, row=0)
label_verication = ttk.Label(frame_button, textvariable=name_var)
label_verication.grid(row=2, column=0)

ttk.Separator(root, orient="horizontal").grid(
    row=4, column=0, sticky="ew", padx=10, pady=10
)

frame_admin = ttk.Frame(root)
frame_admin.grid(row=5, column=0, padx=10, pady=10)
label_admin = ttk.Label(frame_admin, text="Admin: ")
label_admin.grid(column=0, row=0)
senha = StringVar()
entry_admin = ttk.Entry(frame_admin, textvariable=senha, show="*")
entry_admin.grid(column=2, row=0, padx=10, pady=10)


def access_buttun_fuc():
    acessar_parte_restrita(senha)
    senha.set("")


button_access = ttk.Button(frame_admin, text="Acessar", command=access_buttun_fuc)
button_access.grid(row=0, column=3)


root.mainloop()
