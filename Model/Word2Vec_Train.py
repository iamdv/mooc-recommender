import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import nltk.data
import logging
from gensim.models import word2vec


my_fpath_courses = "././Data/Main_Coursera.csv"

course_data = pd.read_csv(my_fpath_courses)


def clean(course_desc, remove_stopwords=True):
    course_desc = re.sub("[^a-zA-Z]"," ", course_desc)
    words = course_desc.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return (words)


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


# Define a function to split a course descriptions into parsed sentences
# Function to split a review into parsed sentences. Returns a 
# list of sentences, where each sentence is a list of words
def course_desc_to_sentences( course_desc, tokenizer, remove_stopwords=True ):
    raw_sentences = tokenizer.tokenize(course_desc.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append( clean( raw_sentence,remove_stopwords ))
    return sentences


sentences = []  # Initialize an empty list of sentences
print("Parsing sentences from training set")
for course_desc in course_data['Course Description'].values:
    sentences += course_desc_to_sentences(str(course_desc), tokenizer)


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)

# Set values for various parameters
num_features = 300    # Word vector dimensionality                      
min_word_count = 40   # Minimum word count                        
num_workers = 4     # Number of threads to run in parallel
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

# Initialize and train the model (this will take some time)
print("Training model...")
model = word2vec.Word2Vec(sentences, workers=num_workers,size=num_features, min_count = min_word_count, window = context, sample = downsampling)

model.init_sims(replace=True)
model_name = "././Data/300features_40minwords_10context_courses"
model.save(model_name)


sim = model.n_similarity(['data','science'],['data'])
print(sim)