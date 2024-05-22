import pandas as pd
from flask import Flask, request, render_template
import pickle

# Load the trained model
model = pickle.load(open("random_forest.pkl", "rb"))

app = Flask(__name__)

# Define features list (assuming it's from logregmodel.py)
features = ["math_score", "reading_score", "writing_score"] 

@app.route("/")
def index():
  """
  Renders the homepage with a form to input student scores.
  """
  return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
  """
  Handles form submission, parses user input, makes a prediction,
  and updates the prediction result in index.html.
  """
  if request.method == "POST":
    try:
      math_score = float(request.form["math_score"])
      reading_score = float(request.form["reading_score"])
      writing_score = float(request.form["writing_score"])
    except KeyError:
      return "Error: Please enter all required scores."

    # Prepare data as a DataFrame for prediction
    data = pd.DataFrame([[math_score, reading_score, writing_score]], columns=features)

    # Make prediction using the loaded model
    prediction = model.predict(data)[0]  # Get the first prediction

    return render_template("index.html", prediction=prediction)  # Update template with prediction

if __name__ == "__main__":
  app.run(debug=True)
