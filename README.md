#  Performance Predictor

This is a Flask application deployed on Heroku.

##  Getting Started

This section assumes you already have a Heroku account and basic understanding of deploying Flask applications.

**1. Clone the Repository:**
```
git clone https://github.com/kevincarrillo032/performancepredictor.git
```
**2. Install Dependencies:**

Navigate to the project directory and install required dependencies:
```
cd performancepredictor  # Replace with your actual directory name
pip install -r requirements.txt
```
**3. Configure Heroku:**

Create a new Heroku application: https://devcenter.heroku.com/articles/creating-apps
Link your local Git repository to the Heroku app using the Heroku CLI:
```
heroku git:remote -a performancepredictor
```

**4. Deploy to Heroku:** 

Push your code to Heroki:
```
git push heroku master
```
