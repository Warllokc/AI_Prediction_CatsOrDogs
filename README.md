# AIPrediction_CatsOrDogs
## Steps to follow




1. Clone the repo.
   ```
      git clone <repository URL>
   ```

2. Copy the dataset from kaggle into the repo and add them to <training_set> folder.
```

   https://www.kaggle.com/datasets/tongpython/cat-and-dog
```
*-- in <training_set> folder should be 2 folders: cats and dogs*

3. Install all required pyhton packages
   ```
      pip install -r requirements.txt
   ```

4. Run the trining.py script adn wait until the training model is trained and saved/updated to model folder
   ```
      python3 trining.py
   ```

5. Use images from <test_images> folder or add your own images (be sure to update the <prediction.py> file if you use your pictures), please use <png> files
  If use your onw pictures, update this line in the <prediction.py> file:
  ```
         img_path = "path/<your image>.jpg"
  ```

  6. Run the <prediction.py > file
   ```
           python3 prediction.py 
```

7. Should see following result
   ```
1/1 [==============================] - 0s 91ms/step

your image.jpg Image is a dog/cat
   ```
