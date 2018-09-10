import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import nltk.data
import logging
from gensim.models import word2vec
nltk.download()


my_fpath_courses = "../Data/main_coursera.csv"

course_data = pd.read_csv(my_fpath_courses)


def clean(course_desc, remove_stopwords=True):
    course_desc = BeautifulSoup(course_desc).get_text()
    course_desc = re.sub("[^a-zA-Z]"," ", course_desc)
    words = course_desc.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return(words)