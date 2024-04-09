from take_command import speak
import requests
import json

def get_news():
    main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=8c9b0db7434e41519fa592c7c8ba26a4"
    news=requests.get(main_url).json()
    articles=news["articles"]

    for i in range(5):
        try:
            author=articles[i]["author"]
            title=articles[i]["title"]
            speak(f"From {author}")
            speak(f"{title}")
            print("--------------------------------------------")
        except KeyError:
            print("No author or title available for this article")