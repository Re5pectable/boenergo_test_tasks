from flask import Flask, render_template, request, jsonify
import sqlite3
from random import randint

# Моя версия: синих -  62,  зеленых - 20,  красных - 18

app = Flask(__name__)


def db_create():
    with sqlite3.connect("items.db") as c:
        c.cursor().execute(f'DROP TABLE IF EXISTS items;')
        c.cursor().execute(f'CREATE TABLE items (id INTEGER PRIMARY KEY AUTOINCREMENT, color text);')

    def add_to_db(color):
        with sqlite3.connect("items.db") as c:
            c.cursor().execute(f'INSERT INTO items (color) VALUES ("{color}" )')

    items = []
    for i in range(1, 101):
        if i <= 62:
            items.append("Синий")
        elif i <= 82:
            items.append("Зеленый")
        else:
            items.append("Красный")

    for i in range(len(items)):
        r = randint(0, len(items)-1)
        add_to_db(items[r])
        print(items[r], r, len(items))
        items.pop(r)


def find(item_id):
    with sqlite3.connect("items.db") as c:
        return c.cursor().execute(f"select color from items where id = '{item_id}'").fetchone()[0]


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        try:
            item_id = request.form.get("id")
            return jsonify(find(item_id))
        except:
            return jsonify(False)



app.run(host="127.0.0.1")