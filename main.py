import keywordCypher
import atbash
import polybiussquare

if __name__ == "__main__":

    print("Hello and welcome to my cipher program where"
          "you can encrypt and decrypt your words with well known ciphers")

    while True:
        first_response = input("please type a number to select what option\n\n"
                               "1. encrypt\n"
                               "2. decrypt\n"
                               "3. exit\n")
        if first_response.lower() == "1":

            second_response = input("please type a number to select "
                                    "what cipher\n\n"
                                    "1. keyword\n"
                                    "2. atbash\n"
                                    "3. polybius square\n")
            if second_response.lower() == "1":
                while True:
                    kw_cypher = keywordCypher.KeywordCipher(
                        input("Choose a keyword.\n"))
                    encrypted_word = kw_cypher.encrypt(input(
                        "Choose your word to encrypt. \n"))
                    print("your encrypted word is {}".format(encrypted_word))
                    third_response = input(
                        "do you want to want to encrypt "
                        "another word using the keyword cipher ?\n"
                        "Y/N\n")
                    if third_response.lower() == "y":
                        pass
                    else:
                        break
            elif second_response.lower() == "2":
                while True:
                    ab_cipher = atbash.Atbash()
                    encrypted_word = ab_cipher.encrypt(input(
                        "Choose your word to encrypt. \n"))
                    print("your encrypted word is {}".format(encrypted_word))
                    third_response = input(
                        "do you want to want to encrypt "
                        "another word using the atbash cipher ?\n"
                        "Y/N\n")
                    if third_response.lower() == "y":
                        pass
                    else:
                        break
            elif second_response == "3":
                while True:
                    ps_cipher = polybiussquare.Polybius()
                    encrypted_word = ps_cipher.encrypt(
                        input("Choose your word to encrypt. \n"))
                    print("your encrypted word is {}".format(encrypted_word))
                    third_response = input(
                        "do you want to want to encrypt "
                        "another word using the polybius "
                        "square cipher ?\n"
                        "Y/N\n")
                    if third_response.lower() == "y":
                        pass
                    else:
                        break

        elif first_response.lower() == "2":
            second_response = input(
                "please type a number "
                "to select what cipher to decrypt your word\n\n"
                "1. keyword\n"
                "2. atbash\n"
                "3. polybius square\n")
            if second_response.lower() == "1":
                while True:
                    kw_cypher = keywordCypher.KeywordCipher(
                        input("Choose a keyword.\n"))
                    decrypted_word = kw_cypher.decrypt(
                        input("Type your word to decrypt.\n"))
                    print("your decrypted word is {}".format(decrypted_word))
                    third_response = input(
                        "do you want to want to decrypt "
                        "another word using the keyword cipher?\n"
                        "Y/N\n")
                    if third_response.lower() == "y":
                        pass
                    else:
                        break
            elif second_response.lower() == "2":
                while True:
                    ab_cipher = atbash.Atbash()
                    decrypted_word = ab_cipher.decrypt(
                        input("Choose your word to decrypt. \n"))
                    print("your decrypted word is {}".format(decrypted_word))
                    third_response = input(
                        "do you want to want to decrypt another "
                        "word using the atbash cipher ?\n"
                        "Y/N\n")
                    if third_response.lower() == "y":
                        pass
                    else:
                        break
            elif second_response == "3":
                while True:
                    ps_cipher = polybiussquare.Polybius()
                    decrypted_word = ps_cipher.decrypt(
                        input("Enter your code to decrypt.(No special "
                              "chars) \n"))
                    print("your decrypted word is {}".format(decrypted_word))
                    third_response = input(
                        "do you want to want to decrypt "
                        "another word using the polybius "
                        "square cipher or ?\n"
                        "Y/N\n")
                    if third_response.lower() == "y":
                        pass
                    else:
                        break
        elif first_response == "3":
            break
        else:
            print("please choose one of the options 1, 2 or 3")
