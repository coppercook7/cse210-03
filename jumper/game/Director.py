from game.terminalservice import TerminalService
from game.skydiver import Skydiver
from game.puzzle import Puzzle

# Create a class called "Director".
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle.
        skydiver (Skydiver): The game's skydiver.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        self._is_playing = True
        self._puzzle = Puzzle()   
        self._skydiver = Skydiver()
        self._terminal_service = TerminalService()
        self._lives = 0
        self._guess = ""
        
        """Args:
            self (Director): an instance of Director.
        """

    def start_game(self):
        """Starts the game by running the main game loop. Use a while
        loop to check if the game has ended and if so, to ask the user
        to keep playing or end game.
        
        Args:
            self (Director): an instance of Director."""
        while self._is_playing == True:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            

        # if self._puzzle.puzzle_complete() == True:
        #     self._terminal_service.game_over("You Win")

        # else:
        #     self._terminal_service.game_over("Better luck next time.")

    def _get_inputs(self):
        """Get the guessed letter from player.
        Args:
            self (Director): An instance of Director."""
        self._guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
        return self._guess


    def _do_updates(self):
        

        if self._puzzle.guess_is_correct(self._guess) == True:
            self._puzzle.replace_blank(self._guess)
            if self._puzzle.puzzle_complete() == True:
                self._is_playing = False
        else:
            self._lives = self._lives+1
            self._skydiver.kill_skydiver(self._lives)

            if self._lives < 4:
                self._is_playing = True
            else:
                self._is_playing = False



            
            """Keeps track of player guess.
            
            Args:
                self (Director): An instance of Director.
            """

    def _do_outputs(self):
        self._terminal_service.write_list(self._skydiver.get_skydiver(),self._skydiver._range)
        self._terminal_service.hidden_word(self._puzzle.replace_blank(self._guess))

        if self._is_playing == False:

            if self._puzzle.puzzle_complete() == True:
                self._terminal_service.game_over(("You Win!!!"))

            else:
                self._terminal_service.game_over("Better luck next time.")

        """Update puzzle displayed.
        
        Args:
            self (Director): An instance of Director.
        """
    
    # It's working perfectly!!!