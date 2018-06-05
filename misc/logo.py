import os

def logo():
    pwd = os.path.dirname(os.path.realpath(__file__))
    with open(pwd+"/logo.txt") as logo:
        return logo.read()
