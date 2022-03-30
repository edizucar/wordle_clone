

import random
def isAlpha(string):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for char in string:
        if char not in alpha:
            return False
    return True

def is5letter(string):
    return len(string) == 5


def generate_5_letter_alpha_words():
    with open("words.txt","r") as words_file:

        words = filter(lambda s: isAlpha(s) and is5letter(s),
            {line.strip().lower() for line in words_file})

        
    with open("words_alpha.txt") as words_alpha_file:
        words_alpha = filter(lambda s: isAlpha(s) and is5letter(s),
            {line.strip().lower() for line in words_alpha_file})

    #Lets just use words_alpha

    return words_alpha



def isValidInput(string,words):
    if not is5letter(string):
        return print("That is not a 5 letter word!")
    if not isAlpha(string):
        return print("Only enter alphabetic characters")
    if string not in words:
        return print("That word is not in the english dictionary")
    return True


def getWordFromUser(words):
    usr_input = input("Enter 5 Letter Word : ")
    while not isValidInput(usr_input,words):
        usr_input = input("Enter 5 Letter Word : ")
    return usr_input

def compareWords(word,guess):
    string = ""
    for real_char,guess_char in zip(word,guess):
        if real_char == guess_char:
            string += "🟩"
        elif guess_char in word:
            string += "🟨"
        else:
            string += "⬛"

    formatted_guess = " ".join(list(guess)) 
    print(f"Guess :   { formatted_guess }")
    print(f"Result : {string}")

    return


def main():
    words = list(generate_5_letter_alpha_words())
    word = random.choice(words)
    #print(f" Cheat : {word}")
    print("    ---- Wordle ----    ")
    for i in range(1,7):
        print(f"   > Guess Number : {i}")
        usr_input = getWordFromUser(words)
        if usr_input != word:
            compareWords(word,usr_input)
        else:
            print("Correct! You Win!")
            break
    print("The correct answer was " + word)


if __name__ == "__main__":
    main()


