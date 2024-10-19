
from sklearn.svm import SVC
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score,confusion_matrix

import os
import pickle
def svm_evaluation(X_train, X_test, y_train, y_test):



    if os.path.exists("../IntrusionDetection/svm_model.pkl"):

        svm_model = pickle.load(open('svm_model.pkl', 'rb'))

        predicted = svm_model.predict(X_test)

        accuracy = accuracy_score(y_test, predicted)*100

        

        print("SVM Evaluation:")
        print("================")
        print("Accuracy:",accuracy)
        
    else:
        svm_clf = SVC(gamma='auto',C=2.0,)

        svm_clf.fit(X_train[0:500], y_train[0:500])

        with open('svm_model.pkl', 'wb') as f:
                pickle.dump(svm_clf, f)

        predicted = svm_clf.predict(X_test)

        accuracy = accuracy_score(y_test, predicted)*100

        

        print("SVM Evaluation:")
        print("================")
        print("Accuracy:",accuracy)
       

 
    return accuracy





