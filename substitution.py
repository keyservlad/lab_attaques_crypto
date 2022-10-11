# author Arnaud Guilhamat guia2612
# date 2022-10-10

import binascii
import secrets
from binascii import hexlify
import textwrap


print("***  question 8 ")


def freq_text(clear_text: str) -> list:
    freq = {}
    for letter in clear_text:
        if freq.get(letter):
            freq[letter] += 1
        else:
            freq[letter] = 1
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)


print("*** question 9")


def freq_cipher(encrypted_text: bytes) -> list:
    freq = {}
    for index in range(len(encrypted_text)):
        if index % 2 == 0:
            letter = encrypted_text[index:index + 2]
            if freq.get(letter):
                freq[letter] += 1
            else:
                freq[letter] = 1
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)


print("*** question 11")


def guess_clear_text(encrypted_text: bytes, decryption_key: dict) -> str:
    clear_text = ""
    for index in range(len(encrypted_text)):
        if index % 2 == 0:
            letter = encrypted_text[index:index + 2]
            if decryption_key.get(letter):
                clear_text += decryption_key[letter]
            else:
                clear_text += "%s" %letter
                # clear_text += "*" # On peut aussi ajouter un caractère * pour indiquer que le caractère n'a pas été trouvé (plus lisible)
    return clear_text


def build_decryption_key(freq_clear_text: list, freq_cipher_text: list, key_size: int):
    decryption_key = {}
    
    for index in range(key_size):
        decryption_key[freq_cipher_text[index][0]] = freq_clear_text[index][0]

    return decryption_key


if __name__ == '__main__':
    with open("cipher_text_1.bin", 'br') as f:
        cipher_text_1 = f.read()
    with open("cipher_text_2.bin", 'br') as f:
        cipher_text_2 = f.read()
    with open("text_hugo.txt", 'r') as f:
        clear_text_hugo = f.read()

    print("*** question 8 ")
    freq_hugo = freq_text(clear_text_hugo)
    print("freq_hugo: %s" % freq_hugo)

    print("*** question 9")
    freq_cipher_text_1 = freq_cipher(cipher_text_1)
    print("freq_cipher_text_1: %s" % freq_cipher_text_1)
    # for index in range(len(freq_cipher_text_1)):
    #     print("freq_cipher_text_1[%d]: %s" % (index, freq_cipher_text_1[index]))
        # print(binascii.hexlify(freq_cipher_text_1[index][0]))

    print("*** question 11")
    decryption_key = build_decryption_key(freq_hugo, freq_cipher_text_1, 15)
    print("decryption_key: %s" % decryption_key)
    clear_text_1 = guess_clear_text(cipher_text_1, decryption_key)
    print("clear_text_1: %s" % clear_text_1)

    print("*** question 12")
    freq_cipher_text_2 = freq_cipher(cipher_text_2)
    decryption_key = build_decryption_key(
        freq_hugo, freq_cipher_text_2, key_size=15)
    print("decryption_key: %s" % decryption_key)
    clear_text_2 = guess_clear_text(cipher_text_2, decryption_key)
    print("clear_text_2: %s" % clear_text_2)

    print("*** question 13")
    indice = "Anton Voyl n'arrivait pas à dormir"

    decryption_key = {}
    for index in range(len(indice)):
        bin_char = cipher_text_2[2 * index: 2 * index + 2]
        decryption_key[bin_char] = indice[index]

    clear_text_2 = guess_clear_text(cipher_text_2, decryption_key)
    print("clear_text_2: %s" % clear_text_2)
