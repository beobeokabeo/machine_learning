import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, precision_score, recall_score
from time import time

# 03
from sklearn.linear_model import LogisticRegression
# 04
from sklearn.svm import SVC
# 05 
from sklearn.neural_network import MLPClassifier
# 06
from sklearn.ensemble import RandomForestClassifier
# 07
from sklearn.ensemble import GradientBoostingClassifier


import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)


titanic = pd.read_csv('./titanic.csv')
print(titanic.head())


# sum of null examples/features in data frame
print(titanic.isnull().sum());


## ====================================================================== ##
##
##      PREPROCESSING START
##
## ====================================================================== ##


# replace null/NA age with mean distribution
titanic['Age'].fillna(titanic['Age'].mean(), inplace=True)
print(titanic.head(10))


for i, col in enumerate(['SibSp', 'Parch']):
    plt.figure(i)
    sns.catplot(x=col, y='Survived', data=titanic, kind='point', aspect=2, )

# combine siblings & spouses + parents & childen into single family_count param and drop originals it from cleaned data set
titanic['Family_cnt'] = titanic['SibSp'] + titanic['Parch']

titanic.drop(['PassengerId', 'SibSp', 'Parch'], axis=1, inplace=True)
print(titanic.head())

print(titanic.isnull().sum())

# check how many survived in the cabin
print(titanic.groupby(titanic['Cabin'].isnull())['Survived'].mean())

# for the ones where Cabin is null, assign 0; else, assign 1
titanic['Cabin_ind'] = np.where(titanic['Cabin'].isnull(), 0, 1)
print(titanic.head())


# map genders from string representation to 0 and 1 for male/female respectively
gender_num = {'male': 0, 'female': 1}
titanic['Sex'] = titanic['Sex'].map(gender_num)
print(titanic.head())


# drop unneeded features
titanic.drop(['Cabin', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
print(titanic.head())

# save cleaned dataset so we don't have to clean it again
titanic.to_csv('./titanic_cleaned.csv', index=False)

# get y / labels of survived passengers
features = titanic.drop('Survived', axis=1)

# if you want to try with scaling features, uncomment next line
#features = preprocessing.scale(tr_features)
labels = titanic['Survived']


X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.4, random_state=24) # random_state is random initialization seed
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=24)

# save features and labels to persisted storage so we don't need to process them again
X_train.to_csv('./train_features.csv', index=False)
X_val.to_csv('./val_features.csv', index=False)
X_test.to_csv('./test_features.csv', index=False)

y_train.to_csv('./train_labels.csv', index=False)
y_val.to_csv('./val_labels.csv', index=False)
y_test.to_csv('./test_labels.csv', index=False)

warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)


# read training features and labels from storage
tr_features = pd.read_csv('./train_features.csv')
tr_labels = pd.read_csv('./train_labels.csv')

# read test features and labels from storage
te_features = pd.read_csv('./test_features.csv')
te_labels = pd.read_csv('./test_labels.csv')

# read validation features and labels from storage
val_features = pd.read_csv('./val_features.csv')
val_labels = pd.read_csv('./val_labels.csv' )

def print_results(results):
    print('BEST PARAMS: {}\n'.format(results.best_params_))

    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))

lr = LogisticRegression()
parameters = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]
}

cv = GridSearchCV(lr, parameters, cv=5)
cv.fit(tr_features, tr_labels.values.ravel()) # reached max num of iterations w/o scaling features; import preprocessing from sklearn if needed

print_results(cv)

print(cv.best_estimator_);

joblib.dump(cv.best_estimator_, './LR_model.pkl')

svc = SVC()
parameters = {
    'kernel': ['linear', 'rbf'],
    'C': [0.1, 1, 10]
}

cv = GridSearchCV(svc, parameters, cv=5)
cv.fit(tr_features, tr_labels.values.ravel())

print_results(cv)

joblib.dump(cv.best_estimator_, './SVM_model.pkl')

mlp = MLPClassifier()
parameters = {
    'hidden_layer_sizes': [(10,), (50,), (100,)], # writing comma means default to 1 in desired dimension
    'activation': ['relu', 'tanh', 'logistic'],
    'learning_rate': ['constant', 'invscaling', 'adaptive']
}

cv = GridSearchCV(mlp, parameters, cv=5)
cv.fit(tr_features, tr_labels.values.ravel())

print_results(cv)

print(cv.best_estimator_)

joblib.dump(cv.best_estimator_, './MLP_model.pkl')

rf = RandomForestClassifier()
parameters = {
    'n_estimators': [5, 50, 250],
    'max_depth': [2, 4, 8, 16, 32, None]
}

cv = GridSearchCV(rf, parameters, cv=5)
cv.fit(tr_features, tr_labels.values.ravel())

print_results(cv)

joblib.dump(cv.best_estimator_, './RF_model.pkl')

gb = GradientBoostingClassifier()
parameters = {
    'n_estimators': [5, 50, 250, 500],
    'max_depth': [1, 2, 3, 5, 7, 9],
    'learning_rate': [0.01, 0.1, 1, 10, 100]
}

cv = GridSearchCV(gb, parameters, cv=5)
cv.fit(tr_features, tr_labels.values.ravel())

print_results(cv);

joblib.dump(cv.best_estimator_, './GB_model.pkl')


models = {}

for mdl in ['LR', 'SVM', 'MLP', 'RF', 'GB']:
    models[mdl] = joblib.load('./{}_model.pkl'.format(mdl)) # load saved models from storage e.g. './LR_model.pkl'


# prediction evaluation metric btwn accuracy, precision, recall
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

# evaluate performance of all the best models on cross validation set
for name, mdl in models.items():
    evaluate_model(name, mdl, val_features, val_labels)

# evaluate on test features
evaluate_model('Gradient Boost', models['GB'], te_features, te_labels)
evaluate_model('Random Forest', models['RF'], te_features, te_labels)