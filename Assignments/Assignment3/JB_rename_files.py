# Script to rename all image files, given a student number
# Assumes that images to be renamed are already in 16 sub-folders (1 per building)
# Written by James Baak, Nov 2019

import os
import glob
import sys

def renameFolder(folder_name, id):
    img_files = glob.glob(".\{}\*jpg".format(folder_name))

    i = 1
    for img_file in img_files:
        os.rename(img_file, ".\{}\{}-{}.jpg".format(folder_name, id, i))
        i += 1
        
def renameAll(last_3_digits):
    folders = [
        "AA", "ML", "HP", "TB",
        "CB", "PA", "HS", "MC",
        "CT", "RB", "LB", "ME",
        "DT", "RO", "FH", "SA"
    ]
    
    for folder in folders:
        renameFolder(folder, last_3_digits)
        print("Renamed files in folder {}".format(folder))
    
if __name__ == "__main__":
    renameAll(sys.argv[1])
    