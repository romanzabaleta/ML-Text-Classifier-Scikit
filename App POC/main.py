import pandas as pd
import interface as intf
import data_preperation as dp
import train_model as tm
import use_model as um

def main():
    inter = intf.interface()
    filepath = inter.openwindow()
    corpus = pd.read_csv(filepath)
    corpus = dp.prep.text_prep(corpus)
    print(corpus)
    if decision == "train":
        t = tm.train()
        SVMmodel = t.SVM_train(corpus = corpus)
        NBmodel = t.NB_train(corpus = corpus)
        tm.train.save_model(SVMmodel, "./Models/SVMcorpus")
        tm.train.save_model(NBmodel, "./Models/NBcorpus")
    elif decision == "predict":
        #SVMmodel = um.predict.load_model("./Models/SVMcorpus")
        #NBmodel =  um.predict.load_model("./Models/NBcorpus")
        #NBpredicted_corpus = um.predict.NB_predict(corpus, NBmodel)
        #SVMpredicted_corpus = um.predict.SVM_predict(corpus, SVMmodel)
        return True

decision = "train"
#if __name__ == '__main__':
main()