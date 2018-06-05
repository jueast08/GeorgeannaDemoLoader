def validateResponse(options, response, caseSensitive = False):
   """
   Return true if the response if among the list of options. 

   @param [string]
   @param string
   @param boolean CaseSentive
   """
   if response in options:
      return True

   if not caseSensitive and response.lower() in map(str.lower,options):
      return True

   return False

def getUserResponse(options, message, caseSensitive = False):
   """
   Takes a list of options and shows to the user a message.
   The user must then enter a response that is included in the
   list of options

   @param [string] a list of options
   @param string message to show to the user
   """

   while True:
      response = raw_input(message)
      if validateResponse(options, response, caseSensitive):
         return response

      print "Response must be one of the following", options
