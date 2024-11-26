from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
# Load a pre-trained text classification pipeline 
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Categories to identify
categories = ["smartphone", "electronics", "gadgets", "home appliances"]
