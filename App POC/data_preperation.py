import pandas as pd
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords

class prep():
    def text_prep(corpus):
        # Remove blank rows
        corpus['text'].dropna(inplace=True)
        # Change all text to lower case
        corpus['text'] = [entry.lower() for entry in corpus['text']]
        # Tokenization
        corpus['text']= [word_tokenize(entry) for entry in corpus['text']]
        # Remove stop words, non-numeric and perfom Word Stemming/Lemmenting.
        tag_map = defaultdict(lambda : wn.NOUN)
        tag_map['J'] = wn.ADJ
        tag_map['V'] = wn.VERB
        tag_map['R'] = wn.ADV
        for index,entry in enumerate(corpus['text']):
            Final_words = []
            word_Lemmatized = WordNetLemmatizer()
            for word, tag in pos_tag(entry):
                if word not in stopwords.words('english') and word.isalpha():
                    word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
                    Final_words.append(word_Final)
            corpus.loc[index,'text_final'] = str(Final_words)
            return corpus