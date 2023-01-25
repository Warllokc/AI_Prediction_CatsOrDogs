import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#set the path to data set
dataset_path = 'training_set'

# Create ImageGenerator object
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

#Load the training and validation data
train_generator = datagen.flow_from_directory(dataset_path, target_size=(150,150), color_mode = 'grayscale', class_mode = 'binary', subset = 'training')
validation_generator = datagen.flow_from_directory(dataset_path, target_size=(150,150), color_mode = 'grayscale', class_mode = 'binary', subset = 'validation')

# Define the CNN architecture
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 1)))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(128, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])

# Train the model
history = model.fit(train_generator, 
                    steps_per_epoch=100, 
                    epochs=10, 
                    validation_data=validation_generator, 
                    validation_steps=50)

# Save the model
model.save('model')
