
class ProcessError (object):
    """
    A class that handles exceptions, errors and user warnings via an object.
    This approach can be used to prevent the code from breaking during the execution.
    """
    def __init__(self):
        self.err_arr = []

    def display_error(self):
        # Prints the error array
        print(self.err_arr)

    def set_error(self, func_name:str = "",err_msg = None):
        # Appends a dict containing function name and error message to the error array
        self.err_arr.append({func_name: err_msg})

    def get_state(self):
        # Defines the state of error and returns 1 if an error exists
        if len(self.err_arr) != 0:
            return 1
        else:
            return 0
        
    def reset_state(self):
        # Clear all the errors from the error array and returns 0 
        self.err_arr = []
        return self.get_state()
    