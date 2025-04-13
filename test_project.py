from project import validateUserInput, generatePasswords, scrambleWord


def test_validateUserInput():
    assert validateUserInput(["word1", "word2", "word3"]) == ["word1", "word2", "word3"]

    assert validateUserInput(["word1", "word2"]) is None
    assert validateUserInput([]) is None


def test_scrambleWord():
    substitutions = {
        "a": "@",
        "b": "8",
        "c": "(",
    }

    assert scrambleWord("abc", substitutions) == "@8("
    assert scrambleWord("ABC", substitutions) == "@8("
    assert scrambleWord("abcdef", substitutions) == "@8(def"


def test_generatePasswords():
    words = ["foo", "bar", "buz", "qux"]
    substitutions = {"a": "@", "b": "8", "e": "3", "o": "0", "t": "7", "z": "2"}

    passwords = generatePasswords(words, substitutions)
    assert len(passwords) == 3
