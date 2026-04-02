from flask import Flask, render_template


app = Flask(__name__)


fruits = [
    {"name": "Olma",   "price": 8000},
    {"name": "Banan",  "price": 12000},
    {"name": "Uzum",   "price": 25000},
    {"name": "Shaftoli","price": 15000},
]


total = sum(fruit for fruit in fruits)
    return render_template("fruits.html", fruits=fruits, total=total)



if __name__ == '__main__':
    app.run(debug=True)
