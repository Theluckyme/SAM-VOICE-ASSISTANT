from http import client
from io import text_encoding
import os
import time
import datetime
from certifi import contents
from click import prompt
from pathlib import Path
import pyautogui
import webbrowser
import wikipedia
import pywhatkit
import pyjokes
import requests
import random
import psutil
import sys
import pywikihow
from urllib.request import urlopen
import speedtest

from take_command import get_audio,speak
from calculate import Calculate #walframaalfa integration
from ip import ip_info,city_info#ip,city
from news import get_news
from camera import open_camera,close_camera
from appl import open_application,close_application
from gpt import ai
from howtodo import search_how_to
from weather import get_weather
from timer import timer
from translator import translategl
    




def wishMe():
   hour  = int(datetime.datetime.now().hour)
   tt= time.strftime("%I:%M %p")
   if hour>=0 and hour<=12:
        speak(f"Good Morning, its {tt}")
   elif hour >12 and hour<=18:
        speak(f"Good Afternoon, its {tt}")
   else:
       speak(f"Good Evening, its {tt}")

if __name__ == "__main__":
    wishMe()
    speak("I am SAM, How can I help you ?")


while True:
    text = get_audio().lower()
    

    
    
    if text is None:
        speak("Sorry, I couldn't understand you. Please try again.")
        continue

    if "hello" in text:
        speak("hello sir, How can I help you ?")
        
    if "what can you do for me" in text:
        speak("yes sir, nice question")
        speak("as per my program, I am a voice assistant which can perform tasks through voice commands")
        
    if "thank you" in text or "cool" in text or "awesome" in text or "nice" in text or "thank" in text:
             speak("yes sir, that's my pleasure !")                    
    
    if "great" in text:
        speak("great! so what are we browsing")

    if "i am fine" in text:
            speak("that's great, sir")
    if "how are you" in text:
             speak("Perfect sir, what about you ?")
    if "thank you" in text:
             speak("you are welcome, sir")    
             
    if "what is your name" in text:
            speak("i am SAM,your personal assistant") 
               
    if "minimize" in text:
        speak("minimizing sir")
        pyautogui.hotkey('win','down','down')
        
                 

    if "wikipedia" in text:
        speak('Searching wikipedia....')
        text = text.replace("wikipedia","")
        results = wikipedia.summary(text, sentences=2)
        speak("according to wikipedia")
        speak(results)
        print(results)
  
    if "youtube" in text:
        speak(".Playing on youtube")
        text = text.replace("youtube search","")
        text = text.replace("youtube","")
        web  = "https://www.youtube.com/results?search_query=" + text
        webbrowser.open(web)
        pywhatkit.playonyt(text) #type:ignore
        speak(".Enjoy, Sir")
       
    if "open google" in text:
       speak(" what should I search on google sir") 
       cm = get_audio()
       webbrowser.open(f"{cm}")

    sites = [["facebook","https://www.facebook.com/"], ["chrome","https://www.google.com/"], ["stack overflow","https://www.stackoverflow.com/"]]
    for site in sites:
     if f"open {site[0]}" in text:
       speak(f"Opening {site[0]} sir...")
       webbrowser.open(site[1])  

    if "the time" in text:
        strfTime=datetime.datetime.now().strftime("%H:%m:%S")
        speak(f"Sir the time is {strfTime}")

    if "date" in text:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {date}")


    apps = [["notepad","Notepad"], ["file explorer","explorer"], ["command prompt","cmd"], ["calculator","calc"] , ["control panel","control"] , ["task manager","taskmgr"], ["settings","ms-settings:"] , ["word","winword"] , ["powerpoint","powerpnt"] , ["excel","excel"]]
    for site in apps:
     if f"open {site[0]}" in text:
       speak(f"Opening {site[0]} sir...")
       open_application(site[1])

     if f"close {site[0]}" in text:
       speak(f"Closing {site[0]} sir...")
       close_application(site[1])
       
     if "close google" in text or "close youtube" in text or "close the window" in text or "close the application" in text:
        speak("closing sir")
        pyautogui.hotkey('ctrl','w')

    
    if "tell me a joke" in text:
        joke = pyjokes.get_joke()
        speak(joke)

    if "ai" in text:
        text=text.replace("search","")
        text=text.replace("for","")
        text=text.replace("browse","")
        text=text.replace("using ai","")
        print(text)
        query=text
        ai(query)


    if "open camera" in text:
        open_camera()
    elif "close camera" in text:
        close_camera()

    if "play a music" in text:
        music_dir = r"D:\DJ MIX"  # Use 'r' before the string to indicate a raw string
        songs = os.listdir(music_dir)
        random_song = random.choice(songs)
        for songs in songs:
            if songs.endswith('.mp3'):
                os.startfile(os.path.join(music_dir, random_song))

