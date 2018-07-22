from bs4 import BeautifulSoup
import requests
import lxml
import html5lib

# source = requests.get('https://www.coursera.org/learn/python-data').text
source = requests.get('https://www.coursera.org/learn/machine-learning').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify().encode('utf-8'))

body = soup.find('body')
summary = body.find('div', class_ = 'bt3-col-sm-9')
print(summary.prettify().encode('utf-8'))


#bt3-col-sm-9
# #266