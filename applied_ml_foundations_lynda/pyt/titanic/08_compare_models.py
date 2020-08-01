import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from time import time

val_features = pd.read_csv('./val_features.csv')
val_labels = pd.read_csv('./val_labels.csv' )

te_features = pd.read_csv('./test_features.csv')
te_labels = pd.read_csv('./test_labels.csv')

models = {}

for mdl in ['LR', 'SVM', 'MLP', 'RF', 'GB']:
    models[mdl] = joblib.load('./{}_model.pkl'.format(mdl))

def evaluate_model(name, model, features, labels):
    start = time()
    
    # predict
    predictions = model.predict(features)
    
    end = time()
    accuracy = round(accuracy_score(labels, predictions), 3)
    precision = round(precision_score(labels, predictions), 3)
    recall = round(recall_score(labels, predictions), 3)
    print('{} -- Accuracy: {} / Precision: {} / Recall: {} / Latency: {}ms'.format(name,
                                                                                   accuracy,
                                                                                   precision,
                                                                                   recall,
                                                                                   round((end - start)*1000, 1)))


for name, mdl in models.items():
    evaluate_model(name, mdl, val_features, val_labels)

evaluate_model('Gradient Boost', models['GB'], te_features, te_labels)
evaluate_model('Random Forest', models['RF'], te_features, te_labels)