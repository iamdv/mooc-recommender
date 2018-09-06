import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import nltk.data
nltk.download() 
import logging
from gensim.models import word2vec



# Read data from course file through pandas


def clean_description(course_desc, remove_stopwords = True):
    
    
    course_desc = re.sub("[^a-zA-Z]"," ", course_desc)
    #
    # 3. Convert words to lower case and split them
    words = course_desc.lower().split()
    #
    # 4. Optionally remove stop words (True by default)
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    #
    # 5. Return a list of words
    return(words)

  
'''
# Load the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Define a function to split a course descriptions into parsed sentences
def course_desc_to_sentences( course_desc, tokenizer, remove_stopwords=True ):
    # Function to split a review into parsed sentences. Returns a 
    # list of sentences, where each sentence is a list of words
    #
    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(course_desc.strip())
    #
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call clean_description to get a list of words
            sentences.append( clean_description( raw_sentence,remove_stopwords ))
    #
    # Return the list of sentences (each sentence is a list of words,
    # so this returns a list of lists
    return sentences


sentences = []  # Initialize an empty list of sentences

print "Parsing sentences from training set"
for course_desc in course_descriptions:
    sentences += course_desc_to_sentences(course_desc, tokenizer)


# Training and saving the model.

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)

# Set values for various parameters
num_features = 300    # Word vector dimensionality                      
min_word_count = 40   # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

# Initialize and train the model (this will take some time)
print "Training model..."
model = word2vec.Word2Vec(sentences, workers=num_workers,size=num_features, min_count = min_word_count, window = context, sample = downsampling)

model.init_sims(replace=True)
model_name = "300features_40minwords_10context"
model.save(model_name)


# Now the saved model can be used just like the pre-trained google model. 

'''
