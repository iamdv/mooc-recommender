from bs4 import BeautifulSoup
import os.path
import requests
import lxml
import html5lib
import json
import csv


def get_linkedin_profiles(uri):
    '''
    Open the html page and read the file using BS4 html.parser
    find all the skills in the page.

    This function return a list of tupes in the following format
    [
        ('Data Science', 'Skill', Score, 'Profile Name'),
        ('Software Engineer', 'Skill', Score, 'Profile Name'),
        ('Acocuntant', 'Skill', Score, 'Profile Name')
    ]
    '''
    my_output_list = []
    my_role = os.path.basename(uri).split('-')[0].strip()
    my_skill = ''
    my_score = 0
    my_name = os.path.basename(uri).split('-')[1].split('.')[0].strip()

    with open(uri, encoding="utf-8") as input_file:
        data = input_file.read()
        soup = BeautifulSoup(data, 'html.parser')
    all_skills = soup.find_all('a')
    
    for each_skill in all_skills:
        skill = each_skill.find('span', {'class': 'visually-hidden'})
        if skill is not None:
            my_score = skill.text.split(' ')[1]
            my_skill = skill.text.replace('for', '|').split('|')[1].strip()
            my_output_list.append(tuple((my_role, my_skill, my_score, my_name)))

    with open('eggs.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

print(get_linkedin_profiles("/Users/DV/GitHub/mooc-recommender/Web-Scrapper/LinkedInProfiles/Data Scientist - Aleksandra Iljina.html"))
