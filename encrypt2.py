import secrets

# mono alphabetic cipher 65 - 90
def ma_cipher_right(text, shift):
    encrypted = []
    for i in text:
        if i.isspace(): # check if its a whitespace
            continue
        num = ord(i.upper())
        if 65 <= num <= 90:
            x = chr((num - 65 + shift) % 26 + 65) # shifts to the right
            encrypted.append(x)
        else:
            print("Invalid Character")
        
    return(''.join(encrypted))


def ma_cipher_left(text, shift):
    decrypted = []
    for i in text:
        if i.isspace():
            continue
        num = ord(i.upper())
        if 65 <= num <= 90:
            x = chr((num - 65 - shift) % 26 + 65)  # Decryption
        else:
            print("Invalid String")
            return None  # Return None for an invalid string
        decrypted.append(x)
    return ''.join(decrypted)


def vig_cipher(text, e5d):
    key = ma_cipher_left(e5d, 8)
    # make key repeat to the length of the text
    key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    cipher_text = ''
    
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            num = ord(char.upper())
            if i % 2 == 0:
                cipher_text += chr((num + shift - ord('A')) % 26 + ord('A'))
            else:
                # if odd
                cipher_text += chr((num - shift - ord('A')) % 26 + ord('A'))
    return cipher_text

def vig_decipher(cipher_text, e5d):
    key = ma_cipher_left(e5d, 8)
    
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
    decrypted_text = ''
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            num = ord(char.upper())
            if i % 2 == 0:
                decrypted_text += chr((num - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((num + shift - ord('A')) % 26 + ord('A'))
    
    return decrypted_text


def generate_random_key(length):
    return secrets.token_bytes(length)

def vern_cipher(plaintext):
    key = generate_random_key(len(plaintext))

    # Perform XOR operation for each character in the plaintext and key
    cipher_text = ''.join(chr(ord(p) ^ k) for p, k in zip(plaintext, key))

    return cipher_text, key

def vern_decipher(cipher_text, key):
    return ''.join(chr(ord(c) ^ k) for c, k in zip(cipher_text, key))




# =====MAIN

string = "i have a crush on macey"
string = string.replace(" ", "")

print("Original:", string)
enc = ma_cipher_left(string, 5)
print("Encrpted:", enc)
print("Decrypted:", ma_cipher_right(enc, 5))

print("\nVignere Cipher")
venc = vig_cipher(string, string[-5:])
encr = vig_cipher(string, venc)
print('Encryptd:', encr)
print('Decrypted:', vig_decipher(encr, venc))

print("\nVernam Cipher")
vernenc, vern_key = vern_cipher(string)
print("Encryptd:", vernenc)
verndec = vern_decipher(vernenc, vern_key)
print("Decrypted:", verndec)
print('Key =', vern_key)