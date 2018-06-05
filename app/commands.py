import re
from termcolor import cprint
from termcolor import colored
from subprocess import call
from subprocess import check_output

class CommandHandler:
   """
   Responsable for handling/running playbook commands
   """

   def __init__(self, commandMap, shell = False, descriptionColor = 'white', commandColor = 'green'):
      """
      @param object commandMap a playbook formated command 
      @param boolean shell indicates whether the call() command should treat the arguements passed in parameter as shell commands
      @param string descriptionColor
      @param string commandColor
      """
      self.command = commandMap
      self.DESC_COLOR = descriptionColor
      self.CMD_COLOR = commandColor
      self.shell = False

   def printCommandDescription(self):
      cprint(self.command["description"], self.DESC_COLOR)
      return self

   def printCommand(self):
      if "command" in self.command:
         cmdTXT="\t$>" + self.command["command"] + " "
         if "options" in self.command:
            for option in self.command["options"]:
               cmdTXT = cmdTXT + option + " "

         cmdTXT = re.sub(r"\s([-]{2})([a-zA-Z])", r"\n\t\t\1\2", cmdTXT)
         cmdTXT = re.sub(r" (\||[&]{2}) ", r" \1\n\t\t", cmdTXT)
         cprint(cmdTXT, self.CMD_COLOR, attrs=['bold'])

      return self

   def _extractCommandFromMap(self, command):
      completeCMD = []
      if "options" in command:
         completeCMD = command["options"]

      completeCMD.insert(0, command["command"])
      shellEnabled = self.shell

      if "shell" in command:
         shellEnabled = command["shell"]

      return completeCMD, shellEnabled

   def run(self):
      try:
         cmd, shellEnabled = self._extractCommandFromMap(self.command)
         call(cmd, shell=shellEnabled)
      except KeyboardInterrupt:
         print "\nInterrupting command."
         return

