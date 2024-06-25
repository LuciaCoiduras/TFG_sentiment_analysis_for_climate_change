import nltk

nltk.download('stopwords')
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from nltk.corpus   import stopwords
from nltk.stem     import PorterStemmer

import spacy
import string
import re

nlp = spacy.load("es_core_news_sm")

def to_lower(text):
    return text.lower()

def remove_punctuation_and_hyphons(text):
    text = text.translate(str.maketrans('', '', string.punctuation + ''.join(['¡', '¿'])))
    return text.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')

def remove_twitter_patterns(text):
    # Replace user tags
    text = re.sub(r'@(\w+)', ' ', text)
    # Replace urls
    text = re.sub(r'http\S+', ' ', text)
    # Replace hashtags
    text = re.sub(r'#', '', text)
    return text

def split_in_tokens(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('spanish'))
    return [t for t in tokens if t not in stop_words]

def merge_tokens(tokens):
    return ' '.join(tokens)

def stemming(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

def lemming(tokens):
    lemmas = []
    for stem in tokens:
        doc = nlp(stem)
        lemma = doc[0].lemma_
        lemmas.append(lemma)
    return lemmas

def preprocess_text(text, steps = ['to_lower','remove_punctuation_and_hyphons','remove_twitter_patterns', 'split_in_tokens','remove_stopwords','merge_tokens', 'stemming','lemming']):

    if 'to_lower' in steps:
        text = to_lower(text)

    if 'remove_punctuation_and_hyphons' in steps:
        text = remove_punctuation_and_hyphons(text)

    if 'remove_twitter_patterns' in steps:
        text = remove_twitter_patterns(text)

    if 'split_in_tokens' in steps:
        text = split_in_tokens(text)
    
    if 'remove_stopwords' in steps:
        text = remove_stopwords(text)
    
   # if 'stemming' in steps:
    #    text = stemming(text)
    
    if 'lemming' in steps:
        text = lemming(text)
    
    if 'merge_tokens' in steps:
        text = merge_tokens(text)
        
    return text