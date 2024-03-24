import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

df = pd.read_csv("data/train.csv")
df = df.sample(frac=1).reset_index(drop=True)
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

classifier = RandomForestClassifier(bootstrap=True, random_state=42, max_depth=50, max_features=2,
                                    min_samples_leaf=5, min_samples_split=8, n_estimators=200)
model = classifier.fit(X, y)

with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)

