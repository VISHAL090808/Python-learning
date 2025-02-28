import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI

recognizer = sr.Recognizer()
engin= pyttsx3.init()

def speak(text):
    engin.say(text)
    engin.runAndWait()
def aiProccess(command):
    client = OpenAI(api_key=("***********************")
)

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
        {
            "role": "user",
            "content": command
        }
    ]
)
    return completion.choices[0].message.content


def processcommand(c):
    if 'open google'in c.lower():
        webbrowser.open('https://google.com')
    elif 'open linkedin'in c.lower():
        webbrowser.open('https://facebook.com')
    elif 'open linkedin'in c.lower():
        webbrowser.open('https://www.linkedin.com/')
    elif 'play ' in c.lower():
        # Extract song name after "play"
        song_name = c.lower().replace("play ", "").strip()
        
        # Handle multi-word song names
        for song in musicLibrary.music.keys():
            if song_name in song.lower():  # Partial match check
                link = musicLibrary.music[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
                return  # Exit function after playing a song
        
        speak("Sorry, I couldn't find that song.")
        print("Song not found.")
    else :
        #let open AI  handle the request
        output =aiProccess(command)
        speak(output)
     



if __name__ == "__main__" :

    speak('Initializing jarvis....')
    #listen for the wake word "jarvis"
    # obtain audio from the microphone

    while True:

        r = sr.Recognizer()
      
        # recognize speech using Sphinx
        print ('recognizing..')
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout= 3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower()== 'jarvis'):
                speak('Ya')
                #Listening for command
                with sr.Microphone() as source:
                    print("jarvis active...!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    # print(command)
                    processcommand(command)
        except Exception as e:
            print("error; {0}".format(e))



