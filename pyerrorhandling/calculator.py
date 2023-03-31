import error

class Math (object):
    """
    Performs basic addition, subtraction and multiplication functions.
    The generated errors and exceptions are appended to the error object.
    """
    def __init__(self):
        self.err = error.ProcessError()

    def addition(self, a: float, b: float):
        # Performs addition if there are no errors 
        try:
            if self.err.get_state() == 0:
                print(a + b)
            else:
                print(self.err.err_arr)
        except Exception as err:
            self.err.set_error(self.addition.__name__, err)
            print(self.err.err_arr)

    
    def subtraction(self, a: float, b: float):
        # Performs subtraction if there are no errors
        # A user generated error message is included
        try:
            if self.err.get_state() == 0:
                print(a - b)
            else:
                print(self.err.err_arr)
        except Exception as err:
            self.err.set_error(self.subtraction.__name__, "error template #1")
            print(self.err.err_arr)

    def multiplication(self, a: float, b: float, ignore_error = False):
        # Performs multiplication if there are no errors
        # An additional switch has been added to perform the same by ignoring the error
        try:
            if self.err.get_state() == 0 or ignore_error:
                print(a * b)
            else:
                print(self.err.err_arr)
        except Exception as err:
            self.err.set_error(self.multiplication.__name__, err)
            print(self.err.err_arr)