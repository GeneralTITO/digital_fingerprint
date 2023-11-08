from data import pessoas_cadastradas
import pickle

def save(new_person):
    pessoas_cadastradas.append(new_person)
    return pessoas_cadastradas

def get_data():
    return pessoas_cadastradas