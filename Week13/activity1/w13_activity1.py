import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

def instructor_chatbot():
    """Command-line AI Itinerary Chatbot."""
    print("\nWelcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    
    # Construct prompt
    prompt = f"""
    You are a professional tourist recommender. Provide an itinerary recommendation based on user data.
    
    User Details:
    - days: {days} days
    - destination: {location} city
    - Age: {age} years
    
    Based on your personal information, 
    Then, give a structured itinerary with a name of the place, address and short description for each day separately in order with maximum three activities in a day.
    """
    
    try:
        # Use Gemini 2.0 Flash (free tier)
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        
        # Generate response
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=200,
                temperature=0.7,
            )
        )
        
        print("\n My Name is Hadi as AI Itinerary expert:")
        print(response.text)
        print("\n" + "-"*50 + "\n")
        
    except Exception as e:
        print("Error communicating with Gemini API:", e)

if __name__ == "__main__":
    instructor_chatbot()
