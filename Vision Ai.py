import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say("text")
    engine.runAndWait()

engine.say('Hello Iam Vision')
engine.say('What i can do for you ?')
engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as sourse:
            print("listening...")
            voice = listener.listen(sourse)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'vision' in command:
                command = command.replace('vision','')
                print(command)
    except:
        pass
    return take_command


def run_vision():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H: %M')
        talk('Current time is' + time)
    elif information in command:
        person = command.replace('information about','')
        info = wikipedia.summary(person,24)
        print(info)
        talk(info)
    elif 'date' in command:
        talk(" Sorry didnt get that")   
    elif 'i love you vision' in command:
        talk("Sorry Iam the assitance you cant love me") 
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Sorry about that did not get anything please speak agian")
while  True:
    run_vision()
  
        