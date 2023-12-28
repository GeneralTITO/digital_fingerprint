import time, datetime


def atualizar_hora(label, root):
    hora_atual = time.strftime("%H:%M:%S")
    label.config(text=f"horario atual: {hora_atual}")
    root.after(1000, lambda: atualizar_hora(label, root))


def actual_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%d/%m/%Y %H:%M")
    return formatted_time
