from termcolor import cprint
from termcolor import colored

class MetaDataHandler:
   """
   Responsable for handling the metadata part of the playbook
   """

   def __init__(self, metadata, desColor = 'white', otherColor = 'green'):
      self.metadata = metadata
      self.DESC_COLOR = desColor
      self.OTHER_COLOR = otherColor

   def printAuthorInfo(self):
      if "metadata" in self.metadata:
         for key, value in self.metadata["metadata"].iteritems():
            metadata = key.upper()+"\t: "+value
            cprint(metadata, self.DESC_COLOR, attrs=['bold'])
         print
      return self

   def printPlaybookName(self):
      cprint(self.metadata["name"], self.DESC_COLOR, attrs=['bold'])
      return self

   def printNumberOfPlays(self, commands):
      plays = "NumberOfPlays : " + str(len(commands))+"\n\n"
      cprint(plays, self.OTHER_COLOR)
      return self

   def printPlaybookDescription(self):
      cprint(self.metadata["description"], self.DESC_COLOR)
      return self
