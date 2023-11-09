'''
Perform symetic encryption in order below:
Find library to provide acess to AES256 algorithm
Create and save your AES256 key
Create string to test encryption
Perform AES256 symetric encryption on the data to get ciphir text.
Use AES256 symetri decryption to get original text.
Use assert to check if decrypted data is the same as original text.
'''

# Note: cryptography is newer than pycrypto and more secure.
# pip install cryptography

from cryptography.fernet import Fernet

AES256key = Fernet.generate_key()

# 'b' is required as data is expected to be in bytes.
test_string = b"text to encrypt"

test_string_encrypted = Fernet(AES256key).encrypt(test_string)
test_string_decrypted = Fernet(AES256key).decrypt(test_string_encrypted)

assert(test_string_decrypted == test_string)


'''
Perform a digital signature operation in the order below:
Generate a RSA256 key pair(private and public keys)
Use the private key to sign an input message.
Use a public key to verify the signature
Describe in words how to get around not being able to sign a very large message.
'''

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


private_key = rsa.generate_private_key(
    public_exponent=65537, 
    key_size=2048,         
    backend=default_backend()
)

public_key = private_key.public_key()

message = b"Message to be signed"
corrupted_message = b"Message to be signed (corrupted)."

# Sign the message using the private key
signature = private_key.sign(message, padding.PKCS1v15(), hashes.SHA384())

try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA384()
    )  
    print('(1) Signature is correct.')  
except Exception as e:
    print('(1) Message is corrupted.')
    print(e)

try:
    public_key.verify(
        signature,
        corrupted_message,
        padding.PKCS1v15(),
        hashes.SHA384()
    )  
    print('(2) Signature is correct.')  
except Exception as e:
    print('(2) Message is corrupted.')
    print(e)

print("All done.")

'''
You can get around not being able to sign a large message by hashing it first, as hashes are of
a fixed length.
'''