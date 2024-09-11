# Summary
The esports_machine_learning_project is a culmination of all the programs a classmate and I had to create for this data science project. We used Python which is one of the best programming languages to use to analyze data using machine learning models. 

In program 1, we had to download a data set and organize the data so we are able to use and analyze it for the latter part of the project. The variable we were targeting in this project was total compensation based on performance of an esports player in the game 
of league of legends. 

For program 2, we had to create an esports class object to use for our project in outputting data on a esports league of legends player. 

Sample code from Program 2
```Python
# Create a single instance of the data set
esports = Esports(95, 273, 506, 1300674, 1257615)
```

In programs 3-5, we outputted our data on Python and tested different machine learning models to analyze the data
to see which model was the most accurate in predicting data on an esports player's stats and their compensation.

Line 66 in Program 4
```Python
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=X, y=y, cv=kfold, scoring='r2')
    print(f"{estimator_name:>16}: mean of r2 scores = {abs(scores.mean()):.3f}")
```

Line 29 in Program 5
```Python
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=X, y=y, cv=kfold, scoring='r2')
    print(f"{estimator_name:>16}: mean of r2 scores = {abs(scores.mean()):.3f}")
```
