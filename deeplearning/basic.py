#deep learning library
#google developed
#it will provide so many model
#image recognition
# Neural Networks 
import tensorflow as tf

from tensorflow import keras

#Sequential - used to create deep learning model input layer 
#create 10 neurons in the layer
# relu - Faster Training , avoid vanishing gradients , deep networks 
# Output layer - 1 return
model = keras.Sequential([
    keras.layers.Dense(10,activation='relu'),
    keras.layers.Dense(1)
])

model.compile(
    optimizer = "adam",
    loss = "mean_squared_error"
)
print ("Deep learning model ready")


