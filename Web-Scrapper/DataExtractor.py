from bs4 import BeautifulSoup
import requests
import lxml
import html5lib
import json

# def get_course_listing(input_uri):
#   uri_listing = []
#   source = requests.get(input_uri).text
#   soup = BeautifulSoup(source, 'lxml') 
#   for alink in soup.find_all('a'):
#     # uri_listing.append(alink.encode('utf-8').strip())
#     print(alink.find('div', class_ = 'card-info').encode('utf-8').strip())
#     print('----------------------')
#     print (alink['href'])
#     print('----------------------')    
#     print(alink.find('span', class_ = 'product-badge'))
#     print('----------------------')    
#     print(alink.find('span', class_ = 'card-description').encode('utf-8'))
#     print('----------------------')    
#   # with open('../Data/course_listing.json', 'w') as outputfile:
#   #   json.dump(uri_listing, outputfile)

# get_course_listing('https://www.coursera.org/courses')
    

# # source = requests.get('https://www.coursera.org/learn/python-data').text
# source = requests.get('https://www.coursera.org/learn/machine-learning').text

# soup = BeautifulSoup(source, 'lxml')

# body = soup.find('body')

# for aText in body.find('div', class_ = 'bt3-col-sm-9').find_all('a'):
#   print(aText.get('href'))

# for a in soup.find_all('a', href=True):
#     print ("Found the URL:", a['href'])
#bt3-col-sm-9
# #266


def get_course_listing():
  with open("../Data/course_catalog.html", encoding="utf-8") as input_file:
    data = input_file.read()
    soup = BeautifulSoup(data, 'html.parser')
    for alink in soup.find_all('a'):
      product_badge = alink.find('span', {'class' : 'product-badge'})
      course_info =  alink.find('div', {'class' : 'card-info'})
      if not product_badge == None:
        course_description = alink.find('span', class_ = 'card-description').encode('utf-8').strip()
        print (alink['href'], product_badge.text, course_description)

        

get_course_listing()