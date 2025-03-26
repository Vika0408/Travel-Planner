from flask import Flask, request, jsonify
import google.generativeai as genai
import os


import streamlit as st
import google.generativeai as genai

# Retrieve API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

if not GOOGLE_API_KEY:
    st.error("Google API key is missing. Please set it in Streamlit secrets.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Flask app
app = Flask(__name__)

# Get Google API Key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing Google API Key. Set it as an environment variable.")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Function to call Google Gemini AI
def call_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # ✅ Correct Model Name
        response = model.generate_content(prompt)  # ✅ Correct API Method
        return response.text  # ✅ Extract Response
    except Exception as e:
        return str(e)  # ✅ Handle Errors

# API Route to generate an itinerary
@app.route("/generate", methods=["POST"])
def generate():
    try:
        # Ensure correct Content-Type
        if request.content_type != "application/json":
            return jsonify({"error": "Invalid Content-Type. Use 'application/json'."}), 415

        # Get JSON input
        data = request.get_json()
        if not data or "user_input" not in data:
            return jsonify({"error": "Missing 'user_input' in request."}), 400

        user_input = data["user_input"]

        # Refinement Phase
        refined_input = call_gemini(f"Refine user travel input: {user_input}")

        # Itinerary Generation
        itinerary = call_gemini(f"Generate an itinerary based on: {refined_input}")

        return jsonify({"itinerary": itinerary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
