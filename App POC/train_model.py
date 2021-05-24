import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
import joblib

class train():
    def SVM_train(corpus):
        # Build the model
        SVMmodel = make_pipeline(TfidfVectorizer(), svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto', probability=True))
        # Train the model using the training data
        SVMmodel.fit(corpus['text_final'], corpus['classification'])
        return SVMmodel
    def NB_train(corpus):
        # Build the model
        NBmodel = make_pipeline(TfidfVectorizer(), naive_bayes.MultinomialNB())
        # Train the model using the training data
        NBmodel.fit(corpus['text_final'], corpus['classification'])
        return NBmodel
    def save_model(model,model_name):
        joblib.dump(model, model_name)
        return model_name
    #def test_model