import requests
import time
import json
import win32com.client
import platform
def speak(str):
    speak=win32com.client.Dispatch("SAPI.SpVoice")
    speak.Speak(str)
url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=c16ead3fb2b44e20b6522549c6ab2ec4')
try:
    response = requests.get(url)
    a = response.json()
    p = a['articles']
    print(f"Performing Recognitions for Compatibilty...")
    speak(f"Performing Recognitions for Compatibilty...")
    time.sleep(2)
    speak(f"Your Operating System is , {platform.platform()}. And your Hardware is ,{platform.machine()}")
    print(f"Your OS: {platform.platform()} \nHardware:{platform.machine()}")
    time.sleep(2)
    speak("Loading the Virtual News assistant. Please, wait Sir!")
    print("Loading the Virtual News assistant Please wait Sir!")
    time.sleep(2)
    speak("Checking internet connections")
    print("Checking internet connections")
    time.sleep(4)
    speak("Creating secure network")
    print("Creating secure network")
    time.sleep(3)
    speak("Please Press ENTER to start-----")
    inp=input("Please Press ENTER to start-----")
except Exception as e:
    print(f"Performing Recognitions for Compatibilty...")
    time.sleep(2)
    print(f"Your OS: {platform.platform()} \nHardware:{platform.machine()}")
    print("Loading the Virtual News assistant Please wait Sir!")
    time.sleep(2)
    print("Checking internet connections")
    print("Check your Network connection Sir! I think you are having some problem with the internet either too slow or broken network ")
    print("ERROR: 404  NOT FOUND ")
if inp=="" \
        "":
    time.sleep(1)
    for i in range(len(p)):
        print(f"News number {i + 1}")
        speak(f"News number {i + 1} about {p[i]['description']}")
        time.sleep(1)
        speak(p[i]['content'])
        time.sleep(1)
        speak(f"For more information kindly visit {p[i]['url'].split('//')[1][:40]}")
        print(f"For more information kindly visit {p[i]['url'][:40]}")
        print("\n")
        time.sleep(2)


