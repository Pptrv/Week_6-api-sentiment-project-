import pandas as pd
import numpy as np
from flask import Flask, request 
from pymongo import MongoClient
import tools.getdata as get
import json
import tools.postdata as post

app = Flask (__name__)



@app.route("/")
def inicial():
    return "Welcome to Star Wars Episode IV Dialogue and Characters"

@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string

@app.route("/dialogue/<character>")
def frase_character(character):
    star_wars = get.dialogue_character(character)
    return json.dumps(star_wars)

@app.route("/line_order/<line>")
def line_order_character(line):
    star_wars = get.order_character_dialogue(line)
    return json.dumps(star_wars)

@app.route("/polarity/")
def polarityCharacters():
    star_wars_pol = get.sentimentAnalysisPolarity(sentence)
    return json.dumps(star_wars_pol)

@app.route("/compound/")
def polarityCharacters():
    star_wars_com = get.sentimentAnalysisCompound(sentence)
    return json.dumps(star_wars_pol)


@app.route("/new_dialogue",methods=["POST"])
def insert_dialogue():
    line_order = request.form.get("Line_order")
    character = request.form.get("Character")
    dialogue = request.form.get("Dialogue")
    post.insert_dialogue(line_order, character, dialogue)
    return "Message inserted succesfully"



app.run(debug=True)
