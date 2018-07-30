#!/Users/dv/anaconda/bin/python3
# -*- coding: utf-8 -*- 

from bs4 import BeautifulSoup
import requests
import lxml
import html5lib
import json
import csv

''' 
getCourseListing function extracts all the courses listed
and we save the courses in the course_listing.csv file 
in the data folder.
'''

def getCourseListing():
    with open("./Data/course_listing.csv", 'w', newline= '') as myCSVFile:
        fieldnames = ['ID', 'FullURI', 'ProductBadge', 'CourseDescription']
        thewriter = csv.DictWriter(myCSVFile, fieldnames= fieldnames)
        thewriter.writeheader()
        with open("./Data/course_catalog.html", encoding="utf-8") as input_file:
            data = input_file.read()
            soup = BeautifulSoup(data, 'html.parser')
            id = 1
            for alink in soup.find_all('a'):
                product_badge = alink.find('span', {'class': 'product-badge'})
                # course_info = alink.find('div', {'class': 'card-info'})
                if not product_badge == None:
                    course_description = alink.find(
                        'span', class_='card-description')
                    thewriter.writerow({
                        'ID': id, 
                        'FullURI': 'https://coursera.org' + alink['href'], 
                        'ProductBadge': product_badge.text , 
                        'CourseDescription': course_description.text
                        })
                    id += 1


getCourseListing()
