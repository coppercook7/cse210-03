class Terminal_Service:
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
    def write_list(self,list):
        """Display the given list on the terminal.
        
        Args:
            self (Terminal_Service): An instance of Terminal_Service.
            list (string): The text to display.
        """
        print(list)