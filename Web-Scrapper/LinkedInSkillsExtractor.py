#!/Users/dv/anaconda/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import lxml
import html5lib
import json
import csv

#############################################################################


#############################################################################
def get_linkedin_profiles(uri):
    '''
    Open the html page and read the file using BS4 html.parser
    find all the skills in the page
    '''
    with open(uri, encoding="utf-8") as input_file:
        data = input_file.read()
        soup = BeautifulSoup(data, 'html.parser')
    all_skills = soup.find_all('a')

    for each_skill in all_skills:
        skill = each_skill.find('span', {'class': 'visually-hidden'})
        if skill is not None:
            print(skill.text)

#############################################################################


get_linkedin_profiles('./LinkedInProfiles/Data Scientist - Andriy Burkov.html')
