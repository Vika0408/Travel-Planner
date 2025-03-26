import streamlit as st
import requests
import json  # ✅ Import json to handle JSON encoding

st.title("AI Travel Planner")

user_input = st.text_area("Enter your travel preferences:")

if st.button("Generate Itinerary"):
    try:
        headers = {"Content-Type": "application/json"}  # ✅ Ensure correct Content-Type
        payload = json.dumps({"user_input": user_input})  # ✅ Explicitly convert to JSON

        response = requests.post(
            "http://127.0.0.1:5000/generate",
            data=payload,  # ✅ Use 'data' instead of 'json'
            headers=headers  # ✅ Include headers
        )

        # Handle response
        if response.status_code == 200:
            data = response.json()
            itinerary = data.get("itinerary", "No itinerary generated.")
        else:
            itinerary = f"Error: {response.status_code}, {response.text}"

    except requests.exceptions.RequestException as e:
        itinerary = f"Request Error: {str(e)}"

    st.write(itinerary)
