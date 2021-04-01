# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a + b
    return str(result)
@app.route('/sub')
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a - b
    return str(result)
@app.route('/div')
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a / b
    return str(result)
@app.route('/mult')
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a * b
    return str(result)
    
