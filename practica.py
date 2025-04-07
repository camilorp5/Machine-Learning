from sklearn.linear_model import LogisticRegression

# Create an instance of the class
LR = LogisticRegression(penalty='12', c=10.0)

#Fit the instance on the data and then predict the expected value
LR = LR.fit(X_train, y_train)
y_predict = LR.predict(X_test)

# X_train are the features and y_train the actual result (labels)
# X_train could be the climate, or the free time and y_train if the person attends or not

# Can now view the output fitted coefficients
LR.coef_

# Tune regularization parameters with cross validation
#prueba