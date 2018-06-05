import app.utility as utl
from unittest import TestCase
#from mock import patch
#from mock import MagicMock

class UtilityTestCase(TestCase):

   #@patch('__builtin__.raw_input', return_value='s')
   def testValidateResponse_AnswerNotInChoices(self):
      options = ["y", "n"]
      message = "test"
      self.assertEqual(utl.validateResponse(options,'s'), False)


   def testValidateResponse_AnswerCaseSensitive(self):
      options = ["y", "n"]
      message = "test"
      self.assertEqual(utl.validateResponse(options,'Y', True), False)

   def testValidateResponse_AnswerNotCaseSensitive(self):
      options = ["y", "n"]
      message = "test"
      self.assertEqual(utl.validateResponse(options,'Y', False), True)

   def testValidateResponse_ExactAnswer(self):
      options = ["y", "n"]
      message = "test"
      self.assertEqual(utl.validateResponse(options,'y'), True)

if __name__ == '__main__':
    unittest.main()


