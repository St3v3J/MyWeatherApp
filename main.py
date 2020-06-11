import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    query = "London,UK"
    unit = "metric"  # use "imperial" for Fahrenheit
    api_key = "<your-api-key>"

    url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=25686f97fa831edf0bde2d51916ab4ff"
    data = requests.get(url=url)  # GET request to the OpenWeatherMap API

    return render_template("index.html", data=data.json())


# @app.route("/")
# def index():
#     some_text = "Message from the handler."
#     current_year = datetime.datetime.now().year
#
#     return render_template("index.html", some_text=some_text, current_year=current_year)
#

@app.route("/about-me")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)