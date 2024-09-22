from flask import Flask, request, jsonify
import base64
import os
import datetime

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json
    user_id = "john_doe_" + datetime.datetime.now().strftime("%d%m%Y")

    # Parse input data
    numbers = [x for x in data.get('data', []) if x.isdigit()]
    alphabets = [x for x in data.get('data', []) if x.isalpha()]

    # Determine highest lowercase alphabet
    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase = [max(lowercase_alphabets)] if lowercase_alphabets else []

    # File handling
    file_b64 = data.get('file_b64', None)
    file_valid = False
    file_mime_type = None
    file_size_kb = None

    if file_b64:
        try:
            file_data = base64.b64decode(file_b64)
            file_valid = True
            file_size_kb = len(file_data) / 1024
            file_mime_type = "image/png"  # Example; you can implement MIME type detection
        except Exception:
            file_valid = False

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase,
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": str(file_size_kb) if file_size_kb else "0"
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": "GET_SUCCESS"})

# This is the export for Vercel
def handler(request, context):
    return app(request.environ, start_response=context)
