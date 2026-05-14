from sklearn.linear_model import LinearRegression
import numpy as np

def predict_demand(df):

    df["t"] = range(1, len(df)+1)

    X = df[["t"]]
    y = df["demand"]

    model = LinearRegression()
    model.fit(X, y)

    next_month = np.array([[len(df)+1]])

    prediction = model.predict(next_month)

    return prediction[0]