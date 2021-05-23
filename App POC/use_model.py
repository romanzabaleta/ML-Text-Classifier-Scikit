import pandas as pd
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
import joblib
from sklearn.metrics import accuracy_score

filepath = interface.openwindow()
corpus = pd.read_csv(filepath)