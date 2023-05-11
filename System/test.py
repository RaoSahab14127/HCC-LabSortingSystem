import os
import cv2
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input, Flatten, Dense
from keras.models import Model
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Define path to the directory containing the dataset
data_dir = "./Dtrain"

# Define the list of body parts to classify
body_parts = ["class1", "class2", "class3", "class4", "class5", "class6"]

# Load the dataset
X = []
y = []

for i, body_part in enumerate(body_parts):
    folder_path = os.path.join(data_dir, body_part)
    for img_path in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, img_path))
        img = cv2.resize(img, (224, 224))
        X.append(img)
        y.append(i)

# Convert data to numpy arrays
X = np.array(X)
y = np.array(y)



# Split the data into training, validation, and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC(kernel = 'rbf', C = 10))])
pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
