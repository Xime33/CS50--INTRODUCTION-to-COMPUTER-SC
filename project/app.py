from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# List of characters with their image URLs
characters = [
    {"name": "Minerva McGonagall", "image": "/static/MIN.webp"},
    {"name": "Narcissa Malfoy", "image": "/static/a3.webp"},
    {"name": "Harry Potter", "image": "/static/Harrypotter.webp"},
    {"name": "Hermione Granger", "image": "/static/hermion.webp"},
    {"name": "Ron Weasley", "image": "/static/ron.jpg"},
    {"name": "Draco Malfoy", "image": "/static/draco.jpg"},
    {"name": "Rubeus Hagrid", "image": "/static/rub.webp"},
    {"name": "Cedric Diggory", "image": "/static/ced.webp"},
    {"name": "Fleur Delacour", "image": "/static/fleur.jpg"},
    {"name": "Newt Scamander", "image": "/static/newt.png"},
    {"name": "Myrtle la llorona", "image": "/static/a1.jpg"},
    {"name": "Argus Filch", "image": "/static/a2.png"},
    {"name": "Hedwig", "image": "/static/a4.webp"},
]

# Home route - renders the index.html page


@app.route('/')
def home():
    return render_template('index.html')  # Render the home page template

# Quiz route


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# Random character route


@app.route('/random-character', methods=['GET'])
def random_character():
    character = random.choice(characters)
    return jsonify({"character": character["name"], "image": character["image"]})


if __name__ == "__main__":
    app.run(debug=True)
