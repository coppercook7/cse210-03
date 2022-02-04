
import random
from game.glider import glider




list = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
words = random.choice(list).upper()


class Jumper:
    

    def __init__(self):
      self.word = words
      self.guess = ""
      self.word = [self.words.word(self)]
      self.reveal = list(len(self.word)*'_')
      self.lives = 3
      self.won = False
      self.lose = False

    def letter_check(self, letter, word):
       print("We need something here to check the letter")




    def show(self):
      #shows the pic and changes it based on the life count
      print(glider[4 - self.lives])
      print(self.reveal)
    def process(self):
      #This is the code that checks the letter while the guessing game is woring
      while self.won == False and self.lives > 0:
          self.show()
          self.guess = input('Guess the letter in the word: ')
          self.guess = self.guess.upper()
          
          if self.guess == self.word:
              self.won = True
              self.reaveal = self.word
          if len(self.guess) == 1 and self.guess in self.word:
              self.won = self.letter_check(self.guess, self.word)   
          else:
              self.lives-=1
          #When word is guessed prints gj message
          if self.won == True:
              print(f"Good Job! You guessed {self.word}")
              
          elif self.won == False:
              print("Looks like you lost :(")
              
          #When you lose this will show the character last pic
          if self.lives == 0:
              self.lose = True
          if self.lose == True:
              print(glider[4])
              print("Game Over :( Sorry about that!")
              self.lost = False
              print(self.word)