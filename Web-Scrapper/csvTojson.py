import csv as csv
import json as json

csvfile = open('../Data/courses.csv', 'r')
jsonfile = open('../Data/courses.json', 'w', encoding='utf8')

fieldnames = ("Course Id",	"Course Name",	"Slug",	"Provider"	"Universities/Institutions"	"Parent Subject", "Child Subject",	"Category",	"Url",	"Next Session Date",	"Length",	"Language",	"Video(Url)", "Course Description",	"Credential Name",	"Created",	"Status",	"Rating",	"Number of Ratings", "Certificate",	"Workload")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
  try:
      json.dump(row, jsonfile)
      jsonfile.write('\n')
  except Exception:
    print(row)
    pass

