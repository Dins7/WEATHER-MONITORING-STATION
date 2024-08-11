import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import warnings
import pickle

warnings.filterwarnings("ignore")

file = r'/Users/dinesharavindh/Desktop/Med/seattle-weather.csv'

# Read the data
data = pd.read_csv(file)

# Separate features and target
X = data[['precipitation', 'temp_max', 'temp_min', 'wind']]
y = data['weather']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the model
clf = RandomForestClassifier()

# Train the model
clf.fit(X_train, y_train)

# Make predictions
predictions = clf.predict(X_test)

def compute_int_features(data):
    random_index = np.random.randint(0, len(data))
    sample_data = data.iloc[random_index]
    int_features = sample_data[['precipitation', 'temp_min', 'wind']].values.reshape(1, -1)
    return int_features

# Save the model
pickle.dump(clf, open('model.pkl', 'wb'))
model=pickle.load(open('model.pkl','rb'))