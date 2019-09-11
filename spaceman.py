import random

#loads a random secret word from words.txt
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word

#Handles all user input with error handling
def user_input(prompt):
    user_input = input(prompt)

    if len(user_input) > 1:
        print('you can only input one letter at a time! ')
    elif user_input.isalpha() == False:
        print("You must use letters only! ")

    return user_input

# creates an array to store the Users correct guesses
def word_init(secret_word):
    return ['_'] * len(secret_word)


def get_correct_index(str, find_char):
    indicies = list()

    for index, char in enumerate(str):
        if char == find_char:
            indicies.append(index)
    
    return indicies

def is_guess_in_word():
    pass

def main(secret_word):
    word_guess = word_init(secret_word)


#test
def test():
    print(secret_word)

    user_input("hello! ")

    word_init(secret_word)



secret_word = load_word()

print('Welcome to the spaceman game! ')
main(secret_word)