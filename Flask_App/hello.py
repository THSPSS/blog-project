from flask import Flask
import random


app = Flask(__name__)


#homepage
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is another paragraph</p>' \
           '<image src="https://media.giphy.com/media/GxN4ics7OlvsA/giphy.gif" />'


def make_bold(function):
    def wrapper_function():
        return "<b>"+function()+"<b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        p = function()
        return f"<em>{p}<em>"
    return wrapper_function


@app.route("/bye")
@make_bold
@make_italic
def bye():
    return "Bye!"

@app.route("/username/<name>/1")
def greet(name):
    return f'Hello there {name +"12"}!'


if __name__ == "__main__":
    app.run(debug=True)