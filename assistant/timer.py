import time
from take_command import get_audio,speak

    
    

def timer():
    speak("For how long? Sir")
    times=get_audio()
    number,unit=times.split()
    number=int(number)
    if unit.lower() == "minutes":
        number *= 60
    elif unit.lower() == "seconds":
        pass
    else:
        print("Invalid time unit. Please say the number followed by 'minutes' or 'seconds'.")
        
    
    for x in reversed(range(0, number)):
        print(x)
        time.sleep(1)
    print("time up")
 