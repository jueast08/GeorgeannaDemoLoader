import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd)

from app.validator import DemoValidator

if __name__ == "__main__":
    # check arguements
    if len(sys.argv) < 2:
        print "The second parameter must be a path to a valid json file"
        sys.exit(1)

    DemoValidator(sys.argv[1]).validateToStdout()
