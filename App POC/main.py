import pandas as pd
import interface
import data_preperation
from train_model import train
import use_model

def main():
    inter = interface.interface()
    filepath = inter.openwindow()
    corpus = pd.read_csv(filepath)
    corpus = data_preperation.prep.text_prep(corpus)
    print(corpus)
    if decision == "train":
        t = train()
        SVMmodel = t.SVM_train(corpus)
        NBmodel = t.NB_train(corpus)
        train_model.train.save_model(SVMmodel, "./Models/SVMcorpus")
        train_model.train.save_model(NBmodel, "./Models/NBcorpus")
    elif decision == "predict":
        SVMpmodel = use_model.predict.load_model("./Models/SVMcorpus")
        NBpmodel =  use_model.predict.load_model("./Models/NBcorpus")
        NBpredicted_corpus = use_model.predict.NB_predict(corpus, NBpmodel)
        SVMpredicted_corpus = use_model.predict.SVM_predict(corpus, SVMpmodel)
        return True

decision = "train"
#if __name__ == '__main__':
main()
