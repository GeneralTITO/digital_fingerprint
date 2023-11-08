from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Chave secreta para a criptografia AES (deve ter 16, 24 ou 32 bytes)
chave_secreta = b'janela'

# Mensagem a ser criptografada
mensagem = "Esta é uma mensagem secreta que será criptografada."

# Inicialize o objeto de cifra AES
cipher = AES.new(chave_secreta, AES.MODE_EAX)

# Criptografe a mensagem
mensagem_cifrada, tag = cipher.encrypt_and_digest(mensagem.encode('utf-8'))

print("Mensagem cifrada:", mensagem_cifrada)

# Inicialize outro objeto de cifra AES para descriptografar
cipher2 = AES.new(chave_secreta, AES.MODE_EAX, nonce=cipher.nonce)

# Descriptografe a mensagem
mensagem_decifrada = cipher2.decrypt(mensagem_cifrada)

print("Mensagem decifrada:", mensagem_decifrada.decode('utf-8'))