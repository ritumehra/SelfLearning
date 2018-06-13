
class DocstringClassMain:

    var_str = "Init"

    def __init__(self):
        """
        This function is the initialization of the class 
        @:param : None
        @:return : Nothing
        """
        print ("Initialize Doctring: {} ".format(self.var_str))

    def __del__(self):
        """
        This function is called at the exit of the class 
        @:param : None
        @:return : Nothing
        """
        print ("Exiting DocString Class : {} ".format(self.var_str))


if __name__ == "__main__":

    docstring_class_main_obj = docstring_class_main()


