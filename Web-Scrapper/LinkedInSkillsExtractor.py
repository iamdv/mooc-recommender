#!/Users/dv/anaconda/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import lxml
import html5lib
import json
import csv


#############################################################################
'''
get_linkedin_skills function extracts all the skills from
top linkedin profiles for each role.
'''


def get_linkedin_profiles(uri):
    with open(uri, encoding="utf-8") as input_file:
        data = input_file.read()
        soup = BeautifulSoup(data, 'html.parser')
    all_skills = soup.find_all('a')
    for each_skill in all_skills:
        skill = each_skill.find('span', {'class': 'visually-hidden'})
        if skill is not None:
            print(skill)


get_linkedin_profiles('./LinkedInProfiles/Data Scientist - Andriy Burkov.html')
