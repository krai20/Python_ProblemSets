import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """v
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print
    "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print
    "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()
word = choose_word(wordlist)
print 'The word has', len(word), 'letters'
guess_word = '_' * len(word)
letters = 'abcdefghijklmnopqrsrtuvwxyz'
attempts = 8

while attempts in range(1, 10) :
    guess = raw_input('Please guess a letter: ')
    for i,c in enumerate(word):
        if guess == c:
            guess_word = guess_word[:i] + guess + guess_word[i+1:]
            print 'Good Guess'
    if guess not in word:
        print 'incorrect guess'
    if '_' not in guess_word: break
    attempts -= 1
    letters = letters.replace(guess,'')

    print ' '.join(guess_word)

    print 'Remaining number of attempts are', attempts

    print 'Remaining letters are:', letters

if '_' not in guess_word:    
    print 'Congratulations, you have guessed the word correctly:', guess_word
else:
    print 'Sorry, you have lost, the correct answer is -', word