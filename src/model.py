import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import sklearn.externals
import joblib

def split_data(df):
    X = df.drop("price", axis=1)
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=1)
    return  X_train, X_test, y_train, y_test

def split_data_no_dummy(df):
    X = df["number_bedrooms"]
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=1)
    return  X_train, X_test, y_train, y_test

def lin_model_train(X_train, y_train):
    model = LinearRegression()
    model = model.fit(X_train, y_train)
    return model

def lin_model_predict(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mae, mse, r2
    
def save_model(model):
    joblib.dump(model, 'house_rent_price.sav')