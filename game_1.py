def check_print_words(word, letter):
    """
    number_of_attempts, word -> str , number_of_letter->
    """
    all_letters='abcdefghijklmnopqrstuvwxyz'
    number_of_attempts= 8
    for i in range(len(word)):
        print(f'You have {number_of_attempts} guesses left')
        print(f'Available letters: {all_letters}')
        letter=input('Please guess a letter: ')
