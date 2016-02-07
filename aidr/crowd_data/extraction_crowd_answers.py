#!/usr/bin/python
#-*- coding: utf8 -*-

import json
import re



if __name__ == '__main__':
	filename = "pamAnnotation.json"
	open_file = open(filename)
	read_data = json.loads(open_file.read())
	RECORDS = read_data["RECORDS"]

	destination = open('crowd_dataset.csv', "wb")
	destination.write("ObjectID,PropertyID,PropertyValue,SourceID,TimeStamp\n")
	for item in RECORDS:
		user_id = item["user_id"]
		user_ip = item["user_ip"]
		info  = json.loads(item['info'])
		prop_value = info["loc"]
		url = str(info["url"]).split('/')
		objectID = url[len(url) - 1]
		
		if len(prop_value) == 0:
			print('{}\t{}\t{}\n'.format(str(objectID), str(0), str(user_ip)))
			destination.write(str(objectID)+",IsHouse,"+str(0)+","+str(user_ip)+",null\n")
		else:
			print('{}\t{}\t{}\n'.format(str(objectID), str(1), str(user_ip)))
			destination.write(str(objectID)+",IsHouse,"+str(1)+","+str(user_ip)+",null\n")

	destination.close()
	
