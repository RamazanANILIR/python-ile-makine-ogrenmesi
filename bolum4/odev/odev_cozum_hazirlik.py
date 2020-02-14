import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression

veriler = pd.read_csv("odev_tenis.csv")

le = LabelEncoder()

play = veriler.iloc[:, 4:].values

play[:, 0] = le.fit_transform(play[:, 0])

print(play)

play_status_df = pd.DataFrame(data=play, index=range(14), columns=['play'])

le = LabelEncoder()

outlook = veriler.iloc[:, 0:1].values

outlook[:, 0] = le.fit_transform(outlook[:, 0])

ohe = OneHotEncoder(categories='auto')
outlook_status = ohe.fit_transform(outlook).toarray()

print(outlook_status)

outlook_status_df = pd.DataFrame(data=outlook_status, index=range(14), columns=['overcast', 'rainy', 'sunny'])

raw = veriler.iloc[:, 1:4]

raw_df = pd.DataFrame(data=raw, index=range(14), columns=["temperature", "humidity", "windy"])

print(raw_df)

veriler = pd.concat([raw_df, outlook_status_df], axis=1)

print(veriler)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(veriler, play_status_df, test_size=0.33, random_state=0)

r2 = LinearRegression()
r2.fit(x_train, y_train)

predict_play_status_from_others = r2.predict(x_test)

import statsmodels.api as sm

X = np.append(arr=np.ones((14, 1)).astype(int), values=veriler, axis=1)
X_l = veriler.iloc[:, [0, 1, 2, 3, 4]].values

model = sm.OLS(play, X_l).fit()

print(model.summary())