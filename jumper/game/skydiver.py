from .puzzle import Puzzle

# Create the class Skydiver:
class Skydiver:
    def __init__(self):
#Erin       
    
        self._parachute_guy = [' _____', '/_____\\', '\     /', ' \   /', '   O',  '  /|\\', '  / \ ', '', '^^^^^^^']
        """List to define each line of the skydiver"""
        self._range = 0

#Joe
#    Create method get_skydiver()
    def get_skydiver(self,):
        return self._parachute_guy
#Joe
#    Create method kill_skydiver()

    # def kill_skydiver(self):
        
    #     if Puzzle.guess_is_correct == False:
    #         new_lives = self.lives + 1
    #         self.lives = new_lives

    def kill_skydiver(self,lives):
        self._range = lives
        
