
from PyQt5 import QtCore, QtGui, QtWidgets
from IntrusionDetect import Ui_IntrusionDetect
import sys
from DataPreprocess import preprocess
from sklearn.model_selection import train_test_split
import pandas as pd
from RF import rf_evaluation
from SVM import svm_evaluation
from DNN import dnn_evaluation

class Ui_Main(object):


    def data_preprocessing(self):

        preprocess("KDDTrain.csv")

        self.showMessageBox("Information", "Data Preprocessing Completed..! ")


    def split_dataset(self):

        global X_train, X_test, y_train, y_test

        df = pd.read_csv("features.csv")
        y = df["attack_class"]  # target column i.e class

        del df["attack_class"]

        X = df  # independent columns

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        self.showMessageBox("Information", "Dataset Spliting Completed..! ")



    def Detection(self):
        try:
            self.ni = QtWidgets.QDialog()
            self.ui = Ui_IntrusionDetect()
            self.ui.setupUi(self.ni)
            self.ni.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def runSVMAlg(self):

        try:
            global accuracy_svm

            accuracy_svm=svm_evaluation(X_train, X_test, y_train, y_test)

            self.showMessageBox("Information", "SVM Algorithm Evaluations Completed..! ")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def runRFAlg(self):

        try:
            global accuracy_rf

            accuracy_rf=rf_evaluation(X_train, X_test, y_train, y_test)

            self.showMessageBox("Information", "RF Algorithm Evaluations Completed..! ")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def runDNNAlg(self):

        try:

            global accuracy_dnn

            accuracy_dnn = dnn_evaluation(X_train, X_test, y_train, y_test)

            self.showMessageBox("Information", "DNN Algorithm Evaluations Completed..! ")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def graph(self):
        import matplotlib.pyplot as plt
        import numpy as np

        print(accuracy_svm, accuracy_rf, accuracy_dnn)

        height=[accuracy_svm, accuracy_rf, accuracy_dnn]
        bars = ('SVM Accuracy', 'Random Forest Accuracy', 'DNN Accuracy')
        y_pos = np.arange(len(bars))
        plt.bar(y_pos, height, color=['blue','red','green'])
        plt.xticks(y_pos, bars)
        plt.xlabel('Algorithms')
        plt.ylabel('Accuracy')
        plt.title('ML & DL Analysis with Accuracy')

        '''height = [accuracy_svm, accuracy_rf, accuracy_dnn]
        bars = ('SVM Accuracy', 'Random Forest Accuracy', 'DNN Accuracy')
        y_pos = np.arange(len(bars))

        plt.bar(y_pos, height)
        plt.xticks(y_pos, bars)'''
        plt.show()






    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(975, 750)
        Dialog.setStyleSheet("")
        Dialog.setStyleSheet("background-color: rgb(199, 99, 74);")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(48, 20, 891, 101))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 20pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.label.setText("")


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 180, 265, 61))
        self.pushButton.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.data_preprocessing)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 180, 265, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.split_dataset)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 298, 265, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.runSVMAlg)


        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 298, 265, 61))
        self.pushButton_4.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.runRFAlg)


        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 410, 265, 61))
        self.pushButton_5.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.runDNNAlg)


        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 410, 265, 61))
        self.pushButton_6.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.graph)


        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 520, 265, 61))
        self.pushButton_7.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.Detection)





        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label.setText(_translate("Dialog", "Intrusion Detection System using Deep Neural Networks"))
        self.pushButton.setText(_translate("Dialog", "Data Preprocessing"))
        self.pushButton_2.setText(_translate("Dialog", "Split Dataset"))

        self.pushButton_3.setText(_translate("Dialog", "Run SVM Algorithm"))

        self.pushButton_4.setText(_translate("Dialog", "Run RF Algorithm"))

        self.pushButton_5.setText(_translate("Dialog", "Run DNN Algorithm"))

        self.pushButton_6.setText(_translate("Dialog", "Accuracy Graph"))

        self.pushButton_7.setText(_translate("Dialog", "Intrusion Detection"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
