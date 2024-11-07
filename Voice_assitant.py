import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os
import pyjokes
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
#print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your Assistant Priti Please tell me how may I help you")   


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open leetcode' in query:
            speak("Here you go to leetcode flow.Happy coding")
            webbrowser.open("leetcode.com") 
        elif 'open spotify' in query:
            speak("Here you go to Spotify\n")
            webbrowser.open("spotify.com") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            speak("opening VS Code")
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open PowerPoint' in query or 'ppt' in query:
            speak("opening Power Point presentation")
            Path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(Path) 
        elif 'open word' in query or 'word' in query:
            speak("opening word")
            Path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(Path)       
        # little converstaion 
        elif 'how r u' in query or 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Priti")    
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'joke' in query or 'Tell me a joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="all") 
            print(My_joke) 
            speak(My_joke) 

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query)   

        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')    
        elif 'restart ' in query:
            speak("Hold On a Sec ! Your system is on its way to restart")
            subprocess.call('shutdown / r /t 1')

        







        