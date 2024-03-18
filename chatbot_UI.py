import streamlit as st
import requests

# Assuming these are the URLs to your Flask app hosted on EC2
UPLOAD_URL = "http://your-ec2-instance-public-dns.amazonaws.com/upload"
ASK_URL = "http://your-ec2-instance-public-dns.amazonaws.com/ask"

st.title('Chatbot Interface')

with st.form("pdf_upload"):
    st.write("Upload PDF")
    uploaded_file = st.file_uploader("Choose a file")
    submit_button = st.form_submit_button("Upload")

    if submit_button and uploaded_file:
        # Here, you'd ideally send the file to your Flask backend
        # For simplicity, we'll just simulate a successful upload response
        response = {"success": True, "message": "File uploaded successfully", "data": {"documentId": "123456"}}
        if response["success"]:
            st.success(response["message"])
            document_id = response["data"]["documentId"]
        else:
            st.error("Failed to upload document.")

with st.form("question_ask"):
    st.write("Ask a Question")
    question = st.text_input("Question")
    ask_button = st.form_submit_button("Ask")

    if ask_button and question:
        # Simulating a request to the backend with the question
        # In a real scenario, you would include the documentId with the request
        # For demonstration, we'll use a fixed response
        mock_response = {
            "success": True,
            "question": question,
            "answer": "This is a dummy answer.",
            "confidence": 0.75,
            "source": "Page 5, Paragraph 2"
        }
        if mock_response["success"]:
            st.write(f"Answer: {mock_response['answer']}")
            st.write(f"Confidence: {mock_response['confidence']}")
            st.write(f"Source: {mock_response['source']}")
        else:
            st.error("Failed to get an answer.")
