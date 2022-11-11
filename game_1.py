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
        print(f'You have {number_of_attempts} guesses left')
        print(f'Available letters: {all_letters}')
        letter=input('Please guess a letter: ')
        if_letter_in_alphabet= check(letter, word, all_letters)
        if if_letter_in_alphabet==True:    
            word_SP=word.split('')
            for o,el in word_SP:
                if el==letter:
                    new_str.replace(new_str[o],letter)
            print(f'Good guess: {new_str}')
        elif if_letter_in_alphabet==False:
            number_of_attempts-=1
            print(f'Oops! That letter is not in my word: {new_str}')
        elif if_letter_in_alphabet =='Oops':
            number_of_attempts-=1
            print(f'Oops! You*ve already guessed that letter: {new_str}')
        else:
            number_of_attempts-=1
            print(f'Oops! This is not a letter: {new_str}')
