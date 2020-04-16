import os
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm

BASE_DIR = os.path.join(os.path.dirname( __file__ ), '..')


data_path = BASE_DIR + '\\data\\phase_2\\envelope_25avg.csv'

df = pd.read_csv(data_path, index_col=0)
df = df.sample(frac=1).reset_index(drop=True)

df_dry = df[df['label'] == 'dry']
df_dry = df_dry.iloc[:500, :]
df_wet = df[df['label'] == 'wet']
df_wet = df_wet.iloc[:500, :]

df = pd.concat([df_dry, df_wet])
df = df.sample(frac=1).reset_index(drop=True)
X = df.iloc[:, :-1]
y = df.iloc[:,-1]

x_temp = X.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x_temp)
X = pd.DataFrame(x_scaled)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

clf = svm.SVC()
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))