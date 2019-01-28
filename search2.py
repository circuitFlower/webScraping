from mathematicians import simple_get
from bs4 import BeautifulSoup
raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.html')
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('li')):
	print(i, li.text)
