# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result
import os
from gtts import gTTS
import uuid

# Instantiating flask app
app = Flask(__name__)

# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    
    try:
       if request.method == 'POST':
            folder = f"static/sound"
            for i in os.listdir(folder):
                os.remove(f"{folder}/{i}")

            filename = f"static/sound/{uuid.uuid4()}.mp3"
            
            img_data = request.files['file'].stream
            
            processed_img = preprocess_img(img_data)


            pred = predict_result(processed_img)

            tts = gTTS(str(pred), lang='id')
            tts.save(filename) 
            return render_template("result.html", predictions=str(pred), sound=filename)


    except Exception as e:
        error = str(e)
        if error == '\'NoneType\' object has no attribute \'shape\'':
            return render_template("result.html", err="Couldn't process the image, please try again")
        return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000)
