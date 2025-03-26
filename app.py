import streamlit as st
import google.generativeai as genai
import os
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Retrieve API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")  # ✅ Safely get secret key

if not GOOGLE_API_KEY:
    st.error("Google API key is missing. Please set it in Streamlit secrets.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Function to call Google Gemini AI
def call_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # ✅ Ensure model is correct
        response = model.generate_content(prompt)  # ✅ Correct API call
        return response.text  # ✅ Extract response text
    except Exception as e:
        return str(e)  # ✅ Handle API errors

# API Route to generate an itinerary
@app.route("/generate", methods=["POST"])
def generate():
    try:
        if request.content_type != "application/json":
            return jsonify({"error": "Invalid Content-Type. Use 'application/json'."}), 415

        data = request.get_json()
        if not data or "user_input" not in data:
            return jsonify({"error": "Missing 'user_input' in request."}), 400

        user_input = data["user_input"]

        # Generate response using Gemini API
        itinerary = call_gemini(f"Generate an itinerary based on: {user_input}")

        return jsonify({"itinerary": itinerary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Streamlit UI
def main():
    st.title("AI Travel Planner ✈️")
    user_input = st.text_area("Enter your travel preferences:")

    if st.button("Generate Itinerary"):
        if not GOOGLE_API_KEY:
            st.error("Google API key is missing. Please set it in Streamlit secrets.")
        else:
            itinerary = call_gemini(f"Generate an itinerary based on: {user_input}")
            st.write(itinerary)

if __name__ == "__main__":
    main()  # ✅ Run Streamlit instead of Flask's debug mode
