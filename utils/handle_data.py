import pickle


def salvar_pessoas(lista_pessoas):
    list_old = carregar_pessoas()
    list_old.append(lista_pessoas)
    with open("pessoas.pickle", "wb") as arquivo:
        pickle.dump(list_old, arquivo)

def sobrescrever(lista_pessoas):
    with open("pessoas.pickle", "wb") as arquivo:
        pickle.dump(lista_pessoas, arquivo)


def carregar_pessoas():
    try:
        with open("pessoas.pickle", "rb") as arquivo:
            lista_pessoas = pickle.load(arquivo)
    except FileNotFoundError:
        return []
    except EOFError:
        return []
    except Exception as e:
        print("An error occurred while loading data:", str(e))
        return []

    return lista_pessoas


def list_treeview():
    nova_lista_pessoas = [pessoa[1:] for pessoa in carregar_pessoas()]
    return nova_lista_pessoas

