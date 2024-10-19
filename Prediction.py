import pandas as pd
import numpy as np

#from keras.models import load_model

import tensorflow as tf

def detection(testing_file):


    int2label = {0:"back", 1:"buffer_overflow", 2:"ftp_write", 3:"guess_passwd", 4:"imap",5:"ipsweep", 6:"land" , 
              7:"loadmodule" , 8:"multihop" , 9:"neptune" ,10:"nmap" ,11:"normal" , 12:"perl" , 13:"phf" , 
              14:"pod", 15:"portsweep" , 16:"rootkit" , 17:"satan" , 18:"smurf" , 19:"spy" , 
              20:"teardrop",21:"warezclient" , 22:"warezmaster" }

    testing_df = pd.read_csv(testing_file, sep=',')

    testing_df = testing_df.iloc[:, :-1]

   
    model_path = 'dnn_model.h5'

    dnn_model = tf.keras.models.load_model(model_path)

    pred_res = np.argmax(dnn_model.predict(testing_df), axis=1)

    print(pred_res)

    pred_res=int2label[pred_res[0]]

   
    return pred_res


