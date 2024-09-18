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
to see which model was the most accurate in predicting data on an esports player's stats and their compensation. The major difference between each of the program files is what data models were using and measuring on our datasets. In program 3, we tested linear_regression
elasticnet, lasso, and ridge on our data model. Where in program 4, we tested the svr, kneighborsregressor, and gradientboostingregressor data models

Lines 26-29 in Program 3
```Python
# Choosing the best model
from sklearn.linear_model import ElasticNet, Lasso, Ridge

estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}

for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=X, y=y, cv=kfold, scoring='r2')
    print(f"{estimator_name:>16}: mean of r2 scores = {abs(scores.mean()):.3f}")
```

Lines 26-27 in Program 4

```Python
# Choosing the best model
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor

estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'SVR': SVR(),
    'KNeighborsRegressor': KNeighborsRegressor(),
    'GradientBoostingRegressor': GradientBoostingRegressor()
}
```

Lines 30-31 in Program 5
```Python

# Train the final model on the entire dataset
final_model = GradientBoostingRegressor()
final_model.fit(X=X, y=y)   # X, y make up the entire dataset

# Save the model to a joblib file
import joblib
joblib.dump(final_model, 'model.joblib')
```
