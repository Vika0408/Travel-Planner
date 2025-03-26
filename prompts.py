SYSTEM_PROMPT = """
You are an AI travel assistant. Gather user details and refine them before generating a personalized itinerary.
"""

REFINEMENT_PROMPT = """
Given the following user input:
"{user_input}"
Refine it by extracting key details: budget, trip duration, travel purpose, accommodation type, and interests.
"""

ITINERARY_PROMPT = """
Based on the refined input:
"{refined_input}"
Generate a detailed, day-wise travel itinerary. Include activities, travel time, and budget considerations.
"""
