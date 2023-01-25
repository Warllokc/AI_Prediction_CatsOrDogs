import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow import keras
import os

# Load teh model
model = keras.models.load_model('model')

# Save the path and the name of the file
img_path = "test_images/dog4.jpg"
img_name = os.path.basename(img_path)

# Load the image
dog_image1 = load_img(img_path, target_size=(150, 150), grayscale=True)

# Change the image to an array
dog_image_array1 = img_to_array(dog_image1)

# Preproces the image
image_array = [dog_image_array1]

for image in image_array: 
  # Add a dimension to match the input format of the model
  image = image / 255.0
  image = np.expand_dims(image, axis=0)
  
  # Make a prediction
  prediction = model.predict(image)

  # check the prediction
  if prediction > 0.5:
    print(f'{img_name} Image is a dog')
  else:
    print(f'{img_name} Image is a cat')
