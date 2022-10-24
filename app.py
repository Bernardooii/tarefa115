from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    nome = "Bernardo"
    idade = "13"

@app.route("/pai")
def father():

    nome = "Leandro"
    idade = "41"

@app.route("/mae")
def mother():

    nome = "Bárbara"
    idade = "36" 

@app.route("/amigo")
def friend():

    nome = "Pedro"
    idade = "13"

app.run(debug=True)