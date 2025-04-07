import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import datetime
import os

# Set your OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Error: Could not request results"

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def perform_task(command):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening insta ")
    elif "hi" in command:
        speak("hi kavya ami chastunav")
    elif "open chatgpt" in command:
        webbrowser.open("https://openai.com/")
        speak("Opening chatgpt")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "shutdown" in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")
    elif "hello" in command:
        speak("hello goodmorning")
    else:
        ai_response = chat_with_ai(command)
        speak(ai_response)
def perfome2(command):
   if "open music" in command:
        webbrowser.open("https://www.amazon.com/")
        speak("Opening music")

def main():
    speak("Hello")
    while True:
        command = listen()
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        if command:
            perform_task(command)

if __name__ == "__main__":
    main()
