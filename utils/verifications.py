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


# # Exemplo de uso
# registros = [
#     ["joao", "123123", "29/12/2023 14:15"],
#     ["messi", "0000", "28/12/2023 14:15"],
#     ["joao", "123123", "28/12/2023 14:44"],
#     ["joao", "123123", "28/12/2023 14:56"],
#     ["messi", "0000", "28/12/2023 14:56"],
#     ["cr7", "7777", "28/12/2023 14:56"],
#     ["joao", "123123", "28/12/2023 15:05"],
#     ["joao", "123123", "28/12/2023 15:09"],
#     ["messi", "0000", "28/12/2023 15:09"],
#     ["cr7", "7777", "28/12/2023 15:09"],
# ]

# dia_especifico = "29/12/2023"
# registros_encontrados = search_by_day(registros, dia_especifico)

# print(f"Registros encontrados para o dia {dia_especifico}:")
# for registro in registros_encontrados:
#     print(registro)
