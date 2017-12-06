#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pygame.locals import *
from Tkinter import *
import time
import subprocess
from threading import Thread
import time
import soundfile as sf
import signal
import subprocess
import signal
import os
import soundfile as sf
from random import randint

soundPLayed = ""

def quit(test) :
    global window
    window.destroy()
    stop(test)


#--------------------------- Threads for the views -------------------------------#
class View1_thread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run (self):
        time.sleep(.1)
        global actual_view
        actual_view = "view1"

class View2_thread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run (self):
        time.sleep(.1)
        global actual_view
        actual_view = "view2"

class View3_thread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run (self):
        time.sleep(.1)
        global actual_view
        actual_view = "view3"

# stop all the speakers
class StopPlay1(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        os.kill(self.pid, signal.SIGINT)
class StopPlay2(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        os.kill(self.pid, signal.SIGINT)
class StopPlay3(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        os.kill(self.pid, signal.SIGINT)
class StopPlay4(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        os.kill(self.pid, signal.SIGINT)

#threads to wait for the end of the song
class waitEnd1(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        global durationSound1
        global stopPressed
        global canPlayMusic1
        broke = 0
        for i in range (int(float(durationSound1))) :
            time.sleep(1)
            if stopPressed == 1 :
                broke = 1
                break

        if broke == 0 :
            time.sleep(1)
            canPlayMusic1 = 1

class waitEnd2(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        global durationSound2
        global stopPressed
        global canPlayMusic2
        broke = 0
        for i in range (int(float(durationSound2))) :
            time.sleep(1)
            if stopPressed == 1 :
                broke = 1
                break
        if broke == 0 :
            time.sleep(1)
            canPlayMusic2 = 1

class waitEnd3(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        global durationSound3
        global stopPressed
        global canPlayMusic3
        broke = 0
        for i in range (int(float(durationSound3))) :
            time.sleep(1)
            if stopPressed == 1 :
                broke = 1
                break
        if broke == 0 :
            time.sleep(.11)
            canPlayMusic3 = 1

class waitEnd4(Thread):
    def __init__(self,pid):
        Thread.__init__(self)
        self.pid=pid;
    def run (self):
        global durationSound4
        global stopPressed
        global canPlayMusic4
        broke = 0
        for i in range (int(float(durationSound4))) :
            time.sleep(1)
            if stopPressed == 1 :
                broke = 1
                break
        if broke == 0 :
            time.sleep(1)
            canPlayMusic4 = 1


isPlaying = 0 # check if a sound is playing
maxTrack=0
# if the music can be played
canPlayMusic1=0
canPlayMusic2=0
canPlayMusic3=0
canPlayMusic4=0
#sound durations
durationSound1=0
durationSound2=0
durationSound3=0
durationSound4=0
indexSoundPlayed=-10


# function to get all sounds durations
def get_duration_1 (path):
    f = sf.SoundFile(path)
    global durationSound1
    durationSound1 = format(len(f) / f.samplerate)
def get_duration_2 (path):
    f = sf.SoundFile(path)
    global durationSound2
    durationSound2 = format(len(f) / f.samplerate)
def get_duration_3 (path):
    f = sf.SoundFile(path)
    global durationSound3
    durationSound3 = format(len(f) / f.samplerate)
def get_duration_4 (path):
    f = sf.SoundFile(path)
    global durationSound4
    durationSound4 = format(len(f) / f.samplerate)



# function to play all the sounds
def playAllSound(test):
    global stopPressed
    stopPressed = 0
    global actual_view
    global track_list1
    global index_soundToPlay
    global isPlaying
    global canPlayMusic1
    if(isPlaying==1 and index_soundToPlay.get() != indexSoundPlayed):
        t=playBackThread(test)
        t.start()
        isPlaying = 0
        stop(test)


    global indexSoundPlayed

    if actual_view == "view3" and index_soundToPlay.get() != indexSoundPlayed:
        if(index_soundToPlay.get()<len(track_list1)):
            indexSoundPlayed = index_soundToPlay.get()
            canPlayMusic1 = 0
            get_duration_1(track_list1[index_soundToPlay.get()].path)
            t1 = playWagon1(track_list1[index_soundToPlay.get()].path)
            t1.start()

        if(index_soundToPlay.get()<len(track_list2)):
            canPlayMusic2 = 0
            t2 = playWagon2(track_list2[index_soundToPlay.get()].path)
            get_duration_2(track_list2[index_soundToPlay.get()].path)
            t2.start()

        if(index_soundToPlay.get()<len(track_list3)):
            t3 = playWagon3(track_list3[index_soundToPlay.get()].path)
            get_duration_3(track_list3[index_soundToPlay.get()].path)
            t3.start()

        global soundPlayed
        test=playLoco.get()
        if(index_soundToPlay<len(track_list_loco)):
            t4 = playLocoSound(track_list_loco[index_soundToPlay.get()].path)
            get_duration_4(track_list_loco[index_soundToPlay.get()].path)
            soundPlayed.set(track_list_loco[index_soundToPlay.get()].name)
            t4.start()
        isPlaying =1

stopPressed = 0

# function to stop all the sounds
def stop(test):
    global stopPressed
    stopPressed = 1 # variable to check when stop pressed en end the wait thread
    global isPlaying
    isPlaying=0
    global pidP1
    global pidP2
    global pidP3
    t1=StopPlay1(pidP1)
    t1.start()
    t2=StopPlay2(pidP2)
    t2.start()
    t3=StopPlay3(pidP3)
    t3.start()
    t4=StopPlay4(pidP4)
    t4.start()


# thread to play again once stop
class playBackThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
    def run (self):
        time.sleep(2)
        global stopPressed
        stopPressed = 0
        global actual_view
        global track_list1
        global index_soundToPlay
        global isPlaying
        global canPlayMusic1
        if(isPlaying==1 and index_soundToPlay.get() != indexSoundPlayed):
            isPlaying = 0
            stop(test)

        global indexSoundPlayed

        if actual_view == "view3" and index_soundToPlay.get() != indexSoundPlayed:
            if(index_soundToPlay.get()<len(track_list1)):
                indexSoundPlayed = index_soundToPlay.get()
                canPlayMusic1 = 0
                get_duration_1(track_list1[index_soundToPlay.get()].path)
                t1 = playWagon1(track_list1[index_soundToPlay.get()].path)
                t1.start()

            if(index_soundToPlay.get()<len(track_list2)):
                canPlayMusic2 = 0
                t2 = playWagon2(track_list2[index_soundToPlay.get()].path)
                get_duration_2(track_list2[index_soundToPlay.get()].path)
                t2.start()

            if(index_soundToPlay.get()<len(track_list3)):
                t3 = playWagon3(track_list3[index_soundToPlay.get()].path)
                get_duration_3(track_list3[index_soundToPlay.get()].path)
                t3.start()

            global soundPlayed
            test=playLoco.get()
            if(index_soundToPlay<len(track_list_loco)):
                t4 = playLocoSound(track_list_loco[index_soundToPlay.get()].path)
                get_duration_4(track_list_loco[index_soundToPlay.get()].path)
                soundPlayed.set(track_list_loco[index_soundToPlay.get()].name)
                t4.start()
            isPlaying =1

pidP1 = 0
p1=subprocess

pidP2 = 0
p2=subprocess

pidP3 = 0
p3=subprocess

pidP4 = 0
p4=subprocess

pidMusic1 = 0
pMusic1=subprocess

# threads to play in each wagon
class playWagon1(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        #os.system("aplay -Dstereo1 " +self.name)
        twait1 = waitEnd1(self.name)
        twait1.start()
        global p1
        p1 = subprocess.Popen(["aplay -Dstereo1 " +self.name], stdout=devnull, shell=True)
        global pidP2
        pidP1 = p1.pid

class playMusic1(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        #os.system("aplay -Dstereo1 " +self.name)
        global p1
        p1 = subprocess.Popen(["aplay -Dstereo1 " +self.name], stdout=devnull, shell=True)
        global pidP2
        pidP1 = p1.pid

class playWagon2(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        twait2 = waitEnd2(self.name)
        twait2.start()
        global p2
        p2 = subprocess.Popen(["aplay -Dstereo2 " +self.name], stdout=devnull, shell=True)
        global pidP2
        pidP2 = p2.pid

class playMusic2(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        #os.system("aplay -Dstereo1 " +self.name)
        global p2
        p2 = subprocess.Popen(["aplay -Dstereo2 " +self.name], stdout=devnull, shell=True)
        global pidP2
        pidP2 = p2.pid


class playWagon3(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        twait3 = waitEnd3(self.name)
        twait3.start()
        global p3
        p3 = subprocess.Popen(["aplay -Dstereo3 " +self.name], stdout=devnull, shell=True)
        global pidP3
        pidP3 = p3.pid

class playMusic3(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        global p3
        p3 = subprocess.Popen(["aplay -Dstereo3 " +self.name], stdout=devnull, shell=True)
        global pidP3
        pidP3 = p3.pid

class playLocoSound(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        twait4 = waitEnd4(self.name)
        twait4.start()
        global p4
        p4 = subprocess.Popen(["aplay -Dstereo4 " +self.name], stdout=devnull, shell=True)
        global pidP4
        pidP4 = p4.pid

class playMusic4(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name;
    def run (self):
        devnull = open('/dev/null', 'w')
        global p4
        p4 = subprocess.Popen(["aplay -Dstereo4 " +self.name], stdout=devnull, shell=True)
        global pidP4
        pidP4 = p4.pid


#----------------------- End Thread ---------------------------------------#
# main window
window = Tk()
window.focus_set()

index_sound1 = 0;

actual_view = "view1"

index_soundToPlay = IntVar()
index_soundToPlay.set("0")

def increaseIndexSoundToPlay(test) :
    global index_soundToPlay
    global actual_view
    global maxTrack
    if(actual_view == "view3"):
        if(index_soundToPlay.get()<maxTrack-1):
            index_soundToPlay.set(index_soundToPlay.get()+1)

def decreaseIndexSoundToPlay(test) :
    global index_soundToPlay
    if(actual_view == "view3"):
        if(index_soundToPlay.get()>0):
            index_soundToPlay.set(index_soundToPlay.get()-1)

#sound class
class son:
    def __init__(self):
        self.name = "ze"
        self.path = "ze"

#parcour list
parcour_list = []

#--------------------- Srcoll with arrow --------------------------#
index_parcour=0
list_button_parcour=[]
nb_parcour=0

nb_langage=0

index_langage1=0
list_button_langage1=[]

index_langage2=0
list_button_langage2=[]

index_langage3=0
list_button_langage3=[]

music_list=[]


def increase1(test):
    global actual_view
    if actual_view == "view2":
        global index_langage1
        if index_langage1<nb_langage-1 :
            index_langage1=index_langage1+1
def decrease1(test):
    global actual_view
    if actual_view == "view2":

        global index_langage1
        if index_langage1>0 :
            index_langage1=index_langage1-1


def increase2(test):
    global actual_view
    if actual_view == "view1":
        global index_parcour
        if index_parcour<nb_parcour-1 :
            index_parcour=index_parcour+1
    if actual_view == "view2":
        global index_langage2
        if index_langage2<nb_langage-1 :
            index_langage2=index_langage2+1
    if actual_view == "view3":
        increaseIndexSoundToPlay(test)

def decrease2(test):
    global actual_view
    if actual_view == "view1":
        global index_parcour
        if index_parcour>0 :
            index_parcour=index_parcour-1
    if actual_view == "view2":
        global index_langage2
        if index_langage2>0 :
            index_langage2=index_langage2-1
    if actual_view == "view3":
        decreaseIndexSoundToPlay(test)


def increase3(test):
    global actual_view
    if actual_view == "view2":
        global index_langage3
        if index_langage3<nb_langage-1 :
            index_langage3=index_langage3+1
def decrease3(test):
    global actual_view
    if actual_view == "view2":
        global index_langage3
        if index_langage3>0 :
            index_langage3=index_langage3-1

#---------------------- End scroll -------------------#

#tack lists
#wagon 1
track_list1 =  []


#wagon 2
track_list2 =  []

#wagon 3
track_list3 =  []

#Locomotive
track_list_loco = []


#path of the app
path = os.path.dirname(os.path.abspath(__file__))

#language list
language_list = []

paused = False

#selected parcour
selected_parcour = StringVar()

#name of the language for wagon 1
wagon1_language = StringVar()

#name of the language for wagon 1
wagon2_language = StringVar()

#name of the language for wagon 1
wagon3_language = StringVar()

soundPlayed = StringVar()

#------------------ FUNCTION ------------------#

#Pause et unpause
def setPlayLoco(test):
    test = playLoco.get()
    if(test== "non"):
        playLoco.set("oui")
    if(test== "oui"):
        playLoco.set("non")



#------------------------- Get parcour function ----------------------------#
# When the user click a parcour it load all  the language
#---------------------------------------------------------------------------#
def get_parcour(parcour_path):
    selected_parcour.set(parcour_path)
    #clear the language_list
    del language_list[:]
    global nb_langage
    nb_langage = 0
    # get the languages of the parcour
    for directory in os.listdir(selected_parcour.get()):
        language_list.append(directory)

    # WAGON 1
    for widget in frame_2.winfo_children():
        if(widget['text'] != "back"):
            widget.destroy()
    Label(frame_2 , text= "WAGON1",width=10,font=(None, 15)).pack()
    for language in language_list :
        bouton=Button(frame_2, text=language, command= lambda j=language: get_language_1(j))
        bouton.pack(padx=10, pady=5)
        list_button_langage1.append(bouton)
        nb_langage = nb_langage+1

    # WAGON 2
    for widget in frame_3.winfo_children():
        if(widget['text'] != "back"):
            widget.destroy()
    Label(frame_3, text= "WAGON2",width=10,font=(None, 15)).pack()
    for language in language_list :
        bouton=Button(frame_3, text=language, command= lambda j=language: get_language_2(j))
        bouton.pack(padx=10, pady=5)
        list_button_langage2.append(bouton)

    # WAGON 3
    for widget in frame_4.winfo_children():
        if(widget['text'] != "back"):
            widget.destroy()
    Label(frame_4 , text= "WAGON3",width=10,font=(None, 15)).pack()
    for language in language_list :
        bouton=Button(frame_4, text=language, command= lambda j=language: get_language_3(j))
        bouton.pack(padx=10, pady=5)
        list_button_langage3.append(bouton)

#--------------------------------------------------------------------------------#
#-------------------------- Get lanugages function ------------------------------#
#When the user click a languge, it load all the sound
#--------------------------------------------------------------------------------#

# Get language for wagon 1
def get_language_1(language_path):
    wagon1_language.set(language_path)
    del track_list1[:]
    for file in os.listdir(path+"/"+selected_parcour.get()+"/"+language_path):
        if file.endswith(".wav"):
            sound1 = son()
            sound1.name = file
            sound1.path = path+"/"+selected_parcour.get()+"/"+language_path+"/"+sound1.name
            track_list1.append(sound1)

# Get language for wagon 2
def get_language_2(language_path):
    wagon2_language.set(language_path)
    del track_list2[:]
    for file in os.listdir(path+"/"+selected_parcour.get()+"/"+language_path):
        if file.endswith(".wav"):
            sound2 = son()
            sound2.name = file
            sound2.path = path+"/"+selected_parcour.get()+"/"+language_path+"/"+sound2.name
            track_list2.append(sound2)
# Get language for wagon 3
def get_language_3(language_path):
    wagon3_language.set(language_path)
    del track_list3[:]
    for file in os.listdir(path+"/"+selected_parcour.get()+"/"+language_path):
        if file.endswith(".wav"):
            sound3 = son()
            sound3.name = file
            sound3.path = path+"/"+selected_parcour.get()+"/"+language_path+"/"+sound3.name
            track_list3.append(sound3)

# Get language for wagon 1
def get_french():
    del track_list_loco[:]
    for file in os.listdir(path+"/"+selected_parcour.get()+"/Francais"):
        if file.endswith(".wav"):
            sound1 = son()
            sound1.name = file
            sound1.path = path+"/"+selected_parcour.get()+"/Francais/"+sound1.name
            track_list_loco.append(sound1)
    global maxTrack
    maxTrack = len(track_list_loco)


#---------------------------------------------------------------------------#
# ----------------------functions to change view----------------------------#
#---------------------------------------------------------------------------#
def go_to_1(test):
    list_button_langage1[:] = []
    list_button_langage2[:] = []
    list_button_langage3[:] = []
    view_1.tkraise()
    wagon1_language.set("")
    wagon2_language.set("")
    wagon3_language.set("")
    global actual_view
    actual_view = "transition"
    thread = View1_thread()
    thread.start()


def go_to_2(test):
    get_parcour(selected_parcour.get())
    view_2.tkraise()
    global actual_view
    actual_view = "transition"
    thread = View2_thread()
    thread.start()

#--------------- Go to the third view ------------------#

w1_final=0
w2_final=0
w3_final=0
loco = 0
playLoco = StringVar()
playLoco.set("non")

def go_to_3(test):
    global w1_final
    w1_final = 0
    global w2_final
    w2_final = 0
    global w3_final
    w3_final = 0
    global loco
    loco = 0
    list_button_langage1[:] = []
    list_button_langage2[:] = []
    list_button_langage3[:] = []

    get_language_1(wagon1_language.get())
    get_language_2(wagon2_language.get())
    get_language_3(wagon3_language.get())

    get_french()


    #-------------- Get French ---------------------------#

    pathW1 = path+"/"+selected_parcour.get()+"/"+wagon1_language.get()

    pathW2 = path+"/"+selected_parcour.get()+"/"+wagon2_language.get()

    pathW3 = path+"/"+selected_parcour.get()+"/"+wagon3_language.get()

    path_loco = path+"/"+selected_parcour.get()+"/Francais"


    view_3.tkraise()
    global actual_view
    actual_view = "transition"
    thread = View3_thread()
    thread.start()

namePist=StringVar()

# get all the parcour
for directory in os.listdir(path):
    if (not directory.endswith(".py") and not directory.endswith(".pyc") and not directory.endswith(".wav") and not directory.endswith(".mp3") and not directory == "Musique"):
        parcour_list.append(directory)


#--------------- First view -----------------#
# view to choose parcour
view_1 = Frame(window, width=800, height=480, borderwidth=2, relief=GROOVE)
view_1.grid(row=0, column=0, sticky='news')
view_1.pack_propagate(False)

frame_1 = Frame(view_1, width=300, height=430, borderwidth=2, relief=GROOVE)
frame_1.grid(row=0, column=0, sticky='news')
frame_1.pack(side=TOP,padx=300)
frame_1.pack_propagate(False)

for parcour in parcour_list :
    bouton=Button(frame_1, text=parcour)
    bouton.pack(padx=10, pady=5)
    list_button_parcour.append(bouton)
    nb_parcour = nb_parcour+1

Label(view_1,  text= "le parcour selectionne : ",width=50).pack()
Label(view_1,  textvariable=selected_parcour,width=50,font=(None, 15)).pack()


#------------------------Second view ------------------------#
# view to choose language
view_2 = Frame(window, width=800, height=480, borderwidth=2)
view_2.grid(row=0, column=0, sticky='news')
view_2.pack_propagate(False)
frame_2 = Frame(view_2, width=200, height=400, borderwidth=2, relief=GROOVE)
frame_2.grid(row=0, column=0, sticky='news')
frame_2.pack(side=LEFT,padx=30)
frame_2.pack_propagate(False)


frame_3 = Frame(view_2, width=200, height=400, borderwidth=2, relief=GROOVE)
frame_3.grid(row=0, column=0, sticky='news')
frame_3.pack(side = LEFT,padx=30)
frame_3.pack_propagate(False)

frame_4 = Frame(view_2, width=200, height=400, borderwidth=2, relief=GROOVE)
frame_4.grid(row=0, column=0, sticky='news')
frame_4.pack(side = LEFT,padx=30)
frame_4.pack_propagate(False)

#------------------------Third view ------------------------#

displaySoundSelected = StringVar()
displaySoundBefore = StringVar()
displaySoundBefore2 = StringVar()
displaySoundAfter = StringVar()
displaySoundAfter2 = StringVar()

# view to play sound
view_3 = Frame(window, width=800, height=480, borderwidth=2)
view_3.grid(row=0, column=0, sticky='news')
view_3.pack_propagate(False)

frame_6 = Frame(view_3, width=200, height=100, borderwidth=2, relief=GROOVE)
Label(frame_6 , text= "Le son joue est:",width=50).pack(side = TOP)
Label(frame_6,  textvariable=soundPlayed,width=50,font=(None, 15)).pack(side = LEFT)
frame_6.grid(row=0, column=0, sticky='news')
frame_6.pack(side=TOP,padx=300)
frame_6.pack_propagate(False)

frame_5 = Frame(view_3, width=200, height=400, borderwidth=2, relief=GROOVE)
frame_5.grid(row=0, column=0, sticky='news')
frame_5.pack(side=BOTTOM,padx=300)
frame_5.pack_propagate(False)



Label(frame_6,  textvariable=soundPlayed,width=50,font=(None, 10)).pack(side = LEFT,padx=300)

Label(frame_5,  textvariable=displaySoundBefore2,width=50,font=(None, 10)).pack()

Label(frame_5,  textvariable=displaySoundBefore,width=50,font=(None, 15)).pack()


Label(frame_5,  textvariable=namePist,width=50,font=(None, 25)).pack()

Label(frame_5,  textvariable=displaySoundAfter,width=50,font=(None, 15)).pack()

Label(frame_5,  textvariable=displaySoundAfter2,width=50,font=(None, 10)).pack()

go_to_1(view_1)

window.bind("q", increase1)
window.bind("a", decrease1)
window.bind("s", increase2)
window.bind("z", decrease2)
window.bind("d", increase3)
window.bind("e", decrease3)
window.bind("p", playAllSound)

window.bind("n", setPlayLoco)

window.bind("m", stop)
window.bind("l", quit)



#get the music list
for file in os.listdir(path+"/Musique"):
    if file.endswith(".wav"):
        sound1 = son()
        sound1.name = file
        sound1.path = path+"/Musique/"+sound1.name
        music_list.append(sound1)

#Main loop
def loop_function():
    global index_soundToPlay
    global isPlaying
    if(actual_view=="view1"):
        window.bind("<Right>", go_to_2)
    if(actual_view=="view2"):
        window.bind("<Right>", go_to_3)
    if(actual_view=="view2"):
        window.bind("<Left>", go_to_1)
    if(actual_view=="view3"):
        window.bind("<Left>", go_to_2)

    time.sleep(0.00000000000000000001)
    window.update_idletasks()
    window.after(1, loop_function)
    #Scroll parcour with arrow
    global namePist
    if(actual_view=="view3"):
        namePist.set(track_list_loco[index_soundToPlay.get()].name)
        displaySoundSelected.set(track_list_loco[index_soundToPlay.get()].name)
        if index_soundToPlay.get() >0:
            displaySoundBefore.set(track_list_loco[index_soundToPlay.get()-1].name)
        else :
            displaySoundBefore.set("")
        if index_soundToPlay.get() > 1 :
            displaySoundBefore2.set(track_list_loco[index_soundToPlay.get()-2].name)
        else :
            displaySoundBefore2.set("")

        if(index_soundToPlay.get() <len(track_list_loco)-1):
            displaySoundAfter.set(track_list_loco[index_soundToPlay.get()+1].name)
        else :
            displaySoundAfter.set("")
        if(index_soundToPlay.get() <len(track_list_loco)-2):
            displaySoundAfter2.set(track_list_loco[index_soundToPlay.get()+2].name)
        else :
            displaySoundAfter2.set("")

    for i in range(len(list_button_parcour)):
        if i == index_parcour:
            list_button_parcour[i].configure(bg = "red")
            selected_parcour.set(list_button_parcour[i]['text'])
        else :
            list_button_parcour[i].configure(bg = "white")

        if(len(list_button_langage1) > 0):
            for i in range(len(list_button_langage1)):
                if i == index_langage1:
                    list_button_langage1[i].configure(bg = "red")
                    wagon1_language.set(list_button_langage1[i]['text'])
                else :
                    list_button_langage1[i].configure(bg = "white")
        if(len(list_button_langage2) > 0):
            for i in range(len(list_button_langage2)):
                if i == index_langage2:
                    list_button_langage2[i].configure(bg = "red")
                    wagon2_language.set(list_button_langage2[i]['text'])
                else :
                    list_button_langage2[i].configure(bg = "white")
        if(len(list_button_langage3) > 0):
            for i in range(len(list_button_langage3)):
                if i == index_langage3:
                        list_button_langage3[i].configure(bg = "red")
                        wagon3_language.set(list_button_langage3[i]['text'])
                else :
                    list_button_langage3[i].configure(bg = "white")

        global canPlayMusic1
        if(canPlayMusic1 == 1) :
            canPlayMusic1 = 0
            t1 = playMusic1(music_list[randint(0,len(music_list)-1)].path)
            t1.start()
        global canPlayMusic2
        if(canPlayMusic2 == 1) :
            canPlayMusic2 = 0
            t2 = playMusic2(music_list[randint(0,len(music_list)-1)].path)
            t2.start()
        global canPlayMusic3
        if(canPlayMusic3 == 1) :
            canPlayMusic3 = 0
            t3 = playMusic3(music_list[randint(0,len(music_list)-1)].path)
            t3.start()
        global canPlayMusic4
        if(canPlayMusic4 == 1) :
            canPlayMusic4 = 0
            t4 = playMusic4(music_list[randint(0,len(music_list)-1)].path)
            t4.start()

















loop_function()
window.mainloop()
