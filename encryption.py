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

