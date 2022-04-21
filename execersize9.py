# Akbar padhke sunao
import requests

    
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice") 
    speak.Speak(str)


if __name__ == '__main__':
    
    API_KEY = "fdd67567225c4460b9f087961f86d2dd"
    r = requests.get("https://newsapi.org/v2/top-headlines/sources?apiKey="+API_KEY)
    data = r.json()
    if data['status'] == "ok":
        for i, news in enumerate(data['sources']):
            speak("title number " + str(i) +": the headline is "+ news['description'])  
