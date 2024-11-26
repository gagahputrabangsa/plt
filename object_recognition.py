from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
# Load a pre-trained text classification pipeline 
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Categories to identify
categories = ["smartphone", "electronics", "gadgets", "home appliances"]
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    # Read the file content
    content = file.read().decode("utf-8")  # Assumes text content for simplicity
