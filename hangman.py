#import random and wordlist to pick from
import random
from hangmanword import wordlist

#pick single word from wordlist
def chooseword(wordlist):
    word=random.choice(wordlist)
    while " " in word or "-" in word:
        word=random.choice(wordlist)
    return word.upper()

def hangman():
    #initialize word, letter bank, guessedletters set and word outline
    word=chooseword(wordlist)
    letters={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    lives=7
    guessedletters=set()
    template=list(len(word)*'-')
    #guess validation and game continuation
    while lives>0 and '-' in template: #continue to prompt for letters while lives remaining
        guess=''
        print(*template, sep='') #print template
        print("You have "+str(lives)+" remaining") #print remaining lives
        if len(guessedletters)>0: #skip if first guess
            print(f"Your guessed letters include: {guessedletters}")
        while guess not in letters: #validate user input for valid guess
            guess=input("Guess a letter: ").upper()
            while guess in guessedletters: #validate user input for unused letter
                print("You have already guessed that letter")
                print(f"Your guessed letters include: {guessedletters}")
                guess = input("Guess a letter: ").upper()
            if guess not in letters:
                print("That is not a valid letter, please try again")
        #test for correctness
        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if guess==word[i]:
                    template[i]=guess
        else:
            print(f"Sorry, {guess} is not in your word.")
            lives-=1
        guessedletters.add(guess)
        print('\n')
    if '-' not in template: #win message
        print('Congratulations, you guessed right!')
    else: #loss message
        print("Sorry, you have lost...")
    print(f"The word was {word}. Thanks for playing!")

hangman()