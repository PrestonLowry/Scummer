import random
import math 
import tkinter as tk
import os
import imageio
import pyglet
import winsound
import time

window = tk.Tk()
icon = tk.PhotoImage(file='img/scum.png')
window.tk.call('wm', 'iconphoto', window._w, icon)
p = random.randint(1,10)
if(p < 5):
    currentTitle="Welcome to the SCUM ZONE"
else:
    currentTitle="Scummer Roll Calculator"    
window.title(currentTitle)
window.resizable(False, False)
window.configure(bg = "grey69")
rollFrame = tk.Frame(window, width = 320, bg = "grey69")
rolls = tk.Frame(window, width = 320, bg = "grey69")
enterFrame = tk.Frame(bg = "grey69")
finalFrame = tk.Frame(bg = "gray69", height = 200, width  =360)
stopgif = False

def roll_x(scumsum, threshold):
    stopgif = True
    rightFuckupSkull.pack_forget()
    leftFuckupSkull.pack_forget()
    leftFuckupCoffin.pack_forget()
    rightFuckupCoffin.pack_forget()
    rollFrame.update()
    halfsum = math.ceil(scumsum/2)
    success=0
    glitch = 0
    succeeded = False
    isGlitch = False
    isCritGlitch = False
    didYouGlitch = "No!"
    didYouCritGlitch = "No!"
    didYouSucceed = "No!"
    currRoll = 0
    rollsList = ""
    byHowMuch = ""
    for roll in range(scumsum):
        currRoll += 1
        p = random.randint(1,6)
        rollsList += (str(p)+", ")
        if(p>4):
            success += 1
        if (p == 1):
            glitch += 1
    if(success>=threshold):
        succeeded = True
        didYouSucceed = "YES!"  
        howGood = success - threshold
        if(howGood > 0):
            winsound.PlaySound('snd/bigsucc.wav',winsound.SND_ASYNC)
            byHowMuch = "\nBy How Much?: "+str(howGood)      
        else:
            winsound.PlaySound('snd/squeakby.wav',winsound.SND_ASYNC)
            byHowMuch = "\nYou barely succeeded!"
    elif(success<threshold):
        winsound.PlaySound('snd/fail.wav',winsound.SND_ASYNC)            
    if((glitch>halfsum) or threshold == 420):  
        isGlitch = True
        stopgif = False
        didYouGlitch = "GLIIIITCH!"
        winsound.PlaySound('snd/glitch.wav',winsound.SND_ASYNC)  
    if((isGlitch == True and success < threshold) and threshold != 420):
        isCritGlitch = True
        stopgif = False
        didYouCritGlitch = "CRITICAL GLIIIIITCH!!!"
        winsound.PlaySound('snd/critglitch.wav',winsound.SND_LOOP)
        results.config()
        YouFuckedUpBad()
    if(threshold == 420):
        isGlitch = True
        stopgif = False
        didYouGlitch = "GLIIIITCH!"
        winsound.PlaySound('snd/glitch.wav',winsound.SND_ASYNC)
        YouFuckedUpALittle()
    elif(threshold == 999):   
        isCritGlitch = True
        stopgif = False
        didYouCritGlitch = "CRITICAL GLIIIIITCH!!!"
        winsound.PlaySound('snd/critglitch.wav',winsound.SND_ASYNC)
        results.config()
        YouFuckedUpBad()
    rollResults.config(text= "Rolls: "+rollsList)
    rollResults.update()
    results.config(text="Successes: "+str(success)+"\nDid you Succeed?: "+str(didYouSucceed)+byHowMuch+"\nDid you Glitch?: "+didYouGlitch+"\nDid you CRITICAL GLITCH?: "+didYouCritGlitch)
    results.update()
    ROLL.pack()
#BREAK THAT SHIT UP


tk.Label(enterFrame, bg = "grey69", text="First Skill Modifier", font = ("device",20)).grid(row=0)
tk.Label(enterFrame, bg = "grey69", text="Second Skill Modifier", font = ("device",20)).grid(row=1)
tk.Label(enterFrame, bg = "grey69", text="Miscellaneous Modifiers", font = ("device",20)).grid(row=2)
tk.Label(enterFrame, bg = "grey69", text="Success Threshold", font = ("device",20)).grid(row=3)
modifier1 = tk.Entry(enterFrame, font = ("device",20))
modifier2 = tk.Entry(enterFrame, font = ("device",20))
modifier3 = tk.Entry(enterFrame, font = ("device",20))
threshold = tk.Entry(enterFrame, font = ("device",20))
modifier1.insert(0, "0")
modifier2.insert(0, "0")
modifier3.insert(0, "0")
threshold.insert(0, "0")

