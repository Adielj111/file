from flask import Flask, request
import random
import pandas as pd

app = Flask(__name__)

names = ["Adiel", "Jake", "John", "Derin"]

@app.route('/hm', methods=['GET'])
def pick():
    number = request.args.get('number')
    if number is None:
        return "a"

    random.seed(number)
    win = random.choice(names)
    return f"The winnner is: {win}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
