from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/_calculate')
def calculate():
    a = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    b = request.args.get('numbere2', '0')
    m = re.match('-?\d', a)
    n = re.match('-?\d', b)
    result = '잘못된 값'
    if m is None or n is None or operator not in '+-*/':
        return jsonify(result = result)
    else:
        return eval(a + operator + b)
    return jsonify(result = result)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
