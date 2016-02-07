#!/usr/bin/python
#-*- coding: utf8 -*-

import os 


def getLabel(folder, filestream):
	
	for subdir, dirs, files in os.walk(folder):
		for filename in files:
			pSplit = str(subdir).split("/")
                        imgFolder = pSplit[len(pSplit)-1]
                        if imgFolder in ['POS', 'NEG']:
                                print imgFolder
                                print filename
                                if imgFolder == "POS":
                                        filestream.write(filename+","+str(1)+"\n")
                                elif imgFolder == "NEG":
                                       	filestream.write(filename+","+str(0)+"\n")

if __name__ == "__main__":
	folder = "/media/8477-CF77/Lamine/Nazia"
	destination = open("manuel_labelling.csv", "wb")
	getLabel(folder, destination)

	destination.close()
