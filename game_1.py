def check_print_words(word, letter):
    """
    word, letter -> str
    """
    all_letters='abcdefghijklmnopqrstuvwxyz'
    number_of_attempts= 8
    for i in range(len(word)):
        print(f'You have {number_of_attempts} guesses left')
        print(f'Available letters: {all_letters}')
        letter=input('Please guess a letter: ')
        if_letter_in_alphabet= check(letter)
        if if_letter_in_alphabet==True:

        else:
            number_of_attempts-=1
            print(f('Oops!'))
