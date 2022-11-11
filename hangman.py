"""Reading file"""
import random
import doctest

def load_words(filename:str)->str:
    """
    Args:
        filename(str): path to file
    returns random word from the file 
    >>> load_words(9)
    """
    if isinstance(filename, str) is True:
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

if __name__=="__main__":
    doctest.testmod()
