from flask import Flask, jsonify
import random

app = Flask(__name__)

app_identifier = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))

@app.route('/fahrenheit_to_celsius/<float:fahrenheit>', methods=['GET'])
def convert_to_celsius(fahrenheit):

  # get Fahrenheit temperature from URL
  fahrenheit = float(fahrenheit)

  fahrenheit_to_celsius = (fahrenheit - 32) / 1.8
  celsius = round(fahrenheit_to_celsius, 2)

  # JSON response
  response = {
    'celsius': celsius,
    'app_identifier': app_identifier
  }

  return jsonify(response)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True)