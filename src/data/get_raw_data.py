# -*- coding: utf-8 -*-
"""
@author: jecheverrigutierrez@gmail.com
"""

def DownloadDatabase(databasepath,filename,url):
    
    #Required library to download files from a given URL
    import requests
    #Required library to unzip a zipfile
    import zipfile
    #Required library to invoke Operative System command
    import os    
    #Required to copy files
    import shutil
    
    #Get file from URL to memory
    try:
        zipfile_db = requests.get(url)
    except:
        print("Problem found: Unable to download zipfile")
        return -127
    
    #Create the zip file
    try:
        open(filename, 'wb').write(zipfile_db.content)
    except: 
        print("Problem found: Unable to generate zipfile on local machine")
        return -128
    
    #Unzip the file and copy files to desired directory
    try:    
        with zipfile.ZipFile(filename, 'r') as zip_file:
            #Iterate through all the files with the full path
            for member in zip_file.namelist():
                #Basename command gets the name of the file
                filename_ = os.path.basename(member)
                # It will not copy folders
                if not filename_:
                    continue            
                #Copy the files
                source = zip_file.open(member)
                target = open(os.path.join(databasepath, filename_), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
    except:
        print("Problem found: Unable to unzip fhe zip file")
        return -129
    
    #Remove the file after downloading    
    try:
        os.remove(filename)
    except:
        print("Problem found: Unable to delete zip file or the file does not exist")
        return -130

    return 0  