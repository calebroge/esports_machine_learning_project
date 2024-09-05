# Program05.py
# Caleb Roge
# Kody Bond

import joblib
import numpy as np

print("Guess how much a league of legends player earns based on their total career stats")
matches_guess = int(input("Guess how many matches played (any number ranging from 1-100): "))
kills_guess = int(input("Predict how many total kills they've gotten from playing league of legends: "))
deaths_guess = int(input("Guess how many total deaths have resulted from their matches: "))
assists_guess = int(input("Guess their total kill assists from their matches: "))
gold_guess = int(input("Guess how much total gold earned from a match (in tousands/hundreds of thousands): "))

esports_prediction = [matches_guess, kills_guess, deaths_guess, assists_guess, gold_guess]

# Load the model that we trained and saved to a file
model = joblib.load('model.joblib')

# Create an input instance starting from a list of feature values
#input1 = [95, 273, 506, 1300674, 1257615]

# Create a 2D numpy array for the input format to our model
input_new = np.array(esports_prediction).reshape(1, -1)

# Feed the model the instance andm ake a prediction for the target value
predicted_value = model.predict(input_new)

# Display the predicted value
print(f"The predicted value is: ${predicted_value[0]:,.2f}")

