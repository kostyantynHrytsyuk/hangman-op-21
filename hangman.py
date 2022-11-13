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
    return None






 