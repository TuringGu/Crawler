import tensorflow as tf
import numpy as np
from tensorflow import keras

print(tf.__version__)

# Use array to store data
# y = (2 * x) - 1
xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Build the model
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

# Start training
model.fit(xs, ys, epochs=500)

# Use trained model to predict the result
print(model.predict([10.0]))