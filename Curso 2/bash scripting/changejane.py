
#!/usr/bin/env python3

import sys
import subprocess
path='/home/studentid'
with open (sys.argv[1], "r") as myfile:
  for line in myfile.readlines():
    source = line.strip()
    destination = source.replace('jane', 'jdoe')
    subprocess.run(['mv', path+source,path+destination])
  myfile.close()

