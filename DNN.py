

from sklearn.metrics import  accuracy_score, recall_score,confusion_matrix
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
import numpy as np
#from keras.models import load_model
from tensorflow.keras.models import load_model

import os


def dnn_evaluation(X_train, X_test, y_train, y_test):

    label_encoder = LabelEncoder()

    y_train= label_encoder.fit_transform(y_train)

    y_test= label_encoder.fit_transform(y_test)

    if os.path.exists("../IntrusionDetection/dnn_model.h5"):

        model_path = 'dnn_model.h5'
        dnn_model = load_model(model_path)

        predicted = np.argmax(dnn_model.predict(X_test), axis=1)

        accuracy = accuracy_score(y_test, predicted)*100

        
        print("DNN Evaluation:")
        print("================")
        print("Accuracy:",accuracy)
        
    else:
        model = tf.keras.models.Sequential()

        # Input Layer and First Hidden Layer
        model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))

        # Second Hidden Layer
        model.add(tf.keras.layers.Dense(32, activation='relu'))

        # Output Layer (softmax for multiclass classification)
        model.add(tf.keras.layers.Dense(23, activation='softmax'))  # 3 output neurons, one for each class

        # Compile the model
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # Train the model
        model.fit(X_train, y_train, epochs=50, batch_size=32)

        #pred = model.predict(X_test)


        predicted = np.argmax(model.predict(X_test), axis=1)

        accuracy = accuracy_score(y_test, predicted)*100

        
        model.save("dnn_model.h5")

        print("DNN Evaluation:")
        print("================")
        print("Accuracy:",accuracy)
        
    return accuracy





