
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


recognizer = sr.Recognizer()
engine= pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")

          
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")    
          
     elif "open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")    
          
     elif "open chatgpt" in c.lower():
          webbrowser.open("https://chatgpt.com")    
          
    
     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]  # convet this into list like play  khatola and for 1th index khatola starts to play
          link = musiclibrary.music[song]        
          webbrowser.open(link)

                    

if __name__=="__main__":
    speak("initializing jarvis..")
    
while True:


    #listen for wake  jarvis
    r = sr.Recognizer()
   
    print("recognizing...")    

            # recognize speech using Sphinx
    try:
         with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=5)

                word= r.recognize_google(audio)
                

         if (word.lower() == "jarvis"):
              speak("ya")
              with sr.Microphone() as source:
                print("jarvis active")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command) 
                
   
    except Exception  as e:
            print(" Error; {0}".format(e))

