import time

def atualizar_hora(label, root):
    hora_atual = time.strftime("%H:%M:%S")  
    label.config(text=hora_atual)
    root.after(1000, atualizar_hora)