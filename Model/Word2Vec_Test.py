import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import string
import gensim
import os
import csv
import re
from gensim.models import Word2Vec


pd.set_option('display.max_columns', 10)
base_path = './Data/'


'''
Import the pre-trained model to remove the words not in the vocabulary.
We will use the custom word2vec model.
'''
model = Word2Vec.load(base_path + "300features_40minwords_10context_courses")


def word2vec_similarity(my_skills, my_coursedesc):
    return model.n_similarity(my_skills, my_coursedesc)


test = "health care biology".split()
print(word2vec_similarity(['google'], test))


def run_word2vec(fpath_skills, fpath_courses, my_role, output_fname):
    stop = stopwords.words('english') + list(string.punctuation)
    df_skills = pd.read_csv(fpath_skills, sep=',')
    df_skills = df_skills[(df_skills['Role'] == my_role)]
    df_courses = pd.read_csv(fpath_courses, sep=',')
    course_text_final = []

    word2vec_score = []

    for _, c_row in df_courses.iterrows():
        c_wgtd_role_score = 0
        c_wgtd_skill_score = 0
        c_wgtd_keyword_score = 0
        course_text = (str(c_row['Category']) + ' '
        + str(c_row['Course Name']) + ' '
        + str(c_row['Course Description']))

        course_text = [i for i in word_tokenize(course_text.lower()) if i not in stop]
        course_text = [word for word in course_text if word in model]

        for _, s_row in df_skills.iterrows():
            skill = str(s_row['Skills']).strip()
            skill_weight = s_row['SkillWeight']
            skill_group = []
            role_list = str(s_row['Role']).split()
            course_name_list = str(c_row['Course Name'])

            course_name_list = [i for i in word_tokenize(course_name_list.lower()) if i not in stop]
            course_name_list = [word for word in course_name_list if word in model]
                      
            skill = [i for i in word_tokenize(skill.lower()) if i not in stop]
            # skill = [word for word in skill if word in model.vocab]

            if skill[0] in model:
                skill_group.append(skill[0])
                # print('Valid Skill: ', skill[0])
                try:
                    c_wgtd_skill_score = c_wgtd_skill_score + (word2vec_similarity(skill + role_list, course_text) * skill_weight)
                    c_wgtd_role_score = word2vec_similarity(skill + role_list, course_name_list)
                    c_wgtd_keyword_score = word2vec_similarity(skill_group, course_name_list)
                except:
                    pass
            else:
                pass
                # print('Not a valid skill: ', skill[0])
            
        word2vec_score.append((c_row['Course Id'], my_role, c_wgtd_skill_score, c_wgtd_role_score, c_wgtd_keyword_score))

    with open("././Data/Word2Vec-Custom/" + output_fname,'w') as result:
        csv_out = csv.writer(result)
        csv_out.writerow(['Course Id', 'Role', 'Skill_Score','Role_Score', 'Keyword_Score'])
        for row in word2vec_score:
            csv_out.writerow(row) 
    return None


print(run_word2vec('././Data/linkedin_skills_weighted.csv',
'././Data/Main_Coursera.csv', 'data scientist', 'Word2VecCustom_DataScientist.csv'))
