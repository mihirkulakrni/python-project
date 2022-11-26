import pyttsx3
import datetime


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morinig sir")
    elif hour >12 and >=18:
        speak("Good Afternoon Sir")

    else:
        speak("Good evenging")

    speak("plez tell me,How can i help you?")        
