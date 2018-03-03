# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:27:21 2018

@author: schattop
"""

# ToDo:  use arguments so that user can specify file path when
# running script. Can also have defaults in case user does not
# specify any path
readFile = open("20180228 ADMET2 ES113=1 list.txt", "r")
writeFile = open("modifiedForSQL.txt", "w+")

for line in readFile:
    line = line.rstrip('\n')
    writeFile.write("\"" + line + "\", ")
    
readFile.close()
writeFile.close()