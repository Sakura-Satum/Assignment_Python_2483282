import re


def get_content(choice):
    ''' Get string "tree" or "value" as input and return tree_list or value list '''
    # test purpose
    if choice == 'test':
        file = 'input_test_1.txt'
        choice = 'trees'
    # test purpose
    elif choice == 'test2':
        file = 'input_test_2.txt'
        choice = 'trees'
    # test purpose
    elif choice == 'test3':
        file = 'input_test_3.txt'
        choice = 'trees'
    # required list
    elif choice == 'trees':
        file = 'trees.txt'

    if choice == 'trees':
        # read file
        with open(file) as file:
            trees_file = file.read()
            trees_list = trees_file.split('\n')

            # split name in to words
            final_list = {}
            for tree in trees_list:
                checking_words = re.split(' |-', tree.upper())
                for i in range(len(checking_words)):
                    # Remove special characters from word
                    checking_words[i] = re.sub(r'[^a-zA-Z]', '', checking_words[i]).upper()
                final_list[tree] = checking_words

        return final_list

    else:
        with open('values.txt') as file:
            alpha_val_file = file.read()

            # keep only one space
            letter_value = alpha_val_file.replace("  ", " ")
            # Converting value.txt to dictionary
            letter_value = dict((x.strip(), int(y.strip()))
                                for x, y in (element.split(' ')
                                             for element in letter_value.split('\n')))

        return letter_value


def assign_values():
    ''' Assigning position and common/uncommon value to letters of tree names and return
     dictionary - {tree_name:(letter,value)}  '''

    # for Testing
    # trees = get_content('test3')
    # trees = get_content('test2')
    # trees = get_content('test3')
    trees = get_content('trees')
    value_of_letter = get_content('value')
    word_letter_value = {}
    for key in trees:
        words = trees[key]
        letter_val = ()
        for word in words:
            # first letter of a word is 0
            letter_val += (word[0], 0)
            last_letter = word[len(word) - 1]

            # If the letter is first nor last letter position value + letter value
            for i in range(1, len(word) - 1):
                value = 0
                if i < 3:
                    value += i
                else:
                    value += 3
                value += value_of_letter[word[i]]
                letter_val += (word[i], value)
            # last letter of a word
            if last_letter == 'E':
                letter_val += (last_letter, 20)
            else:
                letter_val += (last_letter, 5)

        word_letter_value[key] = letter_val

    return word_letter_value


def make_abbry(trees_list):
    ''' brake abbreviation  and return abbreviation dictionary - {tree_name [(Abbreviation,value)]} '''
    clear_list = {}

    for tree in trees_list:
        word = trees_list[tree]
        abr_list = []

        for i in range(0, len(word), 2):
            for j in range(i + 2, len(word), 2):
                for k in range(j + 2, len(word), 2):
                    if i == 0:
                        abr = word[i] + word[j] + word[k]
                        value = word[i + 1] + word[j + 1] + word[k + 1]
                        abr_list.append((abr, value))

        clear_list[tree] = abr_list[:]

    return clear_list
