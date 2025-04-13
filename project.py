import random


def main():
    print("This program will generate a password for you.")
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

    print("===================================")
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")

    print("===================================")


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
