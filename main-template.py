# imports
import argparse

class MyClass:

    def __init__(self, string):
        self.mystring = string
    
    def f(self):
        return self.mystring


###############################################################################
# Main entry (use for testing what's in this file if it's not the app's entry)
###############################################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    ###########################################################################
    # Examples for argparse usage; change these at the program needs
    ###########################################################################
    # Add positional Arg
    #parser.add_argument("square", type=int, help="Number which is to be squared")
    # Optional Arg
    parser.add_argument("-v","--verbosity", help="Increase verbosity of output")
    # Required Arg
    parser.add_argument("-s","--string",help="String to print", required=True)
    # Parse Args
    args = parser.parse_args()

    x = MyClass(args.string)

    print(x.f())
