from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys
import os
import time
import subprocess
from assistant.take_command import speak


process_id = None


def button(request):
    return render(request,'index.html')

def output(request):
    
    global process_id

    if(process_id  == None):
        process = subprocess.Popen(['python', 'D:\\test1\\assistant\\sam.py'])
        process_id = process.pid
        return render(request,'index.html')
    else:
        return render(request,"index.html")
    
    


def kill(request):
    global process_id

    if(process_id != None):
        os.kill(process_id, 9)  # Sending SIGKILL signal
        speak("have a good day")
        return render(request,'index.html')
    else:
        return render(request,'index.html')

# def chatbox():
#     # Read the content of the .txt file
#     with open('D:\\qt\\test1\\static\\output.txt', 'r') as file:
#         file_content = file.read()
    
#     # Pass the content to the template
#     return render(request, 'index.html', {'file_content': file_content})