import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from google import generativeai as genai
import os
import dotenv

def get_ai_response(text):

    api_key: str = os.getenv("API_KEY")
    genai.configure(api_key=api_key)

    client = genai.GenerativeModel('gemini-2.0-flash')

    response = client.generate_content(text)
    return response.text

load_dotenv()

print("hello")

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    text = r.recognize_google(audio)

    engine.say(get_ai_response(text))

    engine.runAndWait()
