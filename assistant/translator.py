import speech_recognition as sr
import requests
from playsound import playsound
import os
import time
from take_command import get_audio,speak
from gtts import gTTS


def get_language_code(language_name):
    # Language code lookup dictionary
    language_codes = {
        "english": "en",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "korean": "ko",
        "chinese": "zh-CN",
        "japanese": "ja",
        "russian": "ru",
        "hindi": "hi",
        "odia": "or",
        "namibia": "na",
        "arabic": "ar",
        "iranian": "fa",
        # Add more languages as needed
    }
    return language_codes.get(language_name.lower(), None)



def translategl(text):
    

    # Get the target language through speech recognition
    
    print("Speak the language in which you want to translate:")
    speak("Speak the language in which you want to translate:")
    target_language=get_audio()
    
    target_language_code = get_language_code(target_language)
    
    
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": target_language_code,
        "dt": "t",
        "q": text,
    }
    response = requests.get(url, params=params)
    translated_text = response.json()[0][0][0]

    
    try:
        speakgl = gTTS(text=translated_text, lang=target_language_code, slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")
    except Exception as e:
        print("Unable to play translated text:", e)