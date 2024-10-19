from PyQt5 import QtCore, QtGui, QtWidgets
from Prediction import detection
import sys
class Ui_IntrusionDetect(object):


    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()



    def browsefile_test(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select testing File", "*.csv")
        print(fileName)
        self.lineEdit.setText(fileName)


    def intrusion_detection(self):
        try:

            testSet = self.lineEdit.text()

            if testSet== "null" or testSet=="":
                self.alertmsg("Failed","Please select the Testing File")
            else:
                print("Start Detecting...")
              
                result = detection(testSet)
                print(result)
                self.label_4.setText(str(result))
        except Exception as e:
            print("Error=", e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(727, 494)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 40, 421, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 130, 241, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 160, 341, 41))
        self.lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 160, 111, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefile_test)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 230, 131, 41))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.intrusion_detection)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 320, 241, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        '''self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 290, 361, 101))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_2.setObjectName("lineEdit_2")'''


        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 300, 241, 51))
        self.label_4.setStyleSheet("color: rgb(#f08080);\n"
"font: 20pt \"Georgia\";")
        self.label_4.setObjectName("label_4")



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Intrusion Detection"))
        self.label.setText(_translate("Dialog", "Intrusion Detection"))
        self.label_2.setText(_translate("Dialog", "Testing Dataset"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Detection"))
        self.label_3.setText(_translate("Dialog", "Detection Results  : "))
        self.label_4.setText(_translate("Dialog", ""))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_IntrusionDetect()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
