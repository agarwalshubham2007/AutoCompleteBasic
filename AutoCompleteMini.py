from flask import Flask
from Model import autoCompleteTrain
from Model import dicRoot
from SearchEngine import searchEngine

app = Flask(__name__)


@app.route('/<inp>')
def main_func(inp):
    return searchEngine(inp)

@app.route('/')
def hello_world():
    autoCompleteTrain()
    return "Welcome to AutoComplete"

if __name__ == '__main__':
    app.run()
