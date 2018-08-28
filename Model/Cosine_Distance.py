import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import string
import csv


def normalize(text):
    """
    Normalizes the text to remove the capital letters and punctuations
    as they hinder textual anyalsis.
    :param text: search text
    :return: returns the normalized text.
    """
    nltk.download('stopwords')
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
    for s_index, s_row in df_skills.iterrows():
        if s_row['Role'] == 'Data Scientist':
            for c_index, c_row in df_courses.iterrows():
                
            # print(row['Skills'], row['SkillWeight'])


execute_cosine('././Data/linkedin_skills_weighted.csv', '././Data/main_coursera.csv')
