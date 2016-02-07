#! /usr/bin/python
#-*- coding: utf8 -*-

import sys
import os
import re
import csv 
import nltk

if __name__ == "__main__":
	filename    = "1454828586235-1500-without-retweet-383cfbddb1e81e00064dc2b04d152e9d.csv"
	file_reader = open(filename, 'r')
	csv_reader  = csv.reader(file_reader, delimiter='\t')

	for index, data in enumerate(csv_reader):
		print 'index:::' + str(index)
		print data 

