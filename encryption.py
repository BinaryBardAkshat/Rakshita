from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def encrypt_message(message, key):
    message_bytes = message.encode('utf-8')
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message_bytes) + padder.finalize()

    iv = b'0123456789abcdef'
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(ct).decode('utf-8')

def decrypt_message(encrypted_message, key):
    ct = base64.b64decode(encrypted_message.encode('utf-8'))
    iv = b'0123456789abcdef'
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ct) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data.decode('utf-8')

# Example usage:
key = b'Sixteen byte key'
message = "*************"

# Encrypt message
encrypted_message = encrypt_message(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt message
decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted message:", decrypted_message)
