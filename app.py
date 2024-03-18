# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Mock PDF upload handling
    return jsonify({
        "success": True,
        "message": "PDF uploaded successfully.",
        "data": {
            "documentId": "67890",
            "uploadTime": "2024-03-18T12:34:56Z"
        }
    })

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '')
    # Mock response for demonstration purposes
    return jsonify({
        "success": True,
        "question": question,
        "answer": "This is a dummy answer.",
        "confidence": 0.75,
        "source": "Page 5, Paragraph 2"
    })

if __name__ == '__main__':
    app.run(debug=True,port=8700)
