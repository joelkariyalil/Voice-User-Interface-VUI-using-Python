import os
import time
import subprocess
import json
import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio

name=input("Name your Perosonal Assistant: ")
print("LOADING ",name,"!!")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak(f"Hello, good morning {name}")
        print(f'Hello, good morning {name}')
    elif hour>=12 and hour<=16:
         speak(f"Hello, good afternoon {name}")
         print(f'Hello, good afternoon {name}')
    else:
         speak(f"Hello, good evening {name}")
         print(f'Hello, good evening {name}')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('I AM LISTENING')
        audio=r.listen(source)
        
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"User Said: {statement}\n")
        
        except Exception as e:
            speak('Pardon Me, Please repeat that again!')
            return "None"
        return statement

speak(f"Loading your personal AI assistant {name}")
wishMe()

if __name__=='__main__':
    while True:
        speak("How can I help you?")
        statement=takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your Personal AI Assistant is Shutting down zzzzzzzz")
            print("Your Personal AI Assistant is Shutting down zzzzzzzz")
            break
            
        if 'wikipedia' in statement:
            speak("Searching Wikipedia.....")
            statement=statement.replace("wikipedia"," ")
            results=wikipedia.summary(statement,sentences=3)
            speak("According to wikipedia...")
            speak(results)
            print(results)
            
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open for you")
            time.sleep(5)
        
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open for you")
            time.sleep(5)
        
        elif 'open Lenskart' in statement:
            webbrowser.open_new_tab("https://www.lenskart.com")
            speak("Lenskart is open for you")
            time.sleep(5)
            
        elif "weather" in statement:
            api_key='8ef61edcf1c576d65d836254e11ea420'
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("What is the City Name")
            city_name=takeCommand()
            complete_url=base_url+"appid = "+api_key+"&q="+city_name
            response=request.get(complete_url)
            res=response.json()
            if res["cod"]!="404":
                y=res["main"]
                current_temp=y["temp"]
                current_humidity=y["humidity"]
                z=res["weather"]
                weather_description=z[0]["descriptions"]
                speak("the temperature in Kelvin Units is "+str(current_temperature)+"\nhumidity in percentage is "+str(current_humidity))
                speak(weather_description)
                print("the temperature in Kelvin Units is "+str(current_temperature)+"\nhumidity in percentage is "+str(current_humidity))
            
            else:
                print("City not Found")
                speak("City not Found")
                
        elif "time" in statement:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
            
        elif "who are you" in statement or "what can you do" in statement:
            speak(f"I'm {name}, and I'm your personal AI Assistant, and yes ChatGPT is better than me")

        elif "who discovered you" in statement:
            speak("I was designed by Joel Thomas Chacko")
            
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Google is open for you")
            time.sleep(5)
            
        elif "news" in statement:
            news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are your headlines')
            speak(news)
            time.sleep(5)
        
        elif "search" in statement:
            statement=statemen.replace("search"," ")
            webbrowser.open_new_tab("statement")
            time.sleep(5)
            
            
        #Wolframalpha Module    
        elif "ask" in statement:
            speak("I can answer your computational questions too! Try me!")
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client=wolframalpha.Client('R2K75H-7ELALHR35X')
            r=client.query(question)
            answer=next(r.results).text
            speak(answer)
            print(answer)
            
        elif "thank you" in statement:
            break
            
        elif "shut down" in statement:
            speak("Your PC will now Shutdown")
            subprocess.call(['sleep',"/1"])

time.sleep(5)