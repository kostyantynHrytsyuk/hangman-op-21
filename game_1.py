def check_print_words(word):
    """
    word-> str
    """
    all_letters='abcdefghijklmnopqrstuvwxyz'
    number_of_attempts= 8
    new_str=''
    for j in range(len(word)):
        new_str+='_'
    for i in range(len(word)):
        set_of_letters= set(all_letters)
        print(f'You have {number_of_attempts} guesses left')
        print(f'Available letters: {all_letters}')
        letter=input('Please guess a letter: ')
        if_letter_in_alphabet= check(letter, word, all_letters)
        if if_letter_in_alphabet==True:
            print(f'Good guess: {new_str}')
        elif if_letter_in_alphabet==False:
            number_of_attempts-=1
            print(f'Oops! That letter is not in my word: {new_str}')
        elif if_letter_in_alphabet=='Oops':
            number_of_attempts-=1
            print(f'Oops! You*ve already guessed that letter: {new_str}')
        else:
            number_of_attempts-=1
            print(f'Oops! This is not a letter: {new_str}')
