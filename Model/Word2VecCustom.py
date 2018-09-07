import pandas as pd
import re
from nltk.corpus import stopwords
import gensim
import os


base_path = './Data/'

# import the pre-trained model to remove the words not in the vocabulary. We're using the open source google model trained on millions of news articles.
model = gensim.models.KeyedVectors.load_word2vec_format(base_path+"/GoogleNews-vectors-negative300.bin",binary=True)

# load the course data

sim = model.n_similarity(['data','scientist'],['data','science'])

print(sim)