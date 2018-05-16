from ciphers import Cipher


class Atbash(Cipher):
    keys = list("abcdefghijklmnopqrstuvwxyz")
    values = keys[::-1]
    cipher_code = dict(zip(keys, values))

    def encrypt(self, text):
        word = []
        for letter in text:
            if letter in self.keys:
                word.append(self.cipher_code[letter])
            else:
                word.append(letter)
        return "".join(word)

    def decrypt(self, text):
        word = []
        for letter in text:
            if letter in self.keys:
                word.append(self.cipher_code[letter])
            else:
                word.append(letter)
        return "".join(word)
