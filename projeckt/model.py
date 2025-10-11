import tensorflow as tf
from tensorflow.keras.moduls import Sequential
from tensorflow.keras.layers import Dense, LSTM
import numpy as np

def create_module(input_shape):
    model = Sequential([
        LSTM(64, input_shape=input_shape, return_sequence=False),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def prepare_data(series, windows_size=5):
    X,y = [], []
    for i in range(len(series) - windows_size):
        X.append(series[i:i+windows_size])
        y.append(series[i+windows_size])
        return np.array(X), np.array(y)
 
def train_model(model, X, y, epochs=100):
    model.fit(X, y, epochs=epochs, verbose=1)

def predict_next(model, last_sequence):
    last_sequence = np.array(last_sequence).reshape(1, -1, 1)
    return model.predict(last_sequence)[0][0]