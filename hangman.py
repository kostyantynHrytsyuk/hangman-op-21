"""Reading file"""
import random


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
    # checking whether it is only one character and a letter
    if isinstance(letter, str) and len(letter) == 1 and 97 <= ord(letter.lower()) <= 122:
        # checks if letter in alphabet
        if letter.lower() not in alphabet:
            return "Oops"
        #chech if letter in word
        return letter.lower() in word.lower()
    return False


def check_print_words(word):
    """ Check let in word and return output

    Args:
        word (str): random word

    Returns:
        guessed_word(str): if player guess th let it will be shown for a player, also player will see tha letters that are left
    """
    all_letters='abcdefghijklmnopqrstuvwxyz'
    number_of_attempts= 8
    new_lst=[]
    change= len(word)
    # creating a empty line
    for j in range(len(word)):
        new_lst.append('_')
    #cheching condiotion for win or loss
    while number_of_attempts>0 and change>0:
        print(f'You have {number_of_attempts} guesses left')
        print(f'Available letters: {all_letters}')
        #player inputing his letter
        letter=input('Please guess a letter: ')
        #checking if its right or nor
        if_letter_in_alphabet= check(letter, word, all_letters)
        #if letter is in our word
        if if_letter_in_alphabet==True:
            for k in range(len(word)):
                if word[k]==letter:
                    change-=1
                    new_lst.pop(k)
                    new_lst.insert(k, letter)
            finnal_lst=''.join(new_lst)
            print(f'Good guess: {finnal_lst}')
        #if letter is not in our word
        elif if_letter_in_alphabet==False:
            number_of_attempts-=1
            finnal_lst=''.join(new_lst)
            print(f'Oops! That letter is not in my word: {finnal_lst}')
        #if letter was used previuosly
        elif if_letter_in_alphabet =='Oops':
            finnal_lst=''.join(new_lst)
            print(f'Oops! You*ve already guessed that letter: {finnal_lst}')
        #if is not a letter or lenght is more than one
        else:
            number_of_attempts-=1
            finnal_lst=''.join(new_lst)
            print(f'Oops! This is not a letter: {finnal_lst}')
        all_letters=all_letters.replace(letter, '')
        print('------------')
    #win combination
    if change==0:
        return 'Congratulations, you won!'
    #loss combination
    return 'You lose('


def load_words(filename:str)->str:
    """
    Reading file
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

def hangman():
    """The game

    Args:
        filename (str): the file that needs to be readed
    Returns:
        The hangman game
    """
    check_print_words(load_words("words.txt"))


if __name__=="__main__":
    print(hangman())
