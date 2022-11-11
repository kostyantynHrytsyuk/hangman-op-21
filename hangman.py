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
    >>> check("z", "alphabet", "abcdefghijklmnopqrstuvwxyz")
    False
    >>> check("aaa", "alphabet", "abcdefghijklmnopqrstuvwxyz")

    >>> check('7', 'split', 'abcdefghijklmnopqrstuvwxyz')

    """
    # checking whether it is only one character
    if len(letter) == 1 and isinstance(letter, str):
        # checking whether it is in English alphabet 
        if 97 <= ord(letter) <= 122:
            if letter not in alphabet:
                return "Oops"
            else:
                # checking whether it is in a guessed word
                if letter in word:
                    return True
                return False




 