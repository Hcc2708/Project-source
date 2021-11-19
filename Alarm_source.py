from tkinter import *
from tkinter import messagebox
import threading
import time
import datetime as dt
import vlc
import os
from PIL import ImageTk, Image

Alarm_Tool = Tk()
Alarm_Tool.geometry('400x400')
Alarm_Tool.title('Alarm Tool')
Alarm_Tool.iconbitmap('Alarm1.ico')
canv = Canvas(Alarm_Tool, width=400, height=400, bg='blue')
canv.grid(row=0,column=0)


def alarm_time():
    global STOP_ALARM
    STOP_ALARM = False
    global snooz_time
    global st
    global p
    try:
        st=snooz_time.get()
    except TclError:
        st=0
    Alarm_Time = f'{hour.get()}:{min.get()}:{sec.get()}'
    Tone = song.get()
    if os.path.exists(Tone):
        p = vlc.MediaPlayer(r"%s"%Tone)
    else:
        p = vlc.MediaPlayer(r'Awesomemorning Alarm.mp3')
    print(Alarm_Time)  
    while True:
        if Can_alarm:
            break
        current_time=dt.datetime.now()  
        Time=time.strftime("%H:%M:%S")   
        Time1=f'{current_time.hour}:{current_time.minute}:{current_time.second}'  
        if((Time == Alarm_Time) or (Time1 == Alarm_Time)):
            p.play()
            time.sleep(0.1)
            threading.Thread(target=Message).start()
            threading.Thread(target=Snooz).start()
            break
        
Can_alarm = False

def Cancel_alarm():
    global Can_alarm
    Can_alarm = True
    
def Al_Tool():
    global Can_alarm
    threading.Thread(target=alarm_time).start()
    Can_alarm = False
    return

def CURRENT_TIME():
    TIME = time.strftime("%H:%M:%S")
    lbl1.config(text=TIME)
    lbl1.after(1000,CURRENT_TIME)
    
def Message():
    messagebox.showinfo("Dear User!","It's Time to wake up")
    
def Stop_alarm():
    global STOP_ALARM
    STOP_ALARM= True
    p.stop()
    
STOP_ALARM = False

def Snooz():
    global st
    if st!=0:
        if STOP_ALARM:
            return
        time.sleep(15)
        p.stop()
        time.sleep(st)
        if STOP_ALARM:
            return
        p.play()
        Snooz()
    if st==0:
        for i in range(7):
            if STOP_ALARM:
                return
            time.sleep(20)
            p.stop()
            if STOP_ALARM==True or i==5:
                return
            p.play()
        
    
img = ImageTk.PhotoImage(Image.open(r"pngtree-clock-time-timepiece-hour-background-picture-image_724407.jpeg"))
canv.create_image(0, 0, anchor=NW, image=img)

canv.create_text(64,22, text="Set Alarm :", fill ="white" , font=('Arial',16,'bold')) 

canv.create_text(115,50, text="Hour   Min   Sec", fill ="white" , font=('Arial',15,'bold'))
canv.create_text(149,101, text="Recommendation : Enter in 24 hour format", fill ="white" , font=('Arial',10))

hour = StringVar()
min=StringVar()
sec=StringVar()
song=StringVar()
snooz_time = IntVar()

canv.create_text(300,15,text="Current Time",fill ="white",font=('Arial',13,'bold'))
lbl1=Label(Alarm_Tool, fg='red',bg='black',font=10)
canv.create_window(300,45,window=lbl1)
threading.Thread(target=CURRENT_TIME).start()


En1=Entry(Alarm_Tool,textvariable=hour,font=10,width=5)
En1.place(x=27,y=65)

En2=Entry(Alarm_Tool,textvariable=min,font=10,width=5)
En2.place(x=87,y=65)

En3=Entry(Alarm_Tool,textvariable=sec,font=10,width=5)
En3.place(x=147,y=65)

canv.create_text(103,140, text="Enter Alarm Tone :",fill="white",font=('Arial',16,'bold'))
En4=Entry(Alarm_Tool,textvariable=song,font=10)
En4.place(x=27,y=154)
canv.create_text(211,190, text="Recommendation : Enter full path of file without quotation marks", fill = "white",font=('Arial',10))

canv.create_text(105,230, text="Enter Snooz Time :",fill="white",font=('Arial',16,'bold'))
En5=Entry(Alarm_Tool,textvariable=snooz_time,font=10)
En5.place(x=27,y=246)
canv.create_text(131,283, text="Recommendetion : Enter in second ",fill="white",font=('Arial',10))

SetBtn=Button(Alarm_Tool, text='Save',fg='white',bg='red',font=('Arial',15,'bold'),width=5,height=1,command=Al_Tool).place(x=30,y=315)
SetBtn1=Button(Alarm_Tool, text='Stop',fg='white',bg='red',font=('Arial',15,'bold'),width=5,height=1,command=Stop_alarm).place(x=141,y=315)
CnclBtn=Button(Alarm_Tool, text='Cancel Alarm',fg='white',bg='red',font=('Arial',15,'bold'),height=1,command=Cancel_alarm).place(x=250,y=315)
Alarm_Tool.mainloop()

