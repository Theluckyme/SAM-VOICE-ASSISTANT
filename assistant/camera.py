from take_command import speak
import subprocess

def open_camera():
    try:
        subprocess.Popen("cmd /c start microsoft.windows.camera:", shell=True)
    except Exception as e:
        print("Error opening camera:", e)
        speak("Error opening camera:",e)
def close_camera():
    try:
        subprocess.Popen("taskkill /f /im WindowsCamera.exe", shell=True)
    except Exception as e:
        print("Error closing camera:", e)
        speak("Error closing camera:", e)