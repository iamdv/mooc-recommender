# !/Users/dv/anaconda/bin/python3
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
    with open("./Data/Coursera-Listings.csv", 'w', newline='') as myCSVFile:
        fieldnames = ['ID', 'ProductBadge', 'CourseDescription', 'FullURI']
        thewriter = csv.DictWriter(myCSVFile, fieldnames=fieldnames)
        thewriter.writeheader()

        with open("./Data/Archive/course_catalog.html", encoding="utf-8") as input_file:
            data = input_file.read()
            soup = BeautifulSoup(data, 'html.parser')
            id = 5000

            for alink in soup.find_all('a'):
                product_badge = alink.find('span', {'class': 'product-badge'})
                # course_info = alink.find('div', {'class': 'card-info'})

                if not product_badge == None:
                    course_description = alink.find(
                        'span', class_='card-description')
                    thewriter.writerow({
                        'ID': id,
                        'ProductBadge': product_badge.text,
                        'CourseDescription': course_description.text,
                        'FullURI': 'https://coursera.org' + alink['href']
                    })
                    id += 1

# getCourseListing()

#############################################################################


#############################################################################
def getCourseContent():
    courseID = 5000
    courseName = ''
    courseDescription = ''
    courseSlug = ''
    courseProvider = 'Coursera'
    courseUniversity = ''
    courseParentSubject = ''
    courseChildSubject = ''
    courseCategory = ''
    courseURI = 'https://coursera.org/learn/machine-learning'
    courseLanguage = ''
    courseLevel = ''
    courseCommitment = ''
    courseRating = 0
    courseNumberOfRatings = 0

    courseBreadCrumb = []
    courseRatingTemp = ''
    courseRatingList = []

    with open("./Data/Coursera-Listings.csv", 'r') as myCSVFile:
        theCSVreader = csv.reader(myCSVFile)
        next(theCSVreader)

    source = requests.get(courseURI).text
    soup = BeautifulSoup(source, 'lxml')
    for data in soup.find_all('div', class_='rc-BannerBreadcrumbs'):
        for a in data.find_all('a'):
            courseBreadCrumb.append(a.text)
    courseDescription = soup.find('p', class_="course-description")
    courseDescription = courseDescription.getText()
    courseName = soup.find('h1', class_="display-3-text").text
    courseSlug = 'coursera-' + courseName.strip().lower().replace(' ', '-')
    courseUniversity = soup.find('div', class_="headline-1-text creator-names").text
    courseUniversity = courseUniversity.split(':')[1].replace('Â', '').strip()
    courseLanguage = soup.find('div', class_="rc-Language").text
    courseRatingTemp = soup.find('div', class_="ratings-text headline-2-text").text
    courseRatingList = courseRatingTemp.split()
    courseRating = courseRatingList[1]
    courseNumberOfRatings = courseRatingList[6]

    # for td in soup.find_all('td', class_="td-data"):
    #     print(td)

    print('Course Name : ', courseName)
    print('Course Description : ', "\n", courseDescription)
    print('Slug : ', courseSlug)
    print('Provider : ', courseProvider)
    print('Universities/Institutions : ', courseUniversity)
    print('Parent Subject : ', courseBreadCrumb[1])
    print('Child Subject : ', courseBreadCrumb[1])
    print('Category : ', courseBreadCrumb[2])
    print('URL : ', courseURI)
    print('Language : ', courseLanguage)
    print('Rating Senctence : ', courseRatingTemp)
    print('Rating : ', courseRating)
    print('Number of Reviews : ', courseNumberOfRatings)



getCourseContent()


# YES     Course Id,
# YES     Course Name,                <h1 class="title display-3-text" data-reactid="227">General Pathophysiology</h1>
# YES     Course Description,
# YES     Slug,
# YES     Provider,
# YES     Universities/Institutions            div class="headline-1-text creator-names"
# YES     Parent Subject,
# YES     Child Subject,
# YES     Category,
# YES     Url,
# Length,
# YES     Language,                 <div class="rc-Language"><!-- react-text: 1464 -->English<!-- /react-text --></div>
# Credential Name,
# YES     Rating,
# NO      Number of Ratings,        class="ratings-text headline-2-text"
# YES     Certificate,
# YES     Workload
