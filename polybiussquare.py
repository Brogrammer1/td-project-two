from ciphers import Cipher


class Polybius(Cipher):
    """Polybius cipher class used for encrypting words according to the
        polybius cipher
        """
    keys = list("abcdefghijklmnopqrstuvwxyz")

    values2 = [11, 12, 13, 14, 15,
               21, 22, 23, 24, 25, 26,
               31, 32, 33, 34, 35,
               41, 42, 43, 44, 45,
               51, 52, 53, 54, 55]
    code = dict(zip(keys, values2))

    def encrypt(self, text):
        """
        accepts a string and then it encrypts the string according to the
        class cipher
        and then returns a encrypted string
        """
        word = []
        l_case_text = text.lower()
        for letter in l_case_text:
            if letter in self.keys:
                word.append(str(self.code[letter]))
            else:
                word.append(letter)
        return "".join(word)

    def decrypt(self, text):
        """
        accepts a string and then it decrypts the string according to the
        class cipher
        and then returns a decrypted string
        """
        return_word = []
        first_list = text.split()
        for blocks in first_list:
            answer = [blocks[i:i + 2] for i in range(0, len(blocks), 2)]
            for number in answer:
                for key, value in self.code.items():
                    if int(number) == value:
                        return_word.append(key)
            return_word.append(" ")

        return "".join(return_word).upper()
