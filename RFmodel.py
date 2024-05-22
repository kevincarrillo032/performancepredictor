import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import pickle

# Assuming StudentsPerformance.csv is in the same directory
data = pd.read_csv("StudentsPerformance.csv")

def preprocess_column_name(col):
  """
  Replaces spaces with underscores in a column name.
  """
  return col.replace(" ", "_")

data.columns = [preprocess_column_name(col) for col in data.columns]

# Select features (relevant scores)
features = ["math_score", "reading_score", "writing_score"]
target = "race/ethnicity"  # Assuming race/ethnicity is the target variable

# Split data into features (X) and target variable (y)
X = data[features]
y = data[target]

# Split data into training and testing sets (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier model
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)  # Example Random Forest

# Train the model on the training data
random_forest.fit(X_train, y_train)

# Make predictions on the testing set (optional)
# y_pred_forest = random_forest.predict(X_test)

# Evaluate accuracy using accuracy_score (or other metrics)
# accuracy_forest = accuracy_score(y_test, y_pred_forest)

# Save the trained model
with open("random_forest.pkl", "wb") as f:
  pickle.dump(random_forest, f)

print("Model trained and saved successfully!")