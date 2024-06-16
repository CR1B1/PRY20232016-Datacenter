import pickle
import os
import tensorflow as tf
import numpy as np
#import tensorflow_addons as tfa
from keras.preprocessing.sequence import pad_sequences

FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")

def normalizer(a):
    b = np.zeros_like(a)
    b[np.arange(len(a)), a.argmax(1)] = 1
    return b

def get_features(text_series, tokenizer, maxlen):
    sequences = tokenizer.texts_to_sequences(text_series)
    return pad_sequences(sequences=sequences)

def predict_labels(predictions:list, mlb):
    return [(mlb.inverse_transform(prediction.reshape(1,-1))) for i,prediction in enumerate(predictions)]

def priority_prediction(incidence:str)->str:
    model = tf.keras.models.load_model(
        FOLDER + "/ia_gestion_incidencias_prioridad.h5", custom_objects=None, compile=False)  # , custom_objects={'F1Score':f1})
    loaded_model = tf.keras.models.load_model(
        os.path.join(FOLDER, "vectorizer-model"))
    vectorizer = loaded_model.layers[0]
    x_ = vectorizer(np.array([incidence]))
    y_pred = model.predict(x_)
    mlb = pickle.load(open(FOLDER + "/MultiLabelBinarizer.pk", 'rb'))
    y_pred = predict_labels(normalizer(y_pred), mlb)
    y_pred = np.unique(y_pred)
    return y_pred[0].upper()