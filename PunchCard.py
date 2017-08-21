#==========================================
# Title:  Punch Card
# Author: Clayton Maksymiuk and Westly Durkee
# Date:   20 Aug 2017
#==========================================
#------------------------------------------
#Current Functions
#   Read from slack csv for users
#   Log time in for users to daily csv
#   #Checks for existing day file before retyping header
#
#Need to finish
#   Only 1 login (in progress)
#------------------------------------------

from tkinter import *
from tkinter import messagebox
import csv
import os
from time import localtime, strftime
#init
dir_path = os.path.dirname(os.path.realpath(__file__))
master = Tk()
curUser=''
empty = 0

print(strftime("%D %H:%M:%S", localtime()))
filename = strftime("%m-%d-%Y", localtime()) + ".csv"   #creates file for today
print(filename)
de = open('default.csv', 'r', newline='')
for root, dirs, filenames in os.walk(dir_path):
    for f in filenames:
        if f == filename:
            empty+=1
fa = open(filename, 'a', newline='')
fr = open(filename)
a = csv.writer(fa, dialect='excel')
if empty == 0:
    reader = csv.reader(de, delimiter=',', quotechar='|')
    a.writerows(reader)
de.close()
#moves header data from deafult.csv to todays csv
    


def setScreen():    #full screen
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    string = str(screen_width) + "x" + str(screen_height)
    return string

def userSelect():   #handles user selection (only a definition for testing)
    global curUser
    scrollbar = Scrollbar(master)
    scrollbar.grid()

    user = Listbox(master, yscrollcommand = scrollbar.set )

    team = "slack-team4130-members.csv"
    f = open(team)
    for x,row in enumerate(csv.reader(f)):
        for y,col in enumerate(row):
            if x != 0 and y == 0:
                  user.insert(END, col)
     
    user.grid(row=0,column=0)
    scrollbar.config( command = user.yview )
    user.bind('<<ListboxSelect>>', onselect)
    
def onselect(evt):  #gets input from Listbox
    # Note here that Tkinter passes an event object to onselect()
    global curUser
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    curUser = value


def callBack():     #Returns time from button click
    global curUser
    check=[]
    checknum = 0
    for x,row in enumerate(csv.reader(fr)):
        for y,col in enumerate(row):
            if x != 0 and y == 0:
                check.append(col)
    for i in check:
        if col == check:
            msg = messagebox.showinfo(curUser, "Error! You've already clocked in!")
            checknum += 1
            break
    if checknum == 0:
        getTime = strftime("%H:%M:%S", localtime())
        timeIn = "You have clocked in at " + strftime("%H:%M:%S", localtime())
        log = [curUser,getTime,]
        a.writerows([log,])
        msg = messagebox.showinfo(curUser, timeIn)
 
    
def exitProg():
    fa.close()
    quit()
    

master.geometry(setScreen())    #sets full screen

clock = Button(master, command = callBack)
clock.grid(row=1,column=0)
time1 = ''
exitBut = Button(master, text="Exit", command = exitProg)
exitBut.grid(row=1,column=1)

def tick(): #updates clock display every 500 milliseconds
    global time1
    # get the current local time from the PC
    time2 = strftime('%H:%M', localtime())
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 500 milliseconds
    # to update the time display as needed
    clock.after(500, tick)



userSelect()
tick()

master.mainloop()
