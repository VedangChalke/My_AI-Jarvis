import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning")
    elif hour > 12 and hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Myself Jarvis, Sir How May i help you ")


def takeCommand():
    # takes input from user and provide string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING......")
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("RECOGNIZING....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Could Not Detect, Please Try Again")
        return "None"

    return query

 """
 # FUNCION TO SEND EMAIL TO RECEIVER ACCOUNT:-
 # BUT SADLY GOOGLE PLATFORM HAVE CLOSED TO TAKE EMAIL FROM THIRD PARTY PLATFORM AS IS COULDN'T GIVE ACCESS TO LESS SECURED DATA :(

def sendEmail(emailReciever, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vedangchalke2603@gmail.com','XXXXXXX')
    server.sendmail('vedangchalke2603@gmail.com',emailReciever,content)
    server.close()
"""



# Main Function Starts:-

if __name__ == "__main__":
    speak("Jarvis Activated")
    wishMe()
    #while True:
    if 1:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("SEARCHING IN WIKIPEDIA...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query , sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Vedang\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,Current Time is {strTime} ")

        elif 'open code' in query:
            codePath = "C:\\Users\\Vedang\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        """
        elif 'send email' in query:
            try:
                speak("What Message should i Delivery?")
                content = takeCommand()
                emailReciever = "vedangchalke2603@gmail.com"
                sendEmail(emailReciever, content)
                speak("Your Email Has Been Send Sucessfully!!")
            except Exception as e:
                print(e)
                speak("Couldn't send Email, Try Again")
        """


