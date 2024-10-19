
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score,confusion_matrix
import numpy as np
import pickle
import os

def rf_evaluation(X_train, X_test, y_train, y_test):

    X_train = X_train + np.random.normal(7.9, 2.3, size=X_train.shape)


    if os.path.exists("../IntrusionDetection/rfst_model.pkl"):
       
        
        RF_model = pickle.load(open('rfst_model.pkl', 'rb'))
        
        
        predicted = RF_model.predict(X_test)
       

        accuracy = accuracy_score(y_test, predicted)*100

        

        print("RF Evaluation:")
        print("================")
        print("Accuracy:",accuracy)
        
    else:
        
        rf_clf = RandomForestClassifier()

        rf_clf.fit(X_train, y_train)

        with open('rfst_model.pkl', 'wb') as f:
                pickle.dump(rf_clf, f)

        predicted = rf_clf.predict(X_test)

        accuracy = accuracy_score(y_test, predicted)*100

        
        print("RF Evaluation:")
        print("================")
        print("Accuracy:",accuracy)
       
    return accuracy





