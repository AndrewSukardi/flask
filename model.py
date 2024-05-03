# Importing required libs
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
import cv2

# Loading model
model = load_model("static/model/model.h5")


# Preparing and pre-processing the image
def preprocess_img(img_data):
    try:    
        # Open image with OpenCV (assuming color format is handled automatically)
        op_img = cv2.imdecode(np.frombuffer(img_data.read(), np.uint8), cv2.IMREAD_COLOR)

        if op_img is None:
            # Handle invalid image format or corruption
            return None

        # Resize the image
        img_resize = cv2.resize(op_img, (64, 64))

        # Convert to NumPy array and normalize (assuming BGR format)
        img2arr = img_resize.astype('float32') / 255.0

        # Check if grayscale (only one channel)
        if len(img2arr.shape) == 2:
            # Expand grayscale to RGB
            img2arr = np.stack((img2arr,) * 3, axis=-1)

        # Reshape to desired format
        img_reshape = img2arr.reshape(1, 64, 64, 3)

        return img_reshape
    
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None


# Predicting function
def predict_result(predict):
    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)

