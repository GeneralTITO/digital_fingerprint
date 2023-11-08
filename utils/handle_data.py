import pickle


def salvar_pessoas(lista_pessoas):
    with open("pessoas.pickle", "wb") as arquivo:
        pickle.dump(lista_pessoas, arquivo)


def carregar_pessoas():
    try:
        with open("pessoas.pickle", "rb") as arquivo:
            lista_pessoas = pickle.load(arquivo)
    except FileNotFoundError:
        lista_pessoas = []

    return lista_pessoas
