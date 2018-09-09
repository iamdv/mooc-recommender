import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import string
import csv

pd.set_option('display.max_columns', 10)
nltk.download('stopwords')


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


def execute_cosine(fpath_skills, fpath_courses, my_role, output_fname):
    df_skills = pd.read_csv(fpath_skills, sep=',')
    df_skills = df_skills[(df_skills['Role'] == my_role)]
    df_courses = pd.read_csv(fpath_courses, sep=',')

    cosine_score = []
    for _, c_row in df_courses.iterrows():
        c_wgtd_role_score = 0
        c_wgtd_skill_score = 0
        c_wgtd_keyword_score = 0
        skill_group = ''
        course_text = (str(c_row['Category']) + ' '
        + str(c_row['Course Name']) + ' '
        + str(c_row['Course Description'])).lower().encode('utf-8')

        course_keywords = str(c_row['Course Keywords']).replace(' | ', ',').lower()

        for _, s_row in df_skills.iterrows():
            skill = str(s_row['Skills']).encode('utf-8')
            skill_group = skill_group + ', ' + str(s_row['Skills']).lower()
            skill_weight = s_row['SkillWeight']
            
            c_wgtd_skill_score =  c_wgtd_skill_score + (cosine_sim(skill, course_text) * skill_weight)
            c_wgtd_role_score = cosine_sim(str(s_row['Role']).lower(), str(c_row['Course Name']).lower())
            c_wgtd_keyword_score = cosine_sim(skill_group, course_keywords)
            # print(c_row['Course Id'], skill_group)
            # print(c_wgtd_keyword_score)
        
        cosine_score.append((c_row['Course Id'], my_role, c_wgtd_skill_score, c_wgtd_role_score, c_wgtd_keyword_score))
    
    with open("././Data/Cosine-Distance/Single-Variable/" + output_fname,'w') as result:
        csv_out = csv.writer(result)
        csv_out.writerow(['Course Id', 'Role', 'Skill_Score','Role_Score', 'Keyword_Score'])
        for row in cosine_score:
            csv_out.writerow(row)   
    return None


print(execute_cosine('././Data/linkedin_skills_weighted.csv',
'././Data/main_coursera.csv', 'software development', 'CosDist_SoftwareDevelopment.csv'))

