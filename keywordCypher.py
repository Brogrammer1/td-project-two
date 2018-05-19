from ciphers import Cipher


class KeywordCipher(Cipher):
    """Keyword cipher class used for encrypting words according to the
    keyword cipher
    """
    keys = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    kyword = None
    kyword_list = []
    kyword_list2 = []

    def __init__(self, keyword):
        for letter in self.keys:
            if letter not in keyword.upper():
                self.kyword_list.append(letter)

        for char in keyword.upper():
            if char not in self.kyword_list2:
                self.kyword_list2.append(char)

        self.kyword = "".join(self.kyword_list2) + "".join(self.kyword_list)
        self.values = list(self.kyword)
        self.cipher_code = dict(zip(self.keys, self.values))

    def encrypt(self, text):
        """
        accepts a string and then it encrypts the string according to the
        class cipher
        and then returns a encrypted string
        """
        word = []
        for letter in text:
            if letter.upper() in self.keys:
                word.append(self.cipher_code[letter.upper()])
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
            if letter in self.cipher_code.values():
                for key, value in self.cipher_code.items():
                    if letter.upper() == value:
                        word.append(key)
            else:
                word.append(letter)

        return "".join(word)
