def check_print_words(word):
    """
    word-> str
    """
    all_letters='abcdefghijklmnopqrstuvwxyz'
    number_of_attempts= 8
    new_lst=[]
    change= len(word)
    for j in range(len(word)):
        new_lst.append('_')
    while number_of_attempts>0 and change>0:
        print(f'You have {number_of_attempts} guesses left')
        print(f'Available letters: {all_letters}')
        letter=input('Please guess a letter: ')
        if_letter_in_alphabet= check(letter, word, all_letters)
        if if_letter_in_alphabet==True:    
            for k in range(len(word)):
                if word[k]==letter:
                    change-=1
                    new_lst.pop(k)
                    new_lst.insert(k, letter)
            finnal_lst=''.join(new_lst)
            print(f'Good guess: {finnal_lst}')
        elif if_letter_in_alphabet==False:
            number_of_attempts-=1
            finnal_lst=''.join(new_lst)
            print(f'Oops! That letter is not in my word: {finnal_lst}')
        elif if_letter_in_alphabet =='Oops':
            finnal_lst=''.join(new_lst)
            print(f'Oops! You*ve already guessed that letter: {finnal_lst}')
        else:
            number_of_attempts-=1
            finnal_lst=''.join(new_lst)
            print(f'Oops! This is not a letter: {finnal_lst}')
        all_letters=all_letters.replace(letter, '')
        print('------------')
    if change==0:
        return 'Congratulations, you won!'
    else:
        return 'You lose('
