from flask import Flask, render_template

# Create App
app = Flask(__name__)

# Create the route of the home page for the app
@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template('index.html')


# Route for the covid cases by county map
@app.route('/countycases')
def county_cases():
    return render_template('county_covid_cases.html')

# Route for the covid deaths by county map
@app.route('/countydeaths')
def county_deaths():
    return render_template('county_covid_deaths.html')

# Route for the covid cases by state map
@app.route('/statecases')
def state_cases():
    return render_template('state_covid_cases.html')

# Route for the covid deaths by state map
@app.route('/statedeaths')
def state_deaths():
    return render_template('state_covid_deaths.html')

if __name__ == '__main__':
    app.run()