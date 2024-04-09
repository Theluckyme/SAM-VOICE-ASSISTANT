import speech_recognition as sr
import pyttsx3
import os

engine =pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(text):
    with open("D:\\qt\\test1\\static\\output.txt", "a", encoding="utf-8") as file:  # Specify UTF-8 encoding
                file.write(f"SAM said: {text}\n")
    print("User said:"+text)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold= 1
        r.energy_threshold = 300
        audio =r.listen(source)
        
        try:
            print("Recognizing.....")
            said = r.recognize_google(audio) #type:ignore
            print(f"User said: {said}\n")
            with open("D:\\qt\\test1\\static\\output.txt", "a", encoding="utf-8") as file:  # Specify UTF-8 encoding
                file.write(f"User said: {said}\n")
            return said.lower()
        except Exception as e:
            speak("..Please say that again")
            return ""
        
        
def clear_output_file():
    if os.path.exists("D:\\qt\\test1\\static\\output.txt"):
        os.remove("D:\\qt\\test1\\static\\output.txt")
        print("Previous messages cleared from output.txt.")

    