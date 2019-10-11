# Import packages
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# Setting up training data
celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

# Creating model

# Build  a layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])

# Assemble layers into the model
model = tf.keras.Sequential([layer0])

# Compile the model, with loss and optimizer functions
# loss function = mean squared error
# optimizer function = Adam optimizer
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

# Training the model
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")

# Display training stats
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])
plt.show()

# save the model
model.save('model.h5')

# Load the model
loadedModel = tf.keras.models.load_model('model.h5')

# Use the loaded model to predict fahrenheit for celsius: 105
print(loadedModel.predict([105.0]))