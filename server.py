from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Define routes
@app.route('/predict', methods=['POST'])
def predict():

  # get celsius value from request body
  celsius = request.json['celsius']

  # Load the model
  model = tf.keras.models.load_model('model.h5')

  # Make prediction
  prediction = model.predict([celsius])

  # Take the first value of prediction
  fahrenheit = str(prediction[0][0])

  # Return the output in JSON format
  return jsonify({ 'fahrenheit': fahrenheit })

if __name__ == '__main__':
    app.run(port=5000, debug=True)