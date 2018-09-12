import pandas as pd
import string
import csv
import json
import numpy as np


def convert_to_json(fpath):
    my_json_string = '['
    with open(fpath, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(readCSV):
            if i > 0:
                my_json_string = my_json_string + \
                '{"courseId": ' + row[1] + ',' + \
                '"courseName": "' + row[2].replace('"', '') + '",' \
                '"slug": "' + row[4].replace('"', '') + '"' \
                '},'
        my_json_string = my_json_string + ']'
   
    with open('test.json', 'w') as outfile:
        json.dump(my_json_string, outfile)
    return None



print(convert_to_json("./Data/Final_Model_Output.csv"))


# [
#   {
#     "courseId": 301,
#     "courseName": "Introduction to Artificial Intelligence",
#     "slug": "udacity-introduction-to-artificial-intelligence",
#     "provider": "Udacity",
#     "universitiesInstitutions": "Stanford University",
#     "parentSubject": "Computer Science",
#     "childSubject": "Artificial Intelligence",
#     "category": "Artificial Intelligence",
#     "url": "https://www.coursera.org/learn/jews-in-china",
#     "nextSessionDate": "Self paced",
#     "length": "10",
#     "language": "English",
#     "videoUrl": "https://www.youtube.com/watch?feature=player_embedded&v=BnIJ7Ba5Sr4",
#     "courseDescription": "Online Introduction to Artificial Intelligence is based on Stanford CS221, Introduction to Artificial Intelligence. This class introduces students to the basics of Artificial Intelligence, which includes machine learning, probabilistic reasoning, robotics, and natural language processing.\n\nThe objective of this class is to teach you modern AI. You learn about the basic techniques and tricks of the trade, at the same level we teach our Stanford students. We also aspire to excite you about the field of AI. Whether you are a seasoned professional, a college student, or a curious high school student - everyone can participate.",
#     "credentialName": "",
#     "created": "",
#     "status": "selfpaced",
#     "rating": 4.0833333333333,
#     "numberOfRatings": 24,
#     "certificate": "",
#     "workload": "6 hours a week",
#     "roleRankMap": {
#       "1": { "all": 5, "isRightPredict": false },
#       "2": { "all": 1, "isRightPredict": true },
#       "3": { "all": 5, "isRightPredict": false },
#       "4": { "all": 1, "isRightPredict": true },
#       "5": { "all": 5, "isRightPredict": false },
#       "6": { "all": 5, "isRightPredict": true },   
#       "7": { "all": 1, "isRightPredict": true },   
#       "8": { "all": 5, "isRightPredict": false }      
#     }
# ]