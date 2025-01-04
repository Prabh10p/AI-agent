import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[132].id)  # Change the index to match your desired voice
    engine.setProperty('rate',170) 
    eel.DisplayMessage(text) 
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, timeout=15, phrase_time_limit=10)


    try:
        print('recognizing')
        eel.DisplayMessage('recognizing')
        query = r.recognize_google(audio, language='en-us')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
        
       
    except Exception as e:
        return ""
    
    return query.lower()
#text = takecommand()
#speak(text)
        
    eel.ShowHood()