from utils.handle_data import *


atual = carregar_dicionario('data.pkl')
print(atual)

atual['1']=['joao','123123123']
salvar_dicionario(atual,'data.pkl')
print(carregar_dicionario('data.pkl'))