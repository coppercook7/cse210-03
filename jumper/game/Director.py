from game.terminalservice import Terminal_Service
from game.skydiver import Skydiver
from game.puzzle import Puzzle

# Create a class called "Director".
class Director:

    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's _puzzle.
        is_playing (boolean): Whether or not to keep playing.
        skydiver (Skydiver): The game's skydiver.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
    # Define new attributes "_puzzle", "_is_playing", "_skydiver", "_terminal_service"
        self._puzzle = Puzzle
        self._is_playing = True
        self._skydiver = Skydiver
        self._terminal_service = Terminal_Service()
        """Args:
            self (Director): an instance of Director.
        """


    # Define a start_game() with the below
    def start_game(self):
        """Starts the game by running the main game loop. Use a while
        loop to check if the game has ended and if so, to ask the user
        to keep playing or end game.
        
        Args:
            self (Director): an instance of Director."""


    #- _do_inputs()
    def _get_inputs(self):
        """Get the guessed letter from player.

        Args:
            self (Director): An instance of Director."""


    #- _do_updates()
    def _do_updates(self):
        """Keeps track of player guess.
        
        Args:
            self (Director): An instance of Director.
        """


    #- _do_output()
    def _do_outputs(self):
        """Update puzzle displayed.
        
        Args:
            self (Director): An instance of Director.
        """