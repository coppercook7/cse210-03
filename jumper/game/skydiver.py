from .puzzle import Puzzle

# Create the class Skydiver:
class Skydiver:
    def __init__(self):
#Erin       
    
        self._parachute_guy = [' _____', '/_____\\', '\     /', ' \   /', '   O',  '  /|\\', '  / \ ', '', '^^^^^^^']
        """List to define each line of the skydiver"""
        self.lives = 0

#Joe
#    Create method get_skydiver()
    def get_skydiver(self, range):
        for i in self._parachute_guy[range:]:
            print (i)
        
        else:
            self._parachute_guy[4] = '  _x_'
            self._parachute_guy[5] = '  _|_'
            self._parachute_guy[6] = '^^^^^^^'
            for i in self._parachute_guy[range:-1]:
                print(i)
#Joe
#    Create method kill_skydiver()

    # def kill_skydiver(self):
        
    #     if Puzzle.guess_is_correct == False:
    #         new_lives = self.lives + 1
    #         self.lives = new_lives

    def kill_skydiver(self,lives):
        self.range = lives
        
