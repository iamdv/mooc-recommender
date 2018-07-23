from bs4 import BeautifulSoup
import requests
import lxml
import html5lib
import json

def get_course_listing(input_uri):
  uri_listing = []
  source = requests.get(input_uri).text
  soup = BeautifulSoup(source, 'lxml') 
  for alink in soup.find_all('a'):
    # uri_listing.append(alink.encode('utf-8').strip())
    print(alink.find('div', class_ = 'card-info').encode('utf-8').strip())
    print (alink['href'])
    print(alink.find('span', class_ = 'product-badge'))
    print(alink.find('span', class_ = 'card-description').encode('utf-8'))
  # with open('../Data/course_listing.json', 'w') as outputfile:
  #   json.dump(uri_listing, outputfile)

get_course_listing('https://www.coursera.org/courses')
    

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


# https://www.coursera.org/courses?refinementList%5Blanguage%5D=&page=1&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=5&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=3&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BhitsPerPage%5D=20&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=4