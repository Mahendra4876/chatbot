import speech_recognition as sr
import webbrowser
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source) 
    audio = recognizer.listen(source) 
    sr.audio()