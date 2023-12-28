# from datetime import datetime

# def procurar_por_dia(registros, dia_especifico):
#     registros_do_dia = []
#     formato_data_hora = "%d/%m/%Y %H:%M"

#     for registro in registros:

#         data_hora_registro = datetime.strptime(registro[2], formato_data_hora)

#         dia_registro = data_hora_registro.strftime("%d/%m/%Y")

#         if dia_registro == dia_especifico:
#             registros_do_dia.append(registro)

#     return registros_do_dia


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

# dia_especifico = "28/12/2023"
# registros_encontrados = procurar_por_dia(registros, dia_especifico)

# print(f"Registros encontrados para o dia {dia_especifico}:")
# for registro in registros_encontrados:
#     print(registro)



new_person =   ["messi", "0000", "28/12/2023 15:09"]
print(len(new_person))