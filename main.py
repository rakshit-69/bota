import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",150)
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def command():
    content=""
    while content == "":
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("say something")
            audio=r.listen(source)

        try:
            content= r.recognize_google(audio,language="en-in")
            print("Sir you said........." + content)
        except Exception as e:
            print("please try again sir....")

    return content


def main_process():  
    while True:
        request= command().lower()
        if "hello" in request:
            speak("Welcome sir , how can i help you today")
        # elif "play my favourite song" in request:
        #     speak("playing song")
        #     song=random.randint(1,5)
        #     if song == 1:
        #         webbrowser.open("https://www.youtube.com/watch?v=K4DyBUG242c&list=RDQMKECDzA8siXM&start_radio=1")
        #     elif song ==2:
        #         webbrowser.open("https://www.youtube.com/watch?v=AnMhdn0wJ4I&list=RDQMKECDzA8siXM&index=2")
        #     elif song ==3:
        #         webbrowser.open("https://www.youtube.com/watch?v=wJnBTPUQS5A&list=RDQMKECDzA8siXM&index=4")
        #     elif song ==4:
        #         webbrowser.open("https://www.youtube.com/watch?v=cMg8KaMdDYo&list=RDQMKECDzA8siXM&index=8")
        #     else:
        #         webbrowser.open("https://www.youtube.com/watch?v=L-VMCv4Y9l8&list=RDQMKECDzA8siXM&index=15")
        elif "what time is it" in request:
            now_time=datetime.datetime.now().strftime("%H:%M")
            speak("current time is "+ str(now_time))
            print(now_time)
        elif "today's date is" in request:
            now_date=datetime.datetime.now().strftime("%d:%m")
            speak("current date is "+ str(now_date))
            print(now_date)
        elif "new task" in request:
            task=request.replace("new task", "")
            task=task.strip()
            if task != "":
                speak("adding task :" + task)
                with open ("todo.txt","a") as file:
                    file.write(task + "\n")    
        elif "speak task " in request:
            with open ("todo.txt","r") as file:
                speak("work we have to do :" + file.read())

        elif "first year" in request:
            webbrowser.open("https://drive.google.com/drive/folders/1tqagtEu85HNidWVer476nlyxwl2q4t-T") 

        elif "second year" in request:
            webbrowser.open("https://drive.google.com/drive/folders/1mVJAG8nz2QjgoFBzVawf3pwp4zs3OWXI")

        elif "third year" in request:
            webbrowser.open("https://drive.google.com/drive/folders/1xU1yGUvHPjhmBesriBZOxTrbTW4CZA_m") 
        elif "forth year" in request:
            webbrowser.open("https://drive.google.com/drive/folders/1y-CQ88HebrkaULtp-4LQvOAZzE1iDbqw")                  

               
           
main_process()