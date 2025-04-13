import random
import csv
import sys


def main():
    print("\nThis program will generate a password for you.\n")
    substitutions = {
        "a": "4",
        "b": "8",
        "c": "(",
        "d": "|)",
        "e": "3",
        "g": "9",
        "h": "#",
        "i": "1",
        "j": "_|",
        "k": "|<",
        "l": "|",
        "o": "0",
        "q": "9",
        "s": "5",
        "t": "7",
        "u": "µ",
        "w": "vv",
        "x": "%",
        "y": "¥",
        "z": "2",
    }

    while True:
        wordsFromUser = input(
            "Enter at least 3 words to use for password (separated with spaces): "
        )

        wordsList = wordsFromUser.split()
        validatedWords = validateUserInput(wordsList)

        if validatedWords is not None:
            break

    passwords = generatePasswords(validatedWords, substitutions)

    print("\n\n===================================\n")
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")

    print("\n===================================\n")

    save = input("\nDo you want to save your passwords to a file? (y/n): ")

    if save.lower() == "y":
        addedPasswords = []

        while len(addedPasswords) < 3:
            passwordIndex = input("\nEnter the password number to save (1-3) or 'q' to quit: ")

            if passwordIndex.lower() == 'q':
                print("Exiting password saving.")
                break

            try:
                passwordIndex = int(passwordIndex)

                if passwordIndex < 1 or passwordIndex > 3:
                    print("Invalid password number. Please enter 1, 2, or 3.\n")
                    continue

                if passwordIndex in addedPasswords:
                    print("This password has already been saved.\n")
                    continue

                addedPasswords.append(passwordIndex)
                passwordKey = ""
                
                while True:
                    passwordKey = input("\nEnter the name of the password: ")
                    if passwordKey == "":
                        print("Password name cannot be empty. Please enter a valid name.\n")

                    else:
                        break

                passwordDict = {passwordKey: passwords[passwordIndex - 1]}

                with open("passwords.csv", "a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([passwordKey, passwords[passwordIndex - 1]])
                    print(f"Password for {passwordKey} saved successfully!\n")

                if len(addedPasswords) == 3:
                    print("All passwords saved.\n")

            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 3.\n")

    elif save.lower() == "n":
        print("Passwords not saved.\n")

    else:
        print("Invalid input. Passwords not saved.\n")

    print("Have a nice day ahead!\n")
    sys.exit(0)


def validateUserInput(words):
    if len(words) >= 3:
        return words

    else:
        print(
            f"Too few words! You need at least {3 - len(words)} more words to generate passwords.\n"
        )

        return None


def generatePasswords(words, substitutions):
    passwords = []

    for i in range(3):
        selectedWords = random.sample(words, 3)
        scrambledWords = []

        for word in selectedWords:
            if random.choice([True, False]):
                scrambledWord = scrambleWord(word, substitutions)

            else:
                scrambledWord = word

            scrambledWord = scrambledWord.upper()
            scrambledWords.append(scrambledWord)

        randomNumber = str(random.randint(10, 99))
        password = "".join(scrambledWords) + randomNumber
        passwords.append(password)

    return passwords


def scrambleWord(word, substitutions):
    scrambled = ""

    for char in word:
        if char.lower() in substitutions:
            scrambled += substitutions[char.lower()]

        else:
            scrambled += char

    return scrambled


if __name__ == "__main__":
    main()
