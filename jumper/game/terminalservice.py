class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
#Seth
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.
        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

#Jeremy 
    def write_list(self,list,range):
        """Display the given list on the terminal.
        
        Args:
            self (Terminal_Service): An instance of Terminal_Service.
            list (string): The text to display.
        """
        for i in list[range:]:
            print (i)
        
        else:
            list[4] = '  _x_'
            list[5] = '  _|_'
            list[6] = '^^^^^^^'
            for i in list[range:-1]:
                print(i)