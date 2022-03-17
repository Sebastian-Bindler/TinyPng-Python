# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:48:04 2022

@author: cj8q21
"""

import glob
import tinify

tinify.key = ""
#tinify.proxy = "" 


filenameExtension = "png"
targetPattern = r"input/*.{}".format(filenameExtension)

if __name__ == "__main__":
    
    daten = glob.glob(targetPattern)
    datenIndex = len(daten)
    
    for i in range (0 , datenIndex):
            
        filename = daten[i]
        source = tinify.from_file(daten[i])
        
        path = "output/{}".format(filename[6:])
        print(path)
        source.to_file(path)