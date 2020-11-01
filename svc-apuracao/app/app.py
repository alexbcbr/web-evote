from flask import Flask

app = Flask(__name__)

@app.route('/')
def apuracao():
    return '{"Candidate A": 1003, "Candidate B": 3040}'