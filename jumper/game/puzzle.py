import random

# Add the class Puzzle:
class Puzzle:

        def __init__(self): #Initialize the class
                self._words = []
                self._hide_word = []
                self._chosen_word = ''

#Kwadjo
        _words = ['bottle', 'moving', 'outfit', 'wealth', 'latest', 'valley','height', 'adjust', 'powder', 'retire', 'palace', 'marine']
        """This will be the dictionary that defines the word to be used with the game using random."""

#Cooper
        _hide_word = ['_ ','_ ','_ ','_ ','_ ','_']
        """This will replace the current letter with a line until the user correctly guesses the letter"""

#Cooper
        _chosen_word = _words[random.randint[0, 11]]

        # Might be easier to do  self._chosen_word = random.choice(self._words)
        # I believe this will just select a word from the list without needing 
        # to know the range. (Jeremy)

        """This will randomly choose a word from the list using random"""

#Bryan
        _guess = ''
        #Setting a blank value for the guess

        def guess_is_correct(self, letterGuessIn): #Returns true if the letterGuessIn is in the chosen word
                return (letterGuessIn in self._chosen_word)


#Bryan
        def replace_blank(self, letterGuessIn): #Replace all the letters that match the letter guess in the _hide_word
                self._indices = [_index for _index in range(len(self._chosen_word)) if self._chosen_word.startswith(letterGuessIn, _index)] #find the index of each matching letter.
                for _index in self._indices: #replace all the '_' in _hide_word with the guessed letter.
                        self._hide_word[_index]=letterGuessIn 
                return self._hide_word #Return the updated _hide_word with letters added.