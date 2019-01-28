from bs4 import BeautifulSoup
from mathematicians import *
import csv
from itertools import chain
csvArray=[]
with open('sites.csv') as csvfile:
	file = csv.reader(csvfile)
	try:
		for row in file:
			print(row)
			csvArray.append(row)
	except csv.Error as e:
		sys.exit('file{},line{}:{}'.format(filename,reader.line_num,e))

list(chain(*csvArray))
print(csvArray)

for row in csvArray:
	raw_html = simple_get(*row)
	try:
		html = BeautifulSoup(raw_html, 'html.parser')
		for i,li in enumerate(html.select('li')):
			print(i, li.text)
	except:
		print(raw_html)
		print("no li found")
