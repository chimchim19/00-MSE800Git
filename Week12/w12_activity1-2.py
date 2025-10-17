""" Week 12 - Activity 1.1: Flask - Variable path """
""" Week 12 - Activity 1.2: Dynamic routing """

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye, Flask!</p>"

@app.route("/username/<name>")
def learn(name):
    return f"{name} is learning Flask!"

""" This accepts a number and displays the value when squared """
@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"


if __name__ == '__main__':
    app.run(debug = True)
