import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import string
import csv

# nltk.download('stopwords')

def normalize(text):
    """
    Normalizes the text to remove the capital letters and punctuations
    as they hinder textual anyalsis.
    :param text: search text
    :return: returns the normalized text.
    """
    remove_punctuation_map = dict((ord(char), None)
                                  for char in string.punctuation)
    return text.lower().translate(remove_punctuation_map)


def cosine_sim(text1, text2):
    """
    Calcuates the cosine distance between the skills
    and the course description.
    :param text1: Phrase 1
    :param text2: Phrase 2
    :return: returns the probabilistic measure of similarity.
    """
    vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


def execute_cosine(fpath_skills, fpath_courses):
    df_skills = pd.read_csv(fpath_skills, sep=',')
    df_courses = pd.read_csv(fpath_courses, sep=',')
    test_list = []
    for _, c_row in df_courses.iterrows():
        c_wgtd_score = 0
        c_wgtd_score2 = 0
        for _, s_row in df_skills.iterrows():
            if s_row['Role'] == 'Data Scientist':
                # print(c_row['Course Description'].encode('utf-8'))
                c_wgtd_score = c_wgtd_score + (
                    cosine_sim(
                               str(s_row['Skills']).encode('utf-8'),
                               str(c_row['Course Name']).encode('utf-8'))
                               * s_row['SkillWeight'])
                c_wgtd_score2 = c_wgtd_score2 + (
                    cosine_sim(
                               str(s_row['Skills']).encode('utf-8'),
                               str(c_row['Course Description']).encode('utf-8'))
                               * s_row['SkillWeight'])                               
        # print(c_wgtd_score)
        test_list.append((c_row['Course Id'], c_wgtd_score, c_wgtd_score2))
    with open("././Data/temp_output.csv",'w') as result:
        csv_out = csv.writer(result)
        csv_out.writerow(['Course Id','CategoryCS', 'DescriptionCS'])
        for row in test_list:
            csv_out.writerow(row)
    return None


print(execute_cosine('././Data/temp.csv', '././Data/main_coursera.csv'))
# print(cosine_sim('Data Science', 'Data'))
# print(cosine_sim('hello world .', 'This sentence is similar to a foo bar sentence'))
# linkedin_skills_weighted