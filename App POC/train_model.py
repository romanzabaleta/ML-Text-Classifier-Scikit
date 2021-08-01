import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
import joblib

class train():
    def SVM_train(self, data):
        # Build the model
        self.SVMmodel = make_pipeline(TfidfVectorizer(), svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto', probability=True))
        # Train the model using the training data
        self.SVMmodel.fit(data['text_final'], data['classification'])
        return self.SVMmodel
    def NB_train(data):
        # Build the model
        NBmodel = make_pipeline(TfidfVectorizer(), naive_bayes.MultinomialNB())
        # Train the model using the training data
        NBmodel.fit(data['text_final'], data['classification'])
        return NBmodel
    def save_model(model,model_name):
        joblib.dump(model, model_name)
        return model_name
    #def test_model