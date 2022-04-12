#!/usr/bin/env python3 

#David Petrovich
#Sources: 
    # https://stackoverflow.com/questions/2212643/python-recursive-folder-read 
    # https://stackoverflow.com/questions/20638040/glob-exclude-pattern

import hashlib
import glob
import sys
from datetime import datetime
from datetime import date

root_dir = '/home'

def encrypt():
    storageFile = open("storeHashes.txt", "w")

    for filename in glob.iglob(root_dir + '**/**', recursive=True):
        filename = str(filename)
        encodedFile = filename.encode()
        hashedFile = hashlib.sha256(encodedFile)
        print("FilePath:" + filename + ", HashedFile:", hashedFile)
    
        storageFile.write(filename + "," + str(hashedFile) + "," + str(date.today()) + "," + str(datetime.now))

    storageFile.close()
    return

def decrypt():
    storageFile = open("storeHashes.txt", "r")
    data = storageFile.read()
    storageFile.close()
    encrypt()
    newStorage = open("storeHashes.txt", "r")
    newData = newStorage.read()
    newStorage.close()
    if data != newData:
        print("Changes detected")
    else:
        print("No changes detected")     
    return

if sys.argv[1] == "Encrypt":
    encrypt()

if sys.argv[1] == "Decrypt":
    decrypt()

