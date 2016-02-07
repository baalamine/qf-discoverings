#!/usr/bin/python
#-*- coding:utf8 -*-

import csv
if __name__ == '__main__':
	algo_output_filename = "claim_results_runset_237_crowd_dataset.csv"
	manual_labelling_filename = "manuel_labelling.csv"
	file1 = open(algo_output_filename)
	file2 = open(manual_labelling_filename)
	
	first_reader = csv.reader(file1, delimiter=",")
	second_reader = csv.reader(file2, delimiter=",")
	truth = dict()
	for true_line in second_reader:
		if str(true_line[0]) not in truth.keys():
			truth[str(true_line[0])] = true_line[1]

	PosGuess = 0
	NegGuess = 0
	TotGuess = 0
	
	h = 0
	for line  in first_reader:
		if h == 0:
			h+=1
			continue
		
		objectID = line[1]
		value = line[3]
		truth_label = line[8]

		if truth_label == "t":
			if str(objectID) in truth.keys():
				value2 = truth[str(objectID)]
				if value == value2:
					PosGuess+=1
				else:
					NegGuess+=1
					
				TotGuess+=1


	print('PosGuess: {}\tNegGuess: {}\tTotGuess: {}'.format(str(PosGuess), str(NegGuess), str(TotGuess)))
