"""
Monetary Incentive Task


This script is being developed for PLAN experimental purposes. I is performing Monetary Incentive Task, measuring time reactions and percent of accurate responses.



------------
| Workflow |
------------

Modules:
    1.Pre-trial
    Stimuli is presented on the screen
    In this module, the respondent is instructed to response as fast as possible for stimuli displayed on the screen.
    The mean time reaction is obtained.
    2.Trial
    The stimuli is displayed on screen 50% times longer than mean time reaction from pre-trial and shorter in 50% of cases, after this time it
    disappears. After respondent's reaction the feedback is provided about accuracy.
    Respondent is instructed to react for stimuli before it deisappears.
    Reaction times are obtained.
    
TODO:
    1.Pre-trial
    2.Trial
    3.Instructions
    4.mechanism for calculating response time


"""



###########
# Modules #
###########

from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
import numpy as np 
import threading
import random
import time
from psychopy.hardware import keyboard


##################
# INITIALIZATION #
##################

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'PLAN_Experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
#dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
#if dlg.OK == False:
#    core.quit()  # user pressed cancel
#expInfo['date'] = data.getDateStr()  # add a simple timestamp
#expInfo['expName'] = expName
#expInfo['psychopyVersion'] = psychopyVersion



win = visual.Window([800,600], monitor="testMonitor", units="deg")





#############
# Pre-trial #
#############

stim = visual.Rect(
    win=win,
    units = "pix",
    width = 300,
    height = 300,
    pos = [0,0],
    fillColor = [0,1,0]
)
start = time.time()
response_times = []
#def myfunc():
 #   pass

#event.globalKeys.add(key='space',func=myfunc)

keyResp = keyboard.Keyboard()
 

for n in range(5):
    time.sleep(random.randint(1,2))
    stim.draw()
    win.flip()
    win.callOnFlip(keyResp.clock.reset)
    zegarek = core.Clock()
    time.sleep(random.random())
    win.clearBuffer()
    win.flip()
    
    theseKeys = keyResp.getKeys(keyList=['space'],waitRelease=False)
    
#    if 'space' in theseKeys:
        
    print(theseKeys.__len__() )
    try:
        print(theseKeys[0].rt)
    except:
        print("No touchin\'")

win.clearBuffer()
win.flip()

core.wait(1.0) 

win.close()
