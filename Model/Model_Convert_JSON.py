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
                '"slug": "' + row[4].replace('"', '') + '",' \
                '"provider": "' + row[5].replace('"', '') + '",' \
                '"universitiesInstitutions": "' + row[6].replace('"', '') + '",' \
                '"parentSubject": "' + row[7].replace('"', '') + '",' \
                '"childSubject": "' + row[8].replace('"', '') + '",' \
                '"category": "' + row[9].replace('"', '') + '",' \
                '"url": "' + row[10].replace('"', '') + '",' \
                '"nextSessionDate": "' + "NA" + '",' \
                '"length": "' + row[11].replace('"', '') + '",' \
                '"language": "' + row[12].replace('"', '') + '",' \
                '"courseDescription": "' + row[3].replace('"', '') + '",' \
                '"credentialName": "' + row[13].replace('"', '') + '",' \
                '"created": "' + "NA" + '",' \
                '"status": "' + "Self paced" + '",' \
                '"rating": "' + row[14].replace('"', '') + '",' \
                '"numberOfRatings": "' + row[15].replace('"', '') + '",' \
                '"certificate": "' + row[16].replace('"', '') + '",' \
                '"workload": "' + row[17].replace('"', '') + '",' \
                '"roleRankMap":' \
                '{"1":' + '{' \
                '"all": "' + str(round(float(row[18]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[19].lower().replace('"', '') + '"},' \
                '"2":' + '{' \
                '"all": "' + str(round(float(row[20]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[21].lower().replace('"', '') + '"},' \
                '"3":' + '{' \
                '"all": "' + str(round(float(row[22]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[23].lower().replace('"', '') + '"},' \
                '"4":' + '{' \
                '"all": "' + str(round(float(row[28]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[29].lower().replace('"', '') + '"},' \
                '"5":' + '{' \
                '"all": "' + str(round(float(row[24]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[25].lower().replace('"', '') + '"},' \
                '"6":' + '{' \
                '"all": "' + str(round(float(row[26]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[27].lower().replace('"', '') + '"},' \
                '"7":' + '{' \
                '"all": "' + str(round(float(row[30]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[31].lower().replace('"', '') + '"},' \
                '"8":' + '{' \
                '"all": "' + str(round(float(row[32]), 4)).replace('"', '') + '",' \
                '"isRightPredict": "' + row[33].lower().replace('"', '') + '"}' \
                '}},'
        my_json_string = my_json_string + ']"'
   
    with open('./Data/Final_Model_Output.txt', 'w') as outfile:
        json.dump(my_json_string, outfile, ensure_ascii=False)
    return None


print(convert_to_json("./Data/Final_Model_Output.csv"))

