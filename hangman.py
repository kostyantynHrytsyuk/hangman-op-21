def check(letter, word, alphabet):
    """
    Check whether the given letter is string and is in alphabet.
    If the given letter is not a string the function should return None.
    If letter not in alphabet, it means that player has already
    chosen that letter and the function should return "Oops". If the given
    letter is in guessed word the function should return True. Else the
    function should return False.
    >>> check('a', 'heart', 'abcdefghijklmnopqrstuvwxyz')
    True
    >>> check('W', 'Wonderland', 'abcdefghijklmnopqrstuvwxyz')
    True
    >>> check('m', 'bridge', 'abcdefghijklmnopqrstuvwxyz')
    False
    >>> check('e', 'economy', 'abcdijklmnopqrstuvwxyz')
    'Oops'
    >>> check(7, 'yellow', 'abcklmnoprsvwxyz')
    False
    """
    # checking whether it is only one character
    if isinstance(letter, str) and \
    (65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122):
        if len(letter) == 1:
            letter = letter.lower()
            word = word.lower()
            if letter not in alphabet:
                return "Oops"
            return letter in word
    return False

"""Reading file"""
import random

def load_words(filename:str)->str:
    """
    Args:
        filename(str): path to file
    returns random word from the file 
    >>> load_words(9)
    """
    if not isinstance(filename, str):
        return ''
    with open(filename, 'r', encoding='utf-8') as file:
        all_words=file.readlines()
    massive=all_words[0].split(' ')
    result=random.randint(0, len(massive))
    print(f"""
Loading word list from file...
{len(massive)} words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is {len(massive[result])} letters long.
""")
    return massive[result]


 