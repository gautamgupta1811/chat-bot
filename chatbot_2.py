from datetime import datetime
import calendar
import webbrowser
import random
import os





print("Welcome".center(20,'*'))

helloIntent=['hi','hello','hey','hello there','hi there',"hola"]
timeIntent=['tell me time','time please','time',"what's the time"]
dateIntent=['tell me date','date please','date',"what's the date","today's date"]
musicIntent=['play song','song','please play songs',"play music","music","please play music"]
songIntent=["show song","song list","list of song","songs","music list"]
videoIntent=['play video','videos','video','play videos','video song']
calendarIntent=['calendar','show calendar','calender please']

chat=True
while chat:
    msg=input("Enter your Message : ")
    if msg.lower() in helloIntent:
        print("hello there")
    elif msg.lower() in dateIntent:
        d= datetime.now().date()
        print(d.strftime("%d/%m/%y,%a"))
    elif msg.lower() in timeIntent:
        t=datetime.now().time()
        print(t.strftime("%H:%M:%S,%p"))
    elif msg.startswith('open'):
        web=msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg in musicIntent:
        path=r"E:\song"
        os.chdir(path)
        songs=os.listdir()
        song=random.choice(songs)
        os.startfile(song)
    elif msg in calendarIntent:
        year=int(input("Enter the Year: "))
        print(calendar.calendar(year))         
    elif msg in songIntent:
        path=r"E:\song"
        os.chdir(path)
        songs=os.listdir()
        print (songs)
        song=input("Enter the name of song: ")
        os.startfile(song+".mp3")
    elif msg.startswith('google'):
        sep=msg.replace('google ','')
        data=sep.split()
        search="+".join(data)
        webbrowser.open("https://www.google.com/search?source=hp&ei=LbwEXf3bLM-w9QO_kISQAQ&q="+search+"&oq="+search+"&gs_l=psy-ab.3..0l10.2157.2861..3080...0.0..0.329.1562.2-1j4......0....1..gws-wiz.....0..35i39j0i131.tqe9b0-p8tw")
    elif msg in videoIntent:
        path=r"E:\video songs"
        os.chdir(path)
        video=os.listdir()
        videos=random.choice(video)
        os.startfile(videos)
    elif msg=="bye":
        print("bye, See you later")
        chat= False
    else:
        print("I don't Understand")
