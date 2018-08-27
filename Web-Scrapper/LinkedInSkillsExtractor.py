from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import os.path
import requests
import lxml
import html5lib
import json
import csv


def get_all_files(path):
    '''
    Extract all file paths from the respective folder
    :param text1: File path
    :return: <List> returns a list of file paths and names. 
    '''
    my_file_list = [path + '/' + f for f in listdir(path)
                    if isfile(join(path, f))]
    return my_file_list


def get_skills(uri):
    '''
    Open the html page and read the file using BS4 html.parser
    Extract all the roles, skills, endorsements, profile_name
    :param: URI of the html page
    :return: <None> but store the data in the CSV file
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

    with open('././Data/linkedin_skills.csv', 'a') as csvfile:
        for each_skill in all_skills:
            skill = each_skill.find('span', {'class': 'visually-hidden'})
            if skill is not None:
                my_score = skill.text.split(' ')[1]
                my_skill = skill.text.replace('for', '|').split('|')[1].strip()
                my_output_list.append(
                    tuple((my_role, my_skill, my_score, my_name)))
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([my_role, my_skill, my_score, my_name])
        csvfile.close()
    return None


def store_skills_csv(files):
    for each_file in files:
        get_skills(each_file)
    return None

my_file_path = get_all_files(
    '/Users/DV/GitHub/mooc-recommender/Web-Scrapper/LinkedInProfiles')
store_skills_csv(my_file_path)
