import datetime
import requests
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    query = "London,UK"
    unit = "metric"  # use "imperial" for Fahrenheit
    api_key = "<your-api-key>"

    url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=25686f97fa831edf0bde2d51916ab4ff"
    data = requests.get(url=url)  # GET request to the OpenWeatherMap API

    return render_template("index.html", data=data.json())


@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return render_template("success.html")


# @app.route("/contact", methods=["POST"])
# def contact():
#     contact_name = request.form.get("contact-name")
#     contact_email = request.form.get("contact-email")
#     contact_message = request.form.get("contact-message")
#
#     print(contact_name)
#     print(contact_email)
#     print(contact_message)
#
#     response = make_response(render_template("success.html"))
#     response.set_cookie("user_name", contact_name)
#
#     return response


if __name__ == '__main__':
    app.run(debug=True)