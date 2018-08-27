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


def get_skill_listing(file_path, *args):
    """
    Extracts the skill listing data from the CSV file
    and the endorsement score as the skill weighting
    :param text1: File path
    :return: returns the probabilistic measure of similarity.
    """
    df_skills = pd.read_csv(file_path, sep=',',
                            names=["Role", "Skills", "Endorsements", "Name"])

    df_sum_skills = df_skills.groupby(['Role', 'Skills'])['Endorsements'].sum().reset_index(name ='SkillEndorsements')
    df_sum_skills.columns = ['Role', 'Skills', 'SkillEndorsements']
    df_sum_skills['RoleTotal'] = df_sum_skills['SkillEndorsements'].groupby(df_sum_skills['Role']).transform('sum')
    df_sum_skills['SkillWeight'] = (df_sum_skills['SkillEndorsements'] / df_sum_skills['RoleTotal'])
    
    return None
    # print(df_sum_skills[df_sum_skills[Skills] == 'Python'])


get_skill_listing('./Data/linkedin_skills.csv', 'Data Scientist')