def doTheThing():
    
    if(not modifier1.get()):
        modifier1.insert(0,"0")
    if(not modifier2.get()):
        modifier2.insert(0,"0")
    if(not modifier3.get()):
        modifier3.insert(0,"0")
    if(not threshold.get()):
        threshold.insert(0,"0")        
    scumsum = (int(modifier1.get())+int(modifier2.get())+int(modifier3.get()))
    pingas = (int(threshold.get()))
    if(scumsum < 1):
        winsound.PlaySound('snd/fail.wav',winsound.SND_ASYNC)
        results.config(text="You can't roll less than 1 die!")
        results.update()
    else:
        ROLL.pack_forget()
        winsound.PlaySound('snd/roll.wav',winsound.SND_ASYNC)
        time.sleep(1)
        roll_x(scumsum, pingas)

#define and place the god damn entry boxes, as well as place the roll button
modifier1.grid(row=0, column=1)
modifier2.grid(row=1, column=1)
modifier3.grid(row=2, column=1)
threshold.grid(row=3, column=1)
ROLL = tk.Button(rollFrame, text = "ROLL", relief = "groove", command = doTheThing)
leftFuckupCoffin = tk.Label(rollFrame, bg="grey69")
rightFuckupCoffin = tk.Label(rollFrame, bg="grey69")
leftFuckupSkull = tk.Label(rollFrame, bg="grey69")
rightFuckupSkull = tk.Label(rollFrame, bg="grey69")
ROLL.config(font=("device", 32))

#Fuckin....animating the god damn bad stuff happening. ridiculous how much this takes. 
leftskullframes = [tk.PhotoImage(file='img/skullflip.gif',format = 'gif -index %i' %(i)) for i in range(4)]
skullframes = [tk.PhotoImage(file='img/skull.gif',format = 'gif -index %i' %(i)) for i in range(4)]
leftcoffinframes = [tk.PhotoImage(file='img/coffinflip.gif',format = 'gif -index %i' %(i)) for i in range(10)]
coffinframes = [tk.PhotoImage(file='img/coffin.gif',format = 'gif -index %i' %(i)) for i in range(10)]
def leftCoffin(ind):
    frame = leftcoffinframes[ind]
    ind += 1
    leftFuckupCoffin.configure(image=frame)
    if(ind == 10):
        ind = 0
    rollFrame.after(125, leftCoffin, ind)
def Coffin(ind):
    frame = coffinframes[ind]
    ind += 1
    rightFuckupCoffin.configure(image=frame)
    if(ind == 10):
        ind = 0   
    rollFrame.after(125, Coffin, ind)
def YouFuckedUpBad():
    leftFuckupCoffin.pack(side="left")
    ROLL.pack(side="left")
    rightFuckupCoffin.pack(side="left")
    if (stopgif == True):
        return
    else:
        rollFrame.after(0,leftCoffin,0)
        rollFrame.after(0,Coffin,0)
        rollFrame.update()

def leftSkull(ind):
    frame = leftskullframes[ind]
    ind += 1
    leftFuckupSkull.configure(image=frame)
    if(ind == 4):
        ind = 0
    rollFrame.after(125, leftSkull, ind)
def Skull(ind):
    frame = skullframes[ind]
    ind += 1
    rightFuckupSkull.configure(image=frame)
    if(ind == 4):
        ind = 0   
    rollFrame.after(125, Skull, ind)

def YouFuckedUpALittle():
    leftFuckupSkull.pack(side="left")
    ROLL.pack(side="left")
    rightFuckupSkull.pack(side="left")
    if (stopgif == True):
        return
    else:
        rollFrame.after(0,leftSkull,0)
        rollFrame.after(0,Skull,0)
        rollFrame.update()

#finished animating all that dumb shit. whatever. 

#pack the Roll section
ROLL.pack(side="left")

#prevent the thing from fucking up too bad if you haven't done the thing yet
defaultText = "You haven't rolled yet!\n"
rollResults = tk.Label(rolls, bg = "grey69", text=defaultText, font = ("device",10))
rollResults.pack()
results = tk.Label(finalFrame, bg = "grey69", text=defaultText, font = ("device",20))
results.pack()


#pack it in fellas we goin 
enterFrame.pack(side="top")
rollFrame.pack(side= "top")
rolls.pack(side="top")
finalFrame.pack(side="bottom")

#ironically this is the only function technically running all the time
window.mainloop()
