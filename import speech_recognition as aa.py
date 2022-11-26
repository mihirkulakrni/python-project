import speech_recognition as aa 
import pyttsx3


machine = pyttsx3.init()

def talk(text):
    machine.say(text)

    machine.runAndWait()
listener = aa.Recognizer()

def input_instruction():
    try:
        with aa.Microphone() as origin:
            print("Listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "Friday" in instruction:
                print(instruction)
            print(instruction)
    except:
        pass    
    
