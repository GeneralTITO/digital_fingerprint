from handle_data import *

new_person1 = ["messi", "123391923", "enhnghnhn245m354"]
new_person2 = ["ronaldinho", "09876391923", "gfhnfghnfghn54"]
new_person3 = ["cr7", "9765432", "345tgdfghdfgh2n4g3jnp34r3245m354"]
new_person4 = ["ronaldo", "87654334567", "9lokijhgvfnp34r3245m354"]
new_person5 = ["chapolim", "65454334567", "nyththgvfnp34r3245m354"]

list_people = [new_person1, new_person2, new_person3, new_person4]


lista_carregada = carregar_pessoas()
lista_carregada.append(new_person5)
salvar_pessoas(lista_pessoas=lista_carregada)
nova_lista_carregada = carregar_pessoas()
print(nova_lista_carregada)
