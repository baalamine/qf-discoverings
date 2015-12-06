#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
this py script parses algorithms.js and creates
a latex script for the description of the algorithm
'''
import demjson


if __name__ == '__main__':
	
	# Read input file and convert js variable into json variable
	algorithms = open('algorithms.js', 'r').read()
	json_object = demjson.decode(algorithms)

	# Create an output latex file
	latex_script = open('algorithms.tex', 'wb')
	latex_script.write("\documentclass[a4paper,10pt]{scrartcl}\n\usepackage[utf8]{inputenc}\n")
	latex_script.write("\\title{Truth Discovery Algorithms}\n\subtitle{Documentation}\n")
	latex_script.write("\\author{Mouhamadou Lamine BA}\n")
	latex_script.write("\\date{\\today}\n")
	latex_script.write("\\begin{document}\n")
	latex_script.write("\\maketitle\n")
	latex_script.write("\section{Supported Algorithms}\n")
	latex_script.write("\\begin{itemize}\n")
	h=1
	for algo_data in json_object:
		print algo_data['name']
		if h <= 12:

			# algo name
			latex_script.write("\item \\textbf{" + algo_data['name'] + "}\n")
			latex_script.write("\\begin{description}\n")
			
			# algo description
			description = algo_data['description'].encode('utf8')
			latex_script.write("\item \\textbf{Description}: " + description + "\n")

			# algo parameters
			latex_script.write("\item \\textbf{Parameters}\n")
			latex_script.write("\\begin{itemize}\n")
			for param in algo_data['params']:
				
				name = param['name']
				if 'dataType' in param.keys():
					dataType = param['dataType']
				if 'min' in param.keys():
					min_value = param['min']
				if 'max' in param.keys():
					max_value = param['max']
				if 'desc' in param.keys():
					desc = param['desc']
				if 'value' in param.keys():
					def_value = param['value']
				if 'hidden' in param.keys():
					isHidden = param['hidden']

				latex_script.write("\item \\textbf{" + name + "}: " + desc.replace('.', '') + ".\n")
				if dataType != None and dataType != '':
					latex_script.write("\item[]\\textbf{dataType: }" + dataType)
				if min_value != None and min_value != '':
					latex_script.write(", \\textbf{min-value: }" + str(min_value))
				if max_value != None and max_value != '':
					latex_script.write(", \\textbf{max-value: }" + str(max_value))
				if def_value != None and def_value !='':
					latex_script.write(", \\textbf{default-value: }" + str(def_value))
				if 'hidden' in param.keys() and isHidden != None and isHidden != '':
					latex_script.write(", \\textbf{hidden: }" + str(isHidden) + "\n")
				
			latex_script.write("\end{itemize}\n")
			latex_script.write("\end{description}\n")

		elif h == 13:
			latex_script.write("\end{itemize}\n")
			name = algo_data['name']
			desc = algo_data['description']
			latex_script.write("\\section{General Parameters}\n")
			latex_script.write(desc + "\n")
			latex_script.write("\\begin{description}\n")
			latex_script.write("\item \\textbf{Parameters}\n")
			latex_script.write("\\begin{itemize}\n")
			for param in algo_data['params']:
			     print param
			     name = param['name']
			     if 'dataType' in param.keys():
					dataType = param['dataType']
			     if 'min' in param.keys():
					min_value = param['min']
			     if 'max' in param.keys():
					max_value = param['max']
			     if 'desc' in param.keys():
					desc = param['desc']
			     if 'value' in param.keys():
					def_value = param['value']
			     if 'step' in param.keys():
					step = param['step']
			     if 'hidden' in param.keys():
					isHidden = param['hidden']
					
			     latex_script.write("\item \\textbf{" + name + "}: " + desc.replace('.', '') + ".\n")
			     if dataType != None and dataType != '':
					latex_script.write("\item[]\\textbf{dataType: }" + dataType)
			     if min_value != None and min_value != '':
					latex_script.write(", \\textbf{min-value: }" + str(min_value))
			     if max_value != None and max_value != '':
					latex_script.write(", \\textbf{max-value: }" + str(max_value))
			     if def_value != None and def_value !='':
					latex_script.write(", \\textbf{default-value: }" + str(def_value))
			     if 'step' in param.keys() and step != None and step != '':
					latex_script.write(", \\textbf{step: }" + str(step))
			     if 'hidden' in param.keys() and isHidden != None and isHidden != '':
					latex_script.write(", \\textbf{hidden: }" + str(isHidden) + "\n")
			
			latex_script.write("\end{itemize}\n")
			latex_script.write("\end{description}\n")
		elif h == 14:
			print algo_data
			name = algo_data['name']
			desc = algo_data['description'].encode('utf8')
			latex_script.write("\\section{Combiner}\n")
			latex_script.write(desc + "\n")
		
		h+=1
		#print algo_data['params']

	latex_script.write("\end{document}")
 	latex_script.close()
