import pickle
import re
import os
import numpy as np
from vectorizer import vect

clf = pickle.load(open(os.path.join('movieclassifier', 'pkl_objects',
                'classifier.pkl'), 'rb'))

label = {0: 'negative', 1: 'positive'}

example = ['I hate this corny movie!']
X = vect.transform(example)
print('Prediction: %s\nProbability: %.2f%%' % (label[clf.predict(X)[0]],
                np.max(clf.predict_proba(X)) * 100))
