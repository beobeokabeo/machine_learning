import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *

training_data_df = pd.read_csv("sales_data_training_scaled.csv")

X = training_data_df.drop('total_earnings', axis=1).values
Y = training_data_df[['total_earnings']].values

# Define the model
model = Sequential()

model.add(Dense(33, input_dim=9, activation='relu'))
model.add(Dense(66, activation='relu'))
model.add(Dense(33, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')


model.fit(X, Y, epochs=75, shuffle=True, verbose=2)

test_data_df = pd.read_csv('sales_data_training_scaled.csv')

X_test = test_data_df.drop('total_earnings', axis=1).values
y_test = test_data_df['total_earnings'].values

test_error_rate = model.evaluate(X_test, y_test, verbose=0)

print('mean squared error for test data set is {}'.format(test_error_rate))
