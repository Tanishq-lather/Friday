import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') #sapi5 ek engine hai jo bole ga pythsx3 module ki help se text to voice converter
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id) # 1 for girl voice 
engine.setProperty('pitch',0.9)
def speak(audio):   #function
    engine.say(audio)
    engine.runAndWait()

def wishme():    #function which wish me everytime i started
    hour = int(datetime.datetime.now().hour)    
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >=12 and hour <17:
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")    
    speak("I am Friday .5")  

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: # speech save in audio file
        print("Listening.....")
        r.pause_threshold = 1    # 1 sec tak sunage if no one speaks
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)   # audio file listen karega
    try:
       print("Recognizing.....")
       query = r.recognize_google(audio,language='en-in')
       print(f"user said: {query}")
    except Exception as e:
        print(e)  
        speak("Boss Can you repeat ")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        # for person
        if 'who ' in query:
            query = query.replace('who is',"")
            results = wikipedia.summary(query,sentences=4)
            speak(results)
        # for thing
        elif 'what ' in query:
            query = query.replace('what is',"")
            results = wikipedia.summary(query,sentences=4)
            speak(results)
        # for other
        elif 'wikipedia' in query:
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,senteces=4)
            speak(results)
        # for open yt
        elif 'youtube open' in query:
            speak("Ok Boss   Youtube is opening")
            webbrowser.open("https://www.youtube.com/")    
        # for open yt
        elif 'open the youtube' in query:
            speak("Ok Boss   Youtube is opening")
            webbrowser.open('https://www.youtube.com/')
        # for open Google
        elif 'google open' in query:
            speak("Ok Boss   Google is opening")
            webbrowser.open('https://www.google.com/')
        # for open Google
        elif 'open the google' in query:
            speak("Ok Boss    Google is opening")
            webbrowser.open('https://www.google.com/')   
        # for open map
        elif 'map open' in query:
            speak("Ok Boss   Map is opening")                  
            webbrowser.open('https://earth.google.com/web/')
        # for open map
        elif 'open the map' in query:
            speak("Ok Boss   Map is opening")
            webbrowser.open('https://earth.google.com/web/')   
        # for current time
        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("it's")
            speak(strtime)
            speak("Boss")
        # for open code
        elif "open code" in query:
            codepath = "c:/Users/lenova/Downloads/VSCodeUserSetup-x64-1.78.2.exe"
            os.startfile(codepath)  
        # for play song
        elif "mood" in query:
            webbrowser.open('https://music.youtube.com/watch?v=CJe2qhAJjWM')
        # for top headlines
        elif "headlines" in query:
            path = "News.py"
            os.startfile(path)
        # for stop
        elif "stop listening" in query:
            break
        # for stopss
        elif "wait" in query:
            speak('ok boss')
            break
        else:
            speak("Sorry,I am still in Improving state")  

        