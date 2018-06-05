import json
import sys
import os
from subprocess import call
from termcolor import cprint
from termcolor import colored
from validator import DemoValidator
from misc.logo import logo
from utility import getUserResponse
from metadata import MetaDataHandler
from commands import CommandHandler

class DemoLauncher:
   """
   Responsible playing a Georgeanna playbook json file.
   """

   def __init__(self, jsonFile):
       self.config = []
       self.commands = []
       self.jsonFile = jsonFile
       self.CMD_COLOR = 'green'
       self.DESC_COLOR = 'white'
       self.LOGO_COLOR = 'green'
       self.PWD = os.path.dirname(os.path.realpath(__file__))
       self.LOGO_FILE = self.PWD+"/../misc/logo.txt"

   def run(self):
       """
       runs the Georgeanna playbook json file
       """
       call(["clear"])
       cprint(logo(), self.LOGO_COLOR, attrs=["bold"])
       self._loadJSONFile(self.jsonFile)
       MetaDataHandler(self.config).printAuthorInfo().printPlaybookName().printNumberOfPlays(self.commands).printPlaybookDescription()

       try:
          response = getUserResponse(['y', 'yes', 'no', 'n'], "Continue [y/n] ")
          if response[:1] == 'n':
             raise KeyboardInterrupt
       except KeyboardInterrupt:
          self._quit()

       print "Starting demo ..."
       self._demoLoop()
       print "finished demo..."

   def _loadJSONFile(self, jsonFile):
       """
       Takes a JsonFile tries to extract the playbook commands and metadata
       from the resulting python object

       Exits if json file is not valid
       @param string json file path
       """
       validator = DemoValidator(jsonFile)
       if validator.validate() is False:
           validator.validateToStdout()
           print "Your playbook is not valid"
           self._quit(1)

       with open(jsonFile) as f:
           self.config = json.load(f)
           self.commands = self.config["commands"]


   def _quit(self, code = 0):
      print "\nStopping playbook"
      sys.exit(0)


   def _demoLoop(self):
       """
       Plays all of the commands until there are no more plays to run or
       until the user refuses to continue
       """
       for command in self.commands:
           call(["clear"])
           handler = CommandHandler(command)
           handler.printCommandDescription().printCommand()
           response = ""

           try:
              response = getUserResponse(['y','yes','no','n','s','skip'], "Continue [y/n] or 's' to skip ? " )
              if response[:1] == 'n':
                 self._quit()
           except KeyboardInterrupt:
              continue

           if response[:1] == 'y':
              handler.run()
              try:
                 response = getUserResponse(['y', 'yes', 'no', 'n'], "Continue [y/n] ")
                 if response[:1] == 'n':
                    raise KeyboardInterrupt
              except KeyboardInterrupt:
                 self._quit()

