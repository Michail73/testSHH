import sys
import re
import os
try:

def test (filename, *args):
      print(filename)
      strings = ['ERROR INFOa', 'INFO b', 'WARN c']
      for string in strings:




            if len(args) == 0:
                  if 'ERROR' in string:
                        print(string)




            else:
                  for arg in args:
                        if arg in string:
                              print(string)
                              break


  filename = str()soft

	if __name__ == "__main__":
  	  if len (sys.argv) > 1:
    	        filename = sys.argv[1]

	if os.path.exists(filename):
  	  with open(filename, 'r') as inF:
    	  print(filename)
      	for line in  inF:
        	  if ('ERROR' in line) or (re.match('^\t.*$', line) ) or ('WARNING' in line):
          	    print line
	else:
  	  print ('file not exist')
except:
  print('Some errors')
	
	
	