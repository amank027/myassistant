import os
import pyttsx3

pyttsx3.speak("Hi there, Welcome to your personal assistant")
print("Note: Type help for all commands.")
while True:
    pyttsx3.speak("What do you want to run")
    print("What do you want to run: ", end = '')
    helps=['Available commands:\n','To run any app you can use start,run,execute,open\n','Then add application name','\nExample: start notepad\n------','To stop one can use(stop,exit,close,end)','Example: stop','----------']
    inp=input()
    app=None
    try:
        r,app = inp.split()
    except:
        r=str(inp)
    start=['run','open','start','execute']
    stop=['stop','end','exit','close']
    apps={'iexplore':['explorer','internet explorer'],'powerpnt':['power point','microsoft power point'],'excel.exe':["excel",'microsoft excel'],'calc':['calculator','calc'],'control panel':['cp','panel','control','control panel'],'chrome':['chrome','browser'],'wmplayer':['media','player','windows media player'],'notepad':['notepad','notebook','text editor'],'mspaint':['paint'],'cmd.exe':['cmd','command prompt','command']}
    if r=='help':
        for i in helps:
            print(i)

    elif (r in stop):
        pyttsx3.speak('Thank you')
        break

    elif app:
        for key,value in apps.items():
            if app in value:
                pyttsx3.speak("opening {} for you".format(key))
                os.system("start "+key)
            else:
                pyttsx3.speak("Don't support, Try again!")
                print("Don't support, Try again!")
                break

    else:
        pyttsx3.speak("Don't support, Try again!")
        print("Don't support, Try again!")
