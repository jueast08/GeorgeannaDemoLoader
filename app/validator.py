import sys
import os
import json
import subprocess
import string
import re
from subprocess import call
from subprocess import check_output
from subprocess import Popen, PIPE
from termcolor import cprint
from jsonschema import validate
from misc.schema import validationSchema

class DemoValidator:
    """
    Validate a playbook json file. Responsible for testing if a jsonFile
    is Valid json and that it corresponds with the Georgeanna Demo Launcher
    Program
    """
    def __init__(self, jsonFile):
        self.jsonFile = jsonFile

    def validateToStdout(self):
        self._validateJSONToStdout()
        if self._isValidJSON():
            self._printJSON()
            self._validatePlaybookToStdout()

    def validate(self):
        """
        Return true if the playbook file is correct
        """
        return self._isValidJSON() and self._isValidPlaybook()

    def _isValidJSON(self):
        """
        Checks if a self.jsonFile is a valid json file

        @return boolean True if json is valid, False otherwise
        """
        try:
            with open(self.jsonFile) as f:
                output = json.load(f)
            return True
        except ValueError as e:
            return False

    def _getErrorMessage(self):
        """
        Returns the error message related to the json file
        @return string
        """
        p = Popen(["python","-m","json.tool", self.jsonFile], stdout=PIPE, stderr=PIPE)
        output, error = p.communicate()
        return error

    def _getErrorLine(self, error):
        """
        Checks to see if the patern "line #" exists in the error string and
        extracts the number of the line if possible

        @return int error line number if available, otherwise -1
        """
        m = re.search("\W*line[\s]\D*(\d+)",error)
        if m is not None and m.group is not None:
            return int(m.group(1))
        return -1

    def _getErrorAndLine(self):
        """
        Returns the error message and the corresponding line number if it exists

        @return string
        @return int error line number if available, otherwise -1
        """
        error = self._getErrorMessage()
        return error, self._getErrorLine(error)

    def _printJSON(self, errorLineNb = -1):
        """
        Prints the JSON file line by line, adding line numbers and coloring the
        line containing the error (if that information is available)

        @param int line number of the error
        """
        with open(self.jsonFile) as f:
            output = f.read()
            splitOutput = output.split('\n')
            numberOfLines = len(splitOutput)
            maxNbDigits = len(str(numberOfLines))

            for i in range(numberOfLines):
                nbOfSpaces = (maxNbDigits - len(str(i)))
                jsonLine = str(i + 1)
                for j in range(nbOfSpaces):
                    jsonLine += " "
                jsonLine += " | "+splitOutput[i]

                if (i + 1) == errorLineNb :
                    cprint(jsonLine, "red", attrs=["bold"])
                else:
                    print jsonLine

    def _validateJSONToStdout(self):
        """
        Checks if JSON is valid and prints errors if the json is not
        """
        valid = self._isValidJSON()
        if valid is True:
            print self.jsonFile, " is valid"
        else:
            error, errorLineNb = self._getErrorAndLine()
            self._printJSON(errorLineNb)
            print error

    def _verifyPlaybookCommands(self, commands):
        """
        Verifies that each command of the playbook follows the correct playbook format

        @return boolean, message
        """
        cmdsValid = True
        for command in commands:
            if "shell" in command and "options" in command:
                if command["shell"]:
                    cmdsValid = False
                    return cmdsValid, "the keys 'shell' and 'options' cannot be used at the same time in a command"
        return cmdsValid, "Playbook commands are valid"

    def _isValidPlaybook(self):
        """
        Returns a boolean describing if the playbook is valid or not
        """
        with open(self.jsonFile) as f:
            output = json.load(f)
            cmdsValid,msg = self._verifyPlaybookCommands(output["commands"])
            try:
                validate(output, validationSchema())
                return cmdsValid
            except:
                return False

    def _validatePlaybookToStdout(self):
        with open(self.jsonFile) as f:
            output = json.load(f)

            cmdsValid, msg = self._verifyPlaybookCommands(output["commands"])
            print msg
            try:
                validate(output, validationSchema())
            except Exception as e:
                print e


