''''
Caeser Cypher
Lookup table: [A,B,C, D,...]
Shift letters by 1: [B,C,D, E, ...] (A is now B, B is now C, etc)
bad => cbe
Write function to convert regular string into caeser cyher and another function to do the opposite.
caesarInput(string:str, shift_amount:int) -> str:
caesrDecrypt(string,str, shift_amount:int) -> str:
n = GET number of characters to shift
s = GET string to convert
FOR each character in s
    GET index of character in alphabet
    ADD n to index
    GET character in alphabet at the new index
    REPLACE character in s WITH the new character
END FOR
'''

from typing import Final

alphabet:Final[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryptChar(char:str, shift:int) -> str:
    
    # Putting these here to show that they are only used by the encryptedChar() function.
    def indexOfChar(char:str) -> int:
        return alphabet.index(char)
    
    def charAtIndex(index:int) -> str:
        return alphabet[index if index < 26 else index % 26]
    
    return charAtIndex(indexOfChar(char) + shift) if char != ' ' else ' '

def caesarInput(string_to_encrypt:str, shift:int) -> str:
    # Convert encrypted_string into a list, encrypt each character and return the new list.
    crypted_string = ''.join([encryptChar(char, shift) for char in list(string_to_encrypt.upper())])
    return crypted_string

def caesarDecrypt(string_to_decrypt:str, shift:int) -> str:
    return caesarInput(string_to_decrypt, shift * -1)

input_to_encrypt = input("Enter some text to encrypt: ")
shift = int(input("Enter the amount to shift by (eg 1): "))
#input_to_encrypt = "hello"
#shift = 30

crypted = caesarInput(input_to_encrypt, shift)
print(crypted)
decrypted = caesarDecrypt(crypted, shift)
print(decrypted)

