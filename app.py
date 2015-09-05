from flask import Flask, render_template, request
import random
from colorscheme import ColorScheme

application = Flask(__name__)

phrases = [
    "Hanging around you gives me sunburn.",
    "You could sublimate tungsten at a glance.",
    "I like your face.",
    "I could demonstrate the Leidenfrost Effect on your bare skin.",
    "Damn, you're hot.",
    "If I found out we were related I'd feel really awkward.",
    "You have the highest emissivity of any known object.",
    "If you were my teacher I'd write a song about you.",
    "If I look at you any longer I'm going to need a cold shower.",
    "You don't need makeup to look beautiful.",
    "You're pretty."
    ]

colors = [
    ColorScheme("#f4f4ff", "#c0b8cc"), #b r
    ColorScheme("#f4f4ff", "#b8c0cc"), #b g
    ColorScheme("#fff4f4", "#ccc0b8"), #r g
    ColorScheme("#fff4f4", "#ccb8c0"), #r b
    ColorScheme("#f4fff4", "#c0ccb8"), #g r
    ColorScheme("#f4fff4", "#b8ccc0"), #g b
    ]

@application.route("/")
def main():
    color = random.choice(colors)
    return render_template("main.html", color=color)

@application.route("/phrase")
def phrase():
    return random.choice(phrases)

if __name__ == "__main__":
    application.run("0.0.0.0")
