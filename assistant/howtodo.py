from take_command import speak
import pywikihow


def search_how_to(query):
    try:
        search_result = pywikihow.search_wikihow(query)
        if search_result:
            result_text = f"Here is what I found: {search_result[0].title}\n{search_result[0].summary}"
            speak(result_text)
        else:
            speak("Sorry, I couldn't find any relevant information.")
    except Exception as e:
        speak("Sorry, I encountered an error while searching. Please try again later.")
