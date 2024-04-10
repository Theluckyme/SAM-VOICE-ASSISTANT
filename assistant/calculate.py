import wolframalpha
from take_command import get_audio,speak

def Calc(query):
    apikey="WKVT8A-WRJX345W6K"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("Sorry! unable to understand")

def Calculate(query):
    Term  = str(query)
    Term = Term.replace("Sam","")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("multiply","*")
    Term = Term.replace("divide","/")

    final= str(Term)

    
    result = Calc(final)
    speak("it's "+result)