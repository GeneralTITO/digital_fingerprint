import pickle
from utils.relogio import actual_time

def save_verification (new_verification):
    list_old = load_verification()
    real_time = actual_time()
    print(real_time," time")
    data = [new_verification[1], new_verification[2], real_time]
    print(data, 'data')
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


