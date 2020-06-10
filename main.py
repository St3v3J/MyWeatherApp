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


if __name__ == '__main__':
    app.run(debug=True)