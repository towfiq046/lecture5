from flask import Flask, render_template, request, jsonify
import os, requests

app = Flask(__name__)
apikey = ("df63a18c1b1fbb8e020b75bb6db79f1a")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    # similar to lecture 4 currency 2.py.

    # qurey for currency exchange rate.
    currency = request.form.get("currency")   # user input currency from html.
    res = requests.get("http://data.fixer.io/api/latest", params={
        "access_key": apikey, "base": "EUR", "symbols": currency})    # parameterizing the url.
    # make sure request succeeded.
    if res.status_code !=200:
        return jsonify({"success": False})  # telling user. lot like api of our own.

    # make sure currency is in response.
    data = res.json()   # convert the json data from the response.
    if data['success'] == False:
        return jsonify({"success": False})

    if currency not in data["rates"]:   # not found in the response list of the rates.
        return jsonify({"success": False})

    # the way we get the api is this. so our code needs to be like this.
    return jsonify({"success":True, "rate": data["rates"] [currency]})  # sending us as a json obj.
