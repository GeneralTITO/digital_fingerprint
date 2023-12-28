import pickle
from utils.relogio import actual_time
from datetime import datetime



def save_verification(new_verification):
    list_old = load_verification()
    real_time = actual_time()
    print(real_time, " time")
    data = [new_verification[1], new_verification[2], real_time]
    print(data, "data")
    list_old.append(data)
    with open("verifications.pickle", "wb") as arquivo:
        pickle.dump(list_old, arquivo)


def load_verification():
    try:
        with open("verifications.pickle", "rb") as arquivo:
            list_verification = pickle.load(arquivo)
    except FileNotFoundError:
        return []
    except EOFError:
        return []
    except Exception as e:
        print("An error occurred while loading data:", str(e))
        return []

    return list_verification


def search_by_day(dia_especifico):
    registros_do_dia = []
    formato_data_hora = "%d/%m/%Y %H:%M"

    registros  = load_verification()
    for registro in registros:
        data_hora_registro = datetime.strptime(registro[2], formato_data_hora)

        dia_registro = data_hora_registro.strftime("%d/%m/%Y")

        if dia_registro == dia_especifico:
            registros_do_dia.append(registro)

    if not registros_do_dia:
        return "Nenhum registro encontrado para o dia específico."

    mensagem = (
        f"Registros encontrados para o dia {registros_do_dia[0][2].split()[0]}:\n"
    )

    for registro in registros_do_dia:
        mensagem += f"{registro[0]} - {registro[2]}\n"

    return mensagem