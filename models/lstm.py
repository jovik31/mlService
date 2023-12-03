
from keras.src.layers.attention.multi_head_attention import activation
import tensorflow as tf
import keras
import json


def decodeJSON(file_name):

    return json.load(file_name)


class LSTM_Model(keras.Model):

    def __init__(self, file_name):

        super(LSTM_Model, self).__init__()
        parameters = decodeJSON(file_name)
        self.lstm = keras.layers.LSTM(
            parameters['lstm_neurons'], activation=parameters['lstm_activation'])
        self.bn = keras.layers.BatchNormalization()

        if "droupout_rate" in parameters:
            self.dp1 = keras.layers.Dropout(parameters['droupout_rate'])
            self.dp2 = keras.layers.Dropout(parameters['droupout_rate'])
            self.dp3 = keras.layers.Dropout(parameters['droupout_rate'])

        for layer in parameters['dense_layers']:

            self.dense1 = keras.layers.Dense(
                layer['neurons'], activation=layer['activation'])
            self.bn1 = keras.layers.BatchNormalization()

            self.dense2 = keras.layers.Dense(
                layer['neurons'], activation=layer['activation'])
            self.bn2 = keras.layers.Dense(
                layer['neurons'], activation=layer['activation'])

        self.out = keras.layers.Dense(
            parameters['output_size'], activation='sigmoid')
