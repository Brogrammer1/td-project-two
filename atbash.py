from ciphers import Cipher


class Atbash(Cipher):
    """Atbash cipher class used for encrypting words according to the
    Atbash cipher
    """
    keys = list("abcdefghijklmnopqrstuvwxyz")
    values = keys[::-1]
    cipher_code = dict(zip(keys, values))

    def encrypt(self, text):
        """
        accepts a string and then it encrypts the string according to the
        class cipher
        and then returns a encrypted string
        """
        word = []
        for letter in text:
            if letter in self.keys:
                word.append(self.cipher_code[letter])
            else:
                word.append(letter)
        return "".join(word)

    def decrypt(self, text):
        """
        accepts a string and then it decrypts the string according to the
        class cipher
        and then returns a decrypted string
        """
        word = []
        for letter in text:
            if letter in self.keys:
                word.append(self.cipher_code[letter])
            else:
                word.append(letter)
        return "".join(word)
