import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd)

from app.demolauncher import DemoLauncher

if __name__ == "__main__":
    # check arguements
    if len(sys.argv) < 2:
        print "The second parameter must be a path to a valid json file"
        sys.exit(1)

    DemoLauncher(sys.argv[1]).run()
