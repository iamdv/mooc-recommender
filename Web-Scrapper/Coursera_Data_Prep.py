import pandas as pd
import nltk
import string
import csv
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.util import bigrams


def extract_keywords(fpath_courses, fpath_skills):
    df_courses = pd.read_csv(fpath_courses, sep=',')
    df_courses['Course Keywords'] = ''
    df_skills = pd.read_csv(fpath_skills, sep=',',
                            names=["Role", "Skills", "Endorsements", "Name"])
    # df_courses = df_courses[(df_courses['Category'] == 'Data Science')]
    # df_skills = df_skills[(df_skills['Role']== 'Data Scientist')]
    skills_master = list(set(df_skills['Skills'].str.lower().tolist()))
    # print(skills_master)

    for c_idx, c_row in df_courses.iterrows():
        course_text_master = []
        course_text = (str(c_row['Category']) + ' '
        + str(c_row['Course Name']) + ' '
        + str(c_row['Course Description']))
        
        # Remove stop words and punctuations from the course text
        stop = stopwords.words('english') + list(string.punctuation)
        course_text = [i for i in word_tokenize(course_text.lower()) if i not in stop]

        # Convert course descripton into bigrams
        course_text_bigrm = list(nltk.bigrams(course_text))
        course_text_bigrm = list(map(" ".join,course_text_bigrm))

        # Combine the single words and bigrams into one master list
        # and take only the words are in skills
        for my_keyword in course_text + course_text_bigrm:
            if my_keyword in skills_master:
                course_text_master.append(my_keyword)

        df_courses.set_value(c_idx, 'Course Keywords', ' | '.join(course_text_master))

    # df_courses = df_courses.reset_index(drop=True)
    df_courses = df_courses.drop(df_courses.columns[df_courses.columns.str.contains('unnamed',case = False)],axis = 1)
    df_courses.to_csv(fpath_courses, sep=',', encoding='utf-8')
    return None


extract_keywords('././Data/Main_Coursera.csv', '././Data/linkedin_skills.csv')