from unittest import result
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
#import smtplib
#import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("Good aaftoornoon ")
    else:
        speak("good evening")

    speak("i am your private assistant so how can i help you")
def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("listning.......")
        #r.pause_threshold = 1
        audio = r.listen(source)
     try:
        print("recogning....")
        query = r.recognize_google(audio)
        print(f"you said :{query}\n")
       

     except Exception as e:
        #print(e)  # do it
        print("say that again plese...")
        return "None"
     return query


if __name__ == "__main__":
    wishMe()
    while True:
     query =takecommand().lower()
     if 'wikipedia' in query:
         speak('searching wikipedia...')
         query=query.replace("wikipedia","")
         results =wikipedia.summary(query,sentences=2)
         speak("according to wikipedia")
         print(results)
         speak(results)
     elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")
     elif 'open google' in query:
        webbrowser.open("https://www.google.com/")
     elif 'open college' in query:
        webbrowser.open("https://campus.softwarica.edu.np/users/profile")
     elif 'open typing' in query:
        webbrowser.open("https://www.typing.com/student/lessons")
     elif 'play music' in query:
        webbrowser.open("https://www.youtube.com/watch?v=UVvXK1rq3ZU&list=PLUhjDsdXUImHCFw9bD-g5Zs7uL4felGie")

     elif 'thank you baby' in query:
         speak("its my pleasure baby always for you i love you")
     elif 'what is your name' in query:
         speak("i am you lovely assistance you can call me love.")
     elif 'who created you' in query:
         speak("my creater is anish bhattarai who is a larner and is learning python")
     elif 'how old are you' in query:
         speak("i was made today so i am 1 day old")
    
     elif 'how are you' in query:
         speak("i am fine baby thnks for asking sweetheart ")
     elif 'do you love me' in query:
         speak("""you are the only one i dream of with my virtual memory too
              so i love you from the buttom of my heart    """)
    
     elif 'the time' in query:
         strTime=datetime.datetime.now().strftime()
         speak(f"baby the time is {strTime}")
     elif 'open code' in query:
         codePath="C:\\Users\\Thachhaina\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

     elif 'stop' in query:
         break
     
         

    
    

