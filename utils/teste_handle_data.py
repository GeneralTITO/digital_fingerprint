from data import pessoas_cadastradas
from handle_data import save, get_data

new_person = ["karina", "99199129391923", "enurgosfgm4ng2n4g3jnp34r3245m354"]


save(new_person=new_person)
print(get_data())

