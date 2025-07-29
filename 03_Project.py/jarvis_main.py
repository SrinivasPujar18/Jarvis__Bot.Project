#jarvis virtual assitant (mega project)

#first install "pip install speechrecognition pyaudio" and "pip install setuptools", after...
 
import speech_recognition as sr       #Helps to -> "recognize the user vioce"
import webbrowser                     #Helps to -> "website"
import pyttsx3  
import musicLibrary                    #Helps to -> "Text to speech"

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Song not found in your music library.")
    

if __name__ == "__main__":
    speak("Initializing jarvis.....")
    r = sr.Recognizer()
    #Listen for wake up "jarvis" 
    #Obtain audio from the microphone
    
    print("Recognizing...")  
    #recognize speech using Google
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)  #timeout and pharse_time_limit helps to listen fast
                r.adjust_for_ambient_noise(source)
                word = r.recognize_google(audio).lower()

            if(word.lower() == "jarvis"):
                speak("ya")
 
                #Listen for command
                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=2)
                    r.adjust_for_ambient_noise(source)
                    command = r.recognize_google(audio)
                    print("You said: ", command)
                    processCommand(command)         #from func 'processCommand()'
                    
                
        except Exception as e:
            print("Voice Error: ", e)
    



