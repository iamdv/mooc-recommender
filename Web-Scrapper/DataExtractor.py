from bs4 import BeautifulSoup
import requests
import lxml
import html5lib

source = requests.get('https://www.coursera.org/learn/python').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())