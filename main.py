import os
import json

from flask import Flask, jsonify, request
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')


with open("users.json") as f:
    users = json.load(f)

@app.route('/process', methods=['POST'])
def process_message():
    auth_username = request.headers.get("Username")
    
    # Authenticate user
    if auth_username not in users:
        return jsonify({"error": "Unauthorized user"}), 403

    
    user_data = users[auth_username]
    phone = user_data["phone"]
    username = user_data["username"]

    # Process message
    message = request.json.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400

    # Example password filtering logic
    passwords = re.findall(r'\b[A-Z0-9]{8}\b', message)
    return jsonify({"passwords": passwords}
