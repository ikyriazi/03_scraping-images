# how to read files and extract their titles
# --> https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing/blob/master/Lesson/reading-multiple-files.md
import glob

# import csv 
# import requests 
import xml.etree.ElementTree as ET 


xml_files = glob.glob('ethnologie-metadaten/*')
# print(xml_files)

# headers = []
for xml_file in xml_files:
	with open(xml_file, 'r') as f:
		tree = ET.parse(xml_file)
		root = tree.getroot()
		# read the first line
		# first_line = f.readline()
		# append to headers
		# headers.append(first_line)

print(headers)



# read all xml files and extract the image urls
# --> https://www.geeksforgeeks.org/xml-parsing-python/