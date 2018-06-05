import json
import mock
import os
from app.validator import DemoValidator
from unittest import TestCase
from mock import patch, mock_open, MagicMock


PWD = os.path.dirname(os.path.realpath(__file__))

class ValidatorTestCase(TestCase):

    def testvaldate_ReturnFalseInvalidJSONAndPlaybook(self):
        validator = DemoValidator("someFile.json")
        validator._isValidJSON = mock.Mock(return_value = False)
        validator._isValidPlaybook = mock.Mock(return_value = False)

        self.assertFalse(validator.validate())


    def testvaldate_ReturnFalseInvalidJSON(self):
        validator = DemoValidator("someFile.json")
        validator._isValidJSON = mock.Mock(return_value = False)
        validator._isValidPlaybook = mock.Mock(return_value = True)

        self.assertFalse(validator.validate())

    def testvaldate_ReturnFalseInvalidPlaybook(self):
        validator = DemoValidator("someFile.json")
        validator._isValidJSON = mock.Mock(return_value = False)
        validator._isValidPlaybook = mock.Mock(return_value = True)

        self.assertFalse(validator.validate())

    def testvaldate_ReturnTrue(self):
        validator = DemoValidator("someFile.json")
        validator._isValidJSON = mock.Mock(return_value = True)
        validator._isValidPlaybook = mock.Mock(return_value = True)

        self.assertTrue(validator.validate())


    def testisValidJSON_Invalid(self):
        validator = DemoValidator(PWD+"/invalid.json")
        self.assertFalse(validator._isValidJSON())

    def testisValidJSON_Valid(self):
        validator = DemoValidator(PWD+"/validJSON_invalidPlaybook1.json")
        validator2 = DemoValidator(PWD+"/validJSON_invalidPlaybook2.json")
        self.assertTrue(validator._isValidJSON())
        self.assertTrue(validator2._isValidJSON())


    
