import csv
import json

rows = []

with open('./Data/Final_Model_Output.csv', 'rt', encoding='latin1') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('./MOOC-UI/src/data/courses.json', 'w') as f:
    json.dump(rows, f)

with open('./MOOC-UI/src/data/courses.json', 'r') as f:
    obj = json.load(f)
    print (obj[3]['courseId'])