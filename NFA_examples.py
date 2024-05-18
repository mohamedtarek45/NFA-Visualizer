from example_1 import state_0 as state_0_1
from example_2 import state_0 as state_0_2
from example_3 import state0 as state_0_3

class NFA_examples:
    def __init__(self, regex, input_string):
        self.regex = regex
        self.input_string = input_string
        self.example_number = 0
        
        if self.regex == "x(x|y)*|z":
            self.example_number = 1
        elif self.regex == "(a|b)*abb":
            self.example_number = 2
        elif self.regex == "XY|Z*":
            self.example_number = 3

    def validate(self):
        if self.example_number == 1:
            return True
        elif self.example_number == 2:
            return True
        elif self.example_number == 3:
            return True
        else:
            return False
        
    def check(self):
        if self.example_number == 1:
            return state_0_1(self.input_string)
        elif self.example_number == 2:
            return state_0_2(self.input_string)
        elif self.example_number == 3:
            return state_0_3(self.input_string)
        else:
            return False
        