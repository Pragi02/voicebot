import speech_recognition as sr
import time
import spacy
nlp = spacy.load('en_core_web_lg')
def speech_to_text():
    global text
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=0) as mic:
         print("listening...")
         audio = recognizer.listen(mic)
    try:
         text = recognizer.recognize_google(audio,language="en-US")
         print("me --> ", text)
    except:
         print("me -->  ERROR")

def wake_up( text):
    global res
    name="tulip"
    return True if name  in text.lower() else False
    

from gtts import gTTS
import os
import playsound
def text_to_speech(text):
    global res
    print("AI --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    file="res.mp3"
    speaker.save(file)
    playsound.playsound(file,True)
    #statbuf = os.stat("res.mp3")
    #mbytes = statbuf.st_size / 1024
    #duration = mbytes / 200
    #time.sleep(int(50*duration))
    #os.system("start res.mp3")  #if you have a macbook->afplay or for windows use->start
    os.remove(file)

def action_time():
    import datetime
    return datetime.datetime.now().time().strftime('%H:%M')
p=action_time()
#print(p)

def action_temp(city1):
    global city
    try:
        import requests
        import bs4

        # Taking thecity name as an input from the user
        city = str(city1)

        # Generating the url
        url = "https://google.com/search?q=weather+in+"+city

        # Sending HTTP request
        request_result = requests.get( url )

        # Pulling HTTP data from internet
        soup = bs4.BeautifulSoup( request_result.text
                    , "html.parser" )

        # Finding temperature in Celsius.
        # The temperature is stored inside the class "BNeawe".
        temp = soup.find( "div" , class_='BNeawe' ).text
        print(temp)
        """celsius = (int(temp[:-2]) - 32)  / 1.8
        celsius = str(int(celsius)) + " degree celcius"""
        return temp
    except:
        return 'unable to find'

def action_day():
    from datetime import datetime as date
    m= date.today().strftime("%A")
    return m

def action_date():
    from datetime import date
    today=date.today()
    d2=today.strftime("%B %d , %Y")
    return d2

def action_weather(city1):
    global city
    from bs4 import BeautifulSoup
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


    city = city1+" weather"
    city = city.replace(" ", "+")
    res = requests.get( f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")
    return info

def wikisearch(word):
    import wikipedia
    word1=word
    # finding result for the search
    # sentences = 2 refers to numbers of line
    result = wikipedia.summary(word1, sentences = 2)
    return result
  
    
   

# This code is contributed by adityatri

import numpy as np
def Tulip():
    global text
    global res
    global nlp
    global city 
    #global city
    ex=True
    recognizer = sr.Recognizer()
    while ex==True:
        with sr.Microphone() as mic:
             print("listening...")
             audio = recognizer.listen(mic)
        try:
             text = recognizer.recognize_google(audio,language="en-US")
             print("me --> ", text)
        except:
             text="error"
             res="I am not getting you"
            
    
        print(text)
        if wake_up(text) is True:
            res = "Hello I am Tulip the AI, what can I do for you?"
            
        elif "time" in text:
            res = action_time()

        elif "temperature" in text:
            #global text
            doc=nlp(text)
            try:
                for ent in doc.ents:
                    if ent.label_=="GPE":
                        city=ent.text
            except:
                city="Delhi"
            res=action_temp(city)

        elif "weekday" in text:
            res=action_day()

        elif "date" in text:
            res=action_date()
        
        elif "weather" in text:
            doc=nlp(text)
            try:
                for ent in doc.ents:
                    if ent.label_=="GPE":
                        city=ent.text
            except:
                city = "Delhi"
            res=action_weather(city)


        elif any(i in text for i in ["exit","close"]):
            res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
            ex=False
            
        elif any(i in text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","peace out!"])

        elif "bye" in text:
            res=np.random.choice(["Take Care!","Come Back Soon","Bye nice to talk to you"])

        elif "search" in text:
        
            try:
                words=text.split()
                word=words[-1]
                res=wikisearch(word)
            except:
                res="Am Sorry I Don't Know about this"
        text_to_speech(res)
#
