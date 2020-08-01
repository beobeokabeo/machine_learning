import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

titanic = pd.read_csv('./titanic.csv')
print(titanic.head())

titanic.isnull().sum()

titanic['Age'].fillna(titanic['Age'].mean(), inplace=True)
print(titanic.head(10))

for i, col in enumerate(['SibSp', 'Parch']):
    plt.figure(i)
    sns.catplot(x=col, y='Survived', data=titanic, kind='point', aspect=2, )

titanic['Family_cnt'] = titanic['SibSp'] + titanic['Parch']

titanic.drop(['PassengerId', 'SibSp', 'Parch'], axis=1, inplace=True)
print(titanic.head())

print(titanic.isnull().sum())
print(titanic.groupby(titanic['Cabin'].isnull())['Survived'].mean())


titanic['Cabin_ind'] = np.where(titanic['Cabin'].isnull(), 0, 1)
print(titanic.head())

gender_num = {'male': 0, 'female': 1}
titanic['Sex'] = titanic['Sex'].map(gender_num)
print(titanic.head())

titanic.drop(['Cabin', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)

titanic.to_csv('./titanic_cleaned.csv', index=False)