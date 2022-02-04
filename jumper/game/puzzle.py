import random

# Add the class Puzzle:
class Puzzle:

#Kwadjo
#   Add the  Attribute with the following - _words = [
#         'bottle', 'moving', 'outfit', 'wealth', 'latest', 'valley',
#         'height', 'adjust', 'powder', 'retire', 'palace', 'marine'
#         ]
        """This will be the dictionary that defines the word to be used with the game using random."""

#Cooper
#      _hide_word = ['_ ','_ ','_ ','_ ','_ ','_']
        """This will replace the current letter with a line until the user correctly guesses the letter"""

#Cooper
#      _chosen_word = _words[random.randint[0, 11]]

        # Might be easier to do  self._chosen_word = random.choice(self._words)
        # I believe this will just select a word from the list without needing 
        # to know the range. (Jeremy)

        """This will randomly choose a word from the list using random"""

#Bryan
#      _guess = ''
        """Setting a blank value for the guess"""

#Bryan
#     - Add method replace_blank()
        """Based on the input user it will check to see if the letter is in the word."""