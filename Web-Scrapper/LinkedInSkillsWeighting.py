import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import string
import csv

pd.set_option('display.max_columns', 10)

def get_skill_listing(file_path, file_name):
    """
    Extracts the skill listing data from the CSV file
    and the endorsement score as the skill weighting
    :param text1: File path
    :return: returns the probabilistic measure of similarity.
    """
    df_skills = pd.read_csv(file_path + file_name, sep=',',
                            names=["Role", "Skills", "Endorsements", "Name"])

    df_sum_skills = df_skills.groupby(['Role', 'Skills'])['Endorsements'].sum().reset_index(name ='SkillEndorsements')
    df_sum_skills.columns = ['Role', 'Skills', 'SkillEndorsements']
    df_sum_skills = df_sum_skills.sort_values(['Role', 'SkillEndorsements'], ascending = [True, False])
    df_sum_skills = df_sum_skills.groupby('Role').head(10).reset_index(drop = True)
    df_sum_skills['RoleTotal'] = df_sum_skills['SkillEndorsements'].groupby(df_sum_skills['Role']).transform('sum')
    df_sum_skills['SkillWeight'] = (df_sum_skills['SkillEndorsements'] / df_sum_skills['RoleTotal'])
    df_sum_skills['Skills'] = df_sum_skills['Skills'].str.lower()
    df_sum_skills['Role'] = df_sum_skills['Role'].str.lower()
    df_sum_skills.to_csv(file_path + 'linkedin_skills_weighted.csv', sep=',', encoding='utf-8')
    return None


get_skill_listing('./Data/', 'linkedin_skills.csv')