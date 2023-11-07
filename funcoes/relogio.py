import time

def atualizar_hora(label, root):
    hora_atual = time.strftime("%H:%M:%S")
    label.config(text=f'horario atual: {hora_atual}')
    root.after(1000, lambda: atualizar_hora(label, root))