from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import os
from main import run

app = Flask(__name__)

@app.route("/Predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        image = request.files["Image"]
        opened_image = Image.open(io.BytesIO(image.read()))

        folder_path = "meter_new_images"

        if os.listdir(folder_path):
            # remove all files in the folder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)

        save_path = folder_path + '/MeterImage.jpg'
        opened_image.save(save_path)

        digits = run()

        json_obj = {
            "Digits": digits
        }

        return jsonify(json_obj)
    return jsonify("image not found")


if __name__ == "__main__":
    app.run(debug=True)