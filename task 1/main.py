from flask import Flask, render_template, request, jsonify
from math import sqrt


app = Flask(__name__)


def calc(a, b, c):
    if (b ** 2) - (4 * a * c) > 0:
        return [((-b) + sqrt(b ** 2 - 4*a*c)) / (2 * a), ((-b) - sqrt(b ** 2 - 4*a*c)) / (2 * a)]
    elif (b ** 2) - (4 * a * c) == 0:
        return [str(-b/(2*a))]
    else:
        return ""


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        f = request.form
        print(f)
        a = f.get("A")
        b = f.get("B")
        c = f.get("C")
        try:
            return jsonify(calc(float(a), float(b), float(c)))
        except:
            return jsonify(False)


app.run(host="127.0.0.1")