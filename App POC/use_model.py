import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

class predict():
    def NB_predict(corpus, model):
        # Predict the categories of the test data
        prediction = model.predict(corpus['text_final'])
        corpus['NB prediction'] = prediction
        return corpus
    def SVM_predict(corpus, model):
        # Predict the categories of the test data
        prediction = model.predict(corpus['text_final'])
        corpus['SVM prediction'] = prediction
        corpus['SVM probability'] = [[max(i)] for i in model.predict_proba(prediction)]        
        return corpus
    def load_model(model_name):
        model = joblib.load(model_name)
        return model
    #def accuraccy_score