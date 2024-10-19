import pandas as pd
import numpy as np

from sklearn import metrics
import warnings
import sys
#from DTC import dt_evaluation
#from RFC import rfc_evaluation

#from LR import lr_evaluation
from sklearn import svm
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from FeatureSelection import getFeatures

def preprocess(training):

    print("Start preprocess...")
    datacols = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","attack", "last_flag"]

    # Load NSL_KDD train dataset
    dfkdd_train = pd.read_csv(training, sep=",", names=datacols) # change path to where the dataset is located.
    dfkdd_train = dfkdd_train.iloc[:,:-1] # removes an unwanted extra field

   

    dfkdd_train['attack_class'] = dfkdd_train['attack']

    unique_classes = dfkdd_train['attack_class'].nunique()

    print(unique_classes)


    dfkdd_train.drop(['attack'], axis=1, inplace=True)

  
    
    #'num_outbound_cmds' field has all 0 values, so drop it
    dfkdd_train.drop(['num_outbound_cmds'], axis=1, inplace=True)
    

    dfkdd_train.drop(['protocol_type'], axis=1, inplace=True)
  

    dfkdd_train.drop(['service'], axis=1, inplace=True)
  

    dfkdd_train.drop(['flag'], axis=1, inplace=True)

    #dfkdd_train.to_csv("dataset.csv",index=False)


    getFeatures(dfkdd_train)
    
  

#preprocess("KDDTrain.txt")

