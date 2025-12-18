# Simple Machine Learning Algorithm example

from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create & train model
model = LinearRegression()
model.fit(X, y)

# Take input from user
value = int(input("Number enter kara: "))

# Prediction
prediction = model.predict([[value]])

print("Prediction:", prediction[0])

