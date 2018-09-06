import pandas as pd
import re
from nltk.corpus import stopwords
import gensim
import os


base_path = './Data/'

'''
Import the pre-trained model to remove the words not in the vocabulary.
We will use the open source google model trained on millions of news articles.
'''

model = gensim.models.KeyedVectors.load_word2vec_format(
    base_path + "GoogleNews-vectors-negative300.bin", binary = True)

sim = model.n_similarity(['data', 'science'],['data', 'scientist'])

print(base_path)