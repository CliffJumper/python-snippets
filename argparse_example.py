import argparse


# Setup Parser and args

parser = argparse.ArgumentParser()

# Add positional Arg
parser.add_argument("square", type=int, help="Number which is to be squared")

# Optional Arg
parser.add_argument("-v", "--verbosity", help="Increase verbosity of output")

# Required Arg
parser.add_argument("-a", "--account", help="Account Number", required=True)

# Parse Args
args = parser.parse_args()