# ..............system task.................

    if "volume up" in text:
        pyautogui.press("volumeup")

    if "volume down" in text:
        pyautogui.press("volumedown")

    if "mute" in text or "volume mute" in text:
        pyautogui.press("volumemute")

    if "ummute" in text or "volume unmute" in text:
        pyautogui.press("volumemute")

    if "switch the window" in text:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

    if "shutdown the system" in text:
        os.system("shutdown /s /t 5")    

    if "restart the system" in text:
        os.system("shutdown /r /t 5")       

    if "sleep the system" in text:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    if "take screenshot" in text or "take a screenshot" in text:
        speak("sir, please tell me name of this screenshot file")
        name = get_audio()
        speak("please sir hold the screen for few seconds, I'm taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("I'm done sir, now I'm ready for next command")

  
    if "my ip" in text:
        ip_info()
    if "where am i" in text:
        city_info()

    if "how much power left" in text or "how much power we have" in text or "battery" in text:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"sir our system have {percentage} percent battery")
        if percentage>=75:
            speak("we have enough power to continue our work")
        elif percentage>=40 and percentage<=75:
            speak("we should connect our system to charging point to charge our battery")
        elif percentage>=15 and percentage<=30:
            speak("we don't have enough power to work, please connect to the charging")
        elif percentage<=15:
            speak("we have very low power, please connect to the charging the system will shutdown very soon")       



    if "calculate" in text:
        text=text.replace("calculate","")
        query=text
        Calculate(query)

    if "a number" in text:
        ran=random.randint(1,100000000)
        speak(f"here is the number {ran}")

    if "flip a coin" in text:
        num = random.choice(['heads', "tails"])
        speak(num)

    if "roll a dice" in text:
        dice = random.randint(1,6)
        speak(f"you rolled {dice}")

    if "news" in text:
        get_news()

    if "internet speed" in text:
        speak("checking internet speed please wait...")
        check_internet_speed()

    if "remember that" in text:
        text = text.replace("remember","")
        text = text.replace("that","")
        text = text.replace("sam","")
        speak("You told me to remember"+text)
        remember = open("Remember.txt","a")
        remember.write(f"{text}\n")
        remember.close()
        
    if "what did i told" in text:
        remember = open("Remember.txt","r")
        data= "You told me to remember" +  remember.read()
        speak(data)
        remember.close()
        
    if "activate searching mode" in text:
        speak("What would you like to search for?")
        search_query = get_audio()
        if search_query is not None:
            search_query=search_query.replace("search","")
            search_query=search_query.replace("for","")
            search_how_to(search_query)    

    if "weather" in text:
        speak("Sure, please tell me the city name.")
        city = get_audio()
        if city:
            weather_info = get_weather(city)
            speak(weather_info)
        else:
            speak("Sorry, I couldn't understand the city name. Please try again.")
    
    if "type" in text:
        speak("please tell me sir what should you want to type")
        writeInNotepad=get_audio()
        pyautogui.write(writeInNotepad)        
    
    if "start a timer" in text:
        timer()
          
    if "translate" in text:
        text=text.replace("translate","")
        translategl(text)
    
    if "exit" in text:
            speak("Thank You for using me sir, Have a good day.")
            sys.exit()