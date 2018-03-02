# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:27:21 2018

@author: schattop
"""

readFile = open("20180228 ADMET2 ES113=1 list.txt", "r")
writeFile = open("modifiedForSQL.txt", "w+")

for line in readFile:
    writeFile.write("\"" + line + "\", ")
    
readFile.close()
writeFile.close()