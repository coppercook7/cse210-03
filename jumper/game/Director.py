from game.Jumper import Jumper
from game.Jumper import words
from game.console import Console



class Director:


    def __init__(self):
        self.keep_playing = True
        self.console = Console()
        self.jumper = Jumper()
        self.word = words

    def start_game(self):

        print("while loop or something here to keep the game going")

    def get_inputs(self):
        self.word

    def do_updates(self):
        
        self.jumper.process()

    def do_outputs(self):
        pass



