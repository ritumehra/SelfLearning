
class teardown_concept:

    def __init__(self):
        print("An instantiation already exists!")
            # do your init stuff

    def __del__(self):
        print("Exiting Class!")

    field = 10

    @classmethod
    def tear_down(self):
        print("tearDown called {}".format(self.field))

    @classmethod
    def print_function(self):
        print("Function Called: print_function: {}".format(self.field))

    def print_function1(self):
        print("Function Called: print_function: {}".format(self.field))