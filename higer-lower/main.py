from flask import Flask
import random

random_number = random.randint(0,9)
app = Flask(__name__)

#homepage
@app.route('/')
def opening():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<image src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'


# @app.route('/<number>')
# def too_low():
#     return "<h1 style='color:red;'>Too low, try again!</h2>"\
#            '<image src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
#
#
# @app.route(f'/{random_number}')
# def correct():
#     return "<h1 style='color:green;'>You found me!</h2>"\
#            '<image src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'
#
# @app.route(f'/9')
# def too_high():
#     return"<h1 style='color:purple;'>Too high, try again!</h2>"\
#            '<image src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'

# def guessing_number(number):
#     def wrapper_function(*args , **kwargs):
#         if number < random_number:
#             return "<h1 style='color:red;'>Too low, try again!</h2>" \
#                    '<image src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
#         elif number > random_number:
#             return "<h1 style='color:purple;'>Too high, try again!</h2>" \
#                    '<image src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
#         else:
#             "<h1 style='color:green;'>You found me!</h2>" \
#             '<image src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'
#
#     return wrapper_function


@app.route('/<int:number>')
def guessing_number(number):
    if number == random_number:
        return  "<h1 style='color:green;'>You found me!</h2>" \
        '<image src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'
    elif number > random_number:
        return "<h1 style='color:purple;'>Too high, try again!</h2>" \
               '<image src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
    elif number < random_number:
        return "<h1 style='color:red;'>Too low, try again!</h2>" \
               '<image src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'


if __name__ == "__main__":
    app.run(debug=True)
