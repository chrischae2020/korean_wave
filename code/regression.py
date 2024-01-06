import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('data\kpop.db')

###### Linear regression ######
# Get the data for mv views
data = conn.execute('SELECT views, percent_english FROM mvs WHERE (views IS NOT NULL) AND (percent_english IS NOT NULL)').fetchall()
data = np.array(data)

views = data[:, 0]
percent_english = data[:, 1]

# Train_test_split
X_train, X_test, y_train, y_test = train_test_split(views, percent_english, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

X_train = X_train.reshape((-1, 1))
X_test = X_test.reshape((-1, 1))
print(X_train.shape)

# create and fit model
model = LinearRegression(fit_intercept=True).fit(X_train, y_train)

# Print the Intercept:
print('intercept:', model.intercept_)

# Print the Slope:
print('slope:', model.coef_) 

# Model predictions
y_pred = model.predict(X_test)
r2_test = r2_score(y_test, y_pred)
r2_train = r2_score(y_train, model.predict(X_train))
print(f"R-squared (train): {r2_train}")
print(f"R-squared (test): {r2_test}")

# Plot linear regression line

Xfit = views.reshape((-1, 1))
yfit = percent_english
plt.scatter(Xfit, yfit, color='b')
plt.plot(Xfit, model.predict(Xfit), color='k')
plt.xlabel('Number of Views')
plt.ylabel("Percent English")
plt.title('Percent English Lyrics of K-pop Music Video vs. Number of YouTube Views')
plt.show()
plt.savefig("./analysis_deliverable/visualizations/lr_line.png")
