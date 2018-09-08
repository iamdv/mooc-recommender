# import pandas as pd
# import re
# from nltk.corpus import stopwords
# import gensim
# import os

# course_desc = "Learn about the most effective data analysis methods to solve problems and achieve insight"
# course_desc = course_desc.split()

# base_path = './Data/'


# # import the pre-trained model to remove the words not in the vocabulary. We're using the open source google model trained on millions of news articles.
# model = gensim.models.KeyedVectors.load_word2vec_format(base_path+"/GoogleNews-vectors-negative300.bin",binary=True)

# # load the course data
# skill = ['data','scientist', 'mining', 'python', 'sql', 'programming', 'latex', 'statistics']
# newskill = [skill.append(word) for word in skill if word in model.vocab]
# sim = model.n_similarity(newskill, course_desc)

# print(skill)
# print(sim)

test = ['a', 'b', 'c']
test2 = ['d']
print(test + test2)