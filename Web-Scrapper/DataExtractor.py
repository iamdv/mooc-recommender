#!/Users/dv/anaconda/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import lxml
import html5lib
import json
import csv


#############################################################################
''' 
getCourseListing function extracts all the courses listed
and we save the courses in the course_listing.csv file 
in the data folder.
'''


def getCourseListing():
    with open("./Data/course_listing.csv", 'w', newline='') as myCSVFile:
        fieldnames = ['ID', 'FullURI', 'ProductBadge', 'CourseDescription']
        thewriter = csv.DictWriter(myCSVFile, fieldnames=fieldnames)
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
                        'ProductBadge': product_badge.text,
                        'CourseDescription': course_description.text
                    })
                    id += 1

# getCourseListing()

#############################################################################


#############################################################################
def getCourseContent():
    myBreadCrumb = []

    with open("./Data/course_listing.csv", 'r') as myCSVFile:
        theCSVreader = csv.reader(myCSVFile)
        next(theCSVreader)

    source = requests.get(
        'https://www.coursera.org/learn/pathophysiology').text
    soup = BeautifulSoup(source, 'lxml')
    for data in soup.find_all('div', class_='rc-BannerBreadcrumbs'):
        for a in data.find_all('a'):
            myBreadCrumb.append(a.text)
    print(myBreadCrumb)


getCourseContent()

# <a data-click-key = "discovery.phoenix_cdp.click.breadcrumb_browse_subdomain" data-click-value = "{&quot;namespace&quot;:{&quot;app&quot;:&quot;discovery&quot;,&quot;page&quot;:&quot;phoenix_cdp&quot;,&quot;component&quot;:&quot;breadcrumb_browse_subdomain&quot;,&quot;action&quot;:&quot;click&quot;},&quot;schema_type&quot;:&quot;FRONTEND&quot;,&quot;href&quot;:&quot;/browse/life-sciences/clinical-science&quot;}" data-track = "true" data-track-app = "discovery" data-track-page = "phoenix_cdp" data-track-action = "click" data-track-component = "breadcrumb_browse_subdomain" data-track-href = "/browse/life-sciences/clinical-science" href = "/browse/life-sciences/clinical-science" to = "/browse/life-sciences/clinical-science" class = "link nostyle" target = "_blank" data-reactid = "245" > Clinical Science < /a >
