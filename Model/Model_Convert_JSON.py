import pandas as pd
import string
import csv
import json
import numpy as np


def convert_to_json(fpath):
    model_data = pd.read_csv(fpath)
    model_data = model_data.drop(model_data.columns[model_data.columns.str.contains('unnamed',case = False)],axis = 1)
    model_data = model_data.replace(np.nan, '', regex=True)
    model_data.columns = ['courseId', 'courseName', 'courseDescription', 'slug', 'provider', 
    'universitiesInstitutions', 'parentSubject', 'childSubject', 
    'category', 'url', 'length', 'language', 'credentialName', 'rating', 
    'numberOfRatings', 'certificate', 'workload']
    with open('./Data/Courses.json', 'w') as outfile:
        json.dump(model_data, outfile, ensure_ascii=False)
    # print(model_data)
    return None


# print(substr_after('course id', ' ', 0))
convert_to_json("./Data/Main_Coursera.csv")
