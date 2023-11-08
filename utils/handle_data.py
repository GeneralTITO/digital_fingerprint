import pickle


def carregar_dicionario(nome_arquivo):
    try:
        with open(nome_arquivo, "rb") as arquivo:
            return pickle.load(arquivo)

    except (FileNotFoundError, EOFError):
        return {}

def salvar_dicionario(dicionario, nome_arquivo):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(dicionario, arquivo)