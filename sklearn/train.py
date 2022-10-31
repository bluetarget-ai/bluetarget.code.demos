from sklearn import svm
from sklearn import datasets

import pickle

# Load training data set
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train the model
clf = svm.SVC(gamma='scale')
clf.fit(X, y)

saved_model = './model.pkl'

pickle.dump(clf, open(saved_model, 'wb'))

print(f"Model saved: {saved_model}")
