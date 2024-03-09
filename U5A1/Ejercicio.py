import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def load_public_key(filename):
    with open(filename, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

def load_private_key(filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def encrypt_file(public_key, filename):
    with open(filename, 'rb') as file:
        plaintext = file.read()
        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    return ciphertext

def decrypt_file(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

def send_file(socket, ciphertext):
    socket.sendall(ciphertext)

def receive_file(socket):
    data = b""
    while True:
        chunk = socket.recv(1024)
        if not chunk:
            break
        data += chunk
    return data

# Configuración de la comunicación
host = '127.0.0.1'  # Cambiar a la dirección IP del nodo B
port = 12345  # Puerto de comunicación

# Cargar claves
public_key_b = load_public_key('clave_publica_b.pem')
private_key_b = load_private_key('clave_privada_b.pem')

# Crear socket y establecer conexión
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    
    # Encriptar y enviar archivo desde A a B
    ciphertext = encrypt_file(public_key_b, 'archivo.txt')
    send_file(s, ciphertext)

    # Recibir archivo encriptado en B
    received_ciphertext = receive_file(s)
    
    # Descifrar archivo en B
    decrypted_data = decrypt_file(private_key_b, received_ciphertext)

    # Guardar el archivo descifrado
    with open('archivo_recibido.txt', 'wb') as file:
        file.write(decrypted_data)