from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        i=input()
        if i==stopper:
            mixer.music.stop()
            break
        
def log_now(msg):
    file=open('./mylogs.txt',"a")
    file.write(msg.datetime.now(),"\n")
    file.close()
  
  
if __name__== '_main_':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersees=0
    exsees=4
    eyesees=3
    

    while True:
        if time().init_water>watersees:
            print("WATER DRINKING TIME. Enter 'drank' to stop the alarm")
            musiconloop('https://funringtones.mobi/twilight-sms-ringtone','drank')
            init_water=time()
            log_now('Drank water at')
        if time().init_eyes>eyesees:
            print("EYE EXERCISE TIME. enter 'doneyes'")
            musiconloop('/krishnaflu-pa2luqdy-37180 (1).mp3', 'doneyes')
            init_eyes=time()
            log_now('eyes relaxed at')
            break
        if time().init_exercise>exsees:
            print("ACTIVITY TIME. Enter 'doneact'")
            musiconloop('./krishnaflu-pa2luqdy-37180 (1).mp3','doneact')
            init_exercise=time()
            log_now("physicalactivity done")


            
            
    
    