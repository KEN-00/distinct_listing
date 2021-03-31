import sys, getopt, json

#config_reader.py is used to retrieved config parameters from either json file or environment variables (i.e. api_config)

def getArgs(argv):
   inputFilePath = None
   outputFilePath = None

   try:
      opts, args = getopt.getopt(argv,"i:o:",["input=", "output="])
   except getopt.GetoptError:
      print('disinct_listing.py -i <input file> -o <output file>')
      sys.exit(2)


   for opt, arg in opts:
      if opt in ("-i", "--input"):
         inputFilePath = arg
      if opt in ("-o", "--output"):
         outputFilePath = arg

   print("[arg_reader.py] Input file is ", inputFilePath)
   print("[arg_reader.py] Output file is ", inputFilePath)

   jsonData = None

   
   config = {
       "inputFilePath": inputFilePath,
       "outputFilePath": outputFilePath
   }
   
   print("[arg_reader.py] args dictionary: ", config)
   return config

if __name__ == "__main__":
   argv = sys.argv[1:]
   config = getArgs(argv)
   print("[arg_reader.py] args dictionary: ", config)