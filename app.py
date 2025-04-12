from flask import Flask, request, jsonify, send_from_directory
import tensorflow as tf
import numpy as np
from PIL import Image
from flask_cors import CORS



# Load the trained model
model = tf.keras.models.load_model("Waste-Classification-CNN-Model.h5")
print("-----------------------------------------------------")
print(model.input_shape)
print("-----------------------------------------------------")


# Define class labels (modify if needed)
class_labels = ["organic", "recyclable"]

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


def preprocess_image(image):
    image = image.resize((150, 150))  # Resize to match model's expected input
    image = image.convert("RGB")  # Ensure it's RGB (3 channels)
    image = np.array(image) / 255.0  # Normalize pixel values to [0,1]

    image = image.reshape(1, 150, 150, 3)  # Reshape to match (1, 150, 150, 3)

    print(f"Processed Image Shape: {image.shape}")  # Debugging line

    return image



@app.route("/")
def serve_frontend():
    return send_from_directory(".", "frontend.html")  # Serve the HTML file


@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        image = Image.open(file.stream)
        processed_image = preprocess_image(image)

        prediction = model.predict(processed_image)
        predicted_class = "organic" if prediction[0][0] > 0.5 else "recyclable"

        response = {"prediction": predicted_class}
        print(f"Sending Response: {response}")  # Debugging output

        return jsonify(response)

    except Exception as e:
        print(f"Error in classification: {e}")  # Debugging output
        return jsonify({"error": "Error in classification. Check console for details."}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



# for running the file just writer "python app.py"
