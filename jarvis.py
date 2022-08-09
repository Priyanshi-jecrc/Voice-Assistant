import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
from datetime import date
import calendar 
from wikipedia.wikipedia import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 or hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I Am Toogle! Please tell me How May I Help You")

def takeCommand():

    # it takes  microphone input from the user  and returns string output   
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recognizing...")    
        query = r.recognize_google(audio, language= 'en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login('priyanshiagrawal.jecrc2@gmail.com', 'Password')
    server.sendmail('agrawal_shubham28@yahoo. com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True :
        query = takeCommand().lower() # logic for execuating task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    
        
        elif 'open amazon' in query:
            webbrowser.open("amazon.in") 
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 
        
        elif 'play music' in query:
            webbrowser.open("ganna.com")

        # elif 'open photos' in query:
        #     photo_dir  = 'C:\\Users\\HP\\OneDrive\\Pictures\\Screenshots'
        #     photo = os.listdir(photo_dir)
        #     print(photo)
            
        # elif 'play music' in query:
        #     # n = random.randint(0,6)
        #     # print(n)
        #     music_dir = 'C:\\Users\\HP\\Downloads\\songs1'
        #     song = os.listdir(music_dir)
        #     print(song)
        #     os.startfile(os.path.join(music_dir, song[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"The current time is {strTime}")

        elif 'date' in query:
            my_date = date.today()
            calendar.day_name[my_date.weekday()] 
            speak(f"The date is {my_date}") 

        elif 'who are you' in query:
            speak("I am Toogle!")    
        
        elif 'quit' in query or 'bye' in query:
            speak("I am Quitting. Thank you for your time")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "agrawal_shubham28@yahoo.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
      