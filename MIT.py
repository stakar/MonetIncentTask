#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Monetary Incentive Task

This script is being developed for PLAN experimental purposes.
I is performing Monetary Incentive Task, measuring time reactions and percent of accurate responses.

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

This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on lipiec 03, 2019, at 12:48
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
from tools import *
from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'MIT_Exp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

too_fast = False
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\Python\\PsychoPy\\untitled.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window

# win = visual.Window(
#     size=(1024, 768), fullscr=True, screen=0,
#     winType='pyglet', allowGUI=False, allowStencil=False,
#     monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
#     blendMode='avg', useFBO=True,
    # units='deg')

# Sometimes the code above works, sometimes one needs to use the one below

win = visual.Window([1920,1080],fullscr=True, allowGUI=True,
monitor='default_monitor', units='deg', color=[0,0,0])
# size of the window in pixels (X,Y), should at least match the .bmp files that are presented


# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instrukcja_1"
Instrukcja_1Clock = core.Clock()
Inst_1 = visual.TextStim(win=win, name='Inst_1',
    text='W tej części badania będziemy mierzyli Twój czas reakcji. Twoim zadaniem będzie jak najszybsze naciśnięcie spacji, gdy na ekranie komputera wyświetli się biały kwadrat.\n \n'
 'Na końcu drugiej części zadania otrzymasz informację odnośnie tego, jak dobrze poradziłeś/aś sobie z jego wykonaniem w porównaniu do pozostałych uczestników badania. \n \n'
'Jeśli masz jakieś pytania zawołaj osobę przeprowadzającą badanie.\n \n''Naciśnij Enter, aby rozpocząć pierwszą część tego zadania. ',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=20,ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "Instrukcja_1"
SCB = get_scoreboard('scores.txt')
scoreBoardClock = core.Clock()
scoreBoard = visual.TextStim(win=win, name='scoreBoard',
    text=SCB,
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=20, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "Przerwa"
PrzerwaClock = core.Clock()
Clear_screen = visual.TextStim(win=win, name='Clear_screen',
    text=None,
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fix"
fixClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

fixDuration = np.random.uniform(1.5,2.5)

# Initialize components for Routine "Trial_1"
Trial_1Clock = core.Clock()
Stimulus = visual.ImageStim(
        win=win,
        name='stimuli.jpg',
        image='stimuli.jpg', mask=None,
        ori=0, pos=(0, 0), size=(10, 10),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "Mean"
MeanClock = core.Clock()

# Initialize components for Routine "Instrukcja_2"
Instrukcja_2Clock = core.Clock()
Inst_2 = visual.TextStim(win=win, name='Inst_2',
    text='To jest koniec pierwszej części tego zadania. Przeczytaj instrukcję do części drugiej, a jeśli coś będzie niejasne lub będziesz miał jakieś pytania, zawołaj osobę przeprowadzającą badanie. \n \n'
'W tej części zadania znowu będziesz musiał(a) jak najszybciej zareagować gdy na ekranie komputera pojawi się biały kwadrat. '
'Tym razem jednak Twoim zadaniem będzie naciśnięcie spacji zanim kwadrat zniknie z ekranu.'
'Jeśli Ci się to uda, na ekranie komputera wyświetli się emotikon uśmiechniętej twarzy. '
'Jeśli naciśniesz spację zbyt wolno, pojawi się obrazek rozzłoszczonej twarzy. \n \n'
'Postaraj się wykonać to zadanie najlepiej jak potrafisz. Jeśli otrzymasz wystarczająco wysoki wynik, trafisz na listę najlepszych graczy. \n \n'
'Naciśnij Enter aby zobaczyć listę najlepszych graczy.',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=20, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial_2"
Trial_2Clock = core.Clock()
Bodziec = visual.ImageStim(
    win=win,
    name='stimuli.jpg',
    image='stimuli.jpg', mask=None,
    ori=0, pos=(0, 0), size=(10, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "feedback"

meanRT = [] #placeholder for responses, to compute a baseline of stim duration
feedVal = [] #placeholder for feedback values, for deciding hardness

feedbackClock = core.Clock()

feedbackfile =['happy.png','sad.png','noReaction.png','tooFast.png']

msg= ""
image = visual.ImageStim(
    win=win,
    name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(10, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "Koniec"
KoniecClock = core.Clock()
End = visual.TextStim(win=win, name='End',
    text='Koniec',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "Instrukcja_1"-------
t = 0
Instrukcja_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_inst_1 = keyboard.Keyboard()
# keep track of which components have finished
Instrukcja_1Components = [Inst_1, key_resp_inst_1]
for thisComponent in Instrukcja_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instrukcja_1"-------
while continueRoutine:
    # get current time
    t = Instrukcja_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Inst_1* updates
    if t >= 0.0 and Inst_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Inst_1.tStart = t  # not accounting for scr refresh
        Inst_1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Inst_1, 'tStartRefresh')  # time at next scr refresh
        Inst_1.setAutoDraw(True)

    # *key_resp_inst_1* updates
    if t >= 0.0 and key_resp_inst_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_inst_1.tStart = t  # not accounting for scr refresh
        key_resp_inst_1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_inst_1, 'tStartRefresh')  # time at next scr refresh
        key_resp_inst_1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_inst_1.clock.reset)  # t=0 on next screen flip
        key_resp_inst_1.clearEvents(eventType='keyboard')
    if key_resp_inst_1.status == STARTED:
        theseKeys = key_resp_inst_1.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_inst_1.keys = theseKeys.name  # just the last key pressed
            key_resp_inst_1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instrukcja_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrukcja_1"-------
for thisComponent in Instrukcja_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Inst_1.started', Inst_1.tStartRefresh)
thisExp.addData('Inst_1.stopped', Inst_1.tStopRefresh)
# check responses
if key_resp_inst_1.keys in ['', [], None]:  # No response was made
    key_resp_inst_1.keys = None
thisExp.addData('key_resp_inst_1.keys',key_resp_inst_1.keys)
if key_resp_inst_1.keys != None:  # we had a response
    thisExp.addData('key_resp_inst_1.rt', key_resp_inst_1.rt)
thisExp.addData('key_resp_inst_1.started', key_resp_inst_1.tStartRefresh)
thisExp.addData('key_resp_inst_1.stopped', key_resp_inst_1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instrukcja_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#Duration of break
breakDuration = np.random.uniform(0.5,1)

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=3, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='test')
thisExp.addLoop(test)  # add the loop to the experiment
thisTest = test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest:
        exec('{} = thisTest[paramName]'.format(paramName))

for thisTest in test:
    currentLoop = test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))

    # ------Prepare to start Routine "Przerwa"-------
    t = 0
    PrzerwaClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # routineTimer.add(0.500000)
    routineTimer.add(breakDuration)
    # update component parameters for each repeat
    # keep track of which components have finished
    PrzerwaComponents = [Clear_screen]
    for thisComponent in PrzerwaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Przerwa"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PrzerwaClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Clear_screen* updates
        if t >= 0.0 and Clear_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            Clear_screen.tStart = t  # not accounting for scr refresh
            Clear_screen.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Clear_screen, 'tStartRefresh')  # time at next scr refresh
            Clear_screen.setAutoDraw(True)
        frameRemains = 0.0 + breakDuration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Clear_screen.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Clear_screen.tStop = t  # not accounting for scr refresh
            Clear_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Clear_screen, 'tStopRefresh')  # time at next scr refresh
            Clear_screen.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break

        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PrzerwaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()


    # -------Ending Routine "Przerwa"-------
    for thisComponent in PrzerwaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Clear_screen.started', Clear_screen.tStartRefresh)
    thisExp.addData('Clear_screen.stopped', Clear_screen.tStopRefresh)
    breakDuration = np.random.uniform(1,2)


    # ------Prepare to start Routine "Trial_1"-------
    t = 0
    Trial_1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    test_resp = keyboard.Keyboard()
    # keep track of which components have finished
    Trial_1Components = [Stimulus, test_resp]
    for thisComponent in Trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Trial_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Trial_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Stimulus* updates
        if t >= 0 and Stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stimulus.tStart = t  # not accounting for scr refresh
            Stimulus.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Stimulus, 'tStartRefresh')  # time at next scr refresh
            Stimulus.setAutoDraw(True)
        frameRemains = 0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Stimulus.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Stimulus.tStop = t  # not accounting for scr refresh
            Stimulus.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Stimulus, 'tStopRefresh')  # time at next scr refresh
            Stimulus.setAutoDraw(False)

        # *test_resp* updates
        if t >= 0 and test_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_resp.tStart = t  # not accounting for scr refresh
            test_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(test_resp, 'tStartRefresh')  # time at next scr refresh
            test_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(test_resp.clock.reset)  # t=0 on next screen flip
            test_resp.clearEvents(eventType='keyboard')
        frameRemains = 0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if test_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            test_resp.tStop = t  # not accounting for scr refresh
            test_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test_resp, 'tStopRefresh')  # time at next scr refresh
            test_resp.status = FINISHED
        if test_resp.status == STARTED:
            theseKeys = test_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                test_resp.keys = theseKeys.name  # just the last key pressed
                test_resp.rt = theseKeys.rt
                print(test_resp.rt)
                meanRT.append(test_resp.rt)
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Trial_1"-------
    for thisComponent in Trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test.addData('Stimulus.started', Stimulus.tStartRefresh)
    test.addData('Stimulus.stopped', Stimulus.tStopRefresh)
    # check responses
    if test_resp.keys in ['', [], None]:  # No response was made
        test_resp.keys = None
    test.addData('test_resp.keys',test_resp.keys)
    if test_resp.keys != None:  # we had a response
        test.addData('test_resp.rt', test_resp.rt)
    test.addData('test_resp.started', test_resp.tStartRefresh)
    test.addData('test_resp.stopped', test_resp.tStopRefresh)
    thisExp.nextEntry()

# completed 10 repeats of 'test'
print(meanRT)
baseline = np.mean(meanRT)

#duration of first stimulus in Trial_2
duration = np.round(np.random.uniform(0.1,2*baseline),2)


# ------Prepare to start Routine "Instrukcja_2"-------
t = 0
Instrukcja_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_inst_2 = keyboard.Keyboard()
# keep track of which components have finished
Instrukcja_2Components = [Inst_2, key_resp_inst_2]
for thisComponent in Instrukcja_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instrukcja_2"-------
while continueRoutine:
    # get current time
    t = Instrukcja_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Inst_2* updates
    if t >= 1 and Inst_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Inst_2.tStart = t  # not accounting for scr refresh
        Inst_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Inst_2, 'tStartRefresh')  # time at next scr refresh
        Inst_2.setAutoDraw(True)

    # *key_resp_inst_2* updates
    if t >= 1 and key_resp_inst_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_inst_2.tStart = t  # not accounting for scr refresh
        key_resp_inst_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_inst_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_inst_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_inst_2.clock.reset)  # t=0 on next screen flip
        key_resp_inst_2.clearEvents(eventType='keyboard')
    if key_resp_inst_2.status == STARTED:
        theseKeys = key_resp_inst_2.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_inst_2.keys = theseKeys.name  # just the last key pressed
            key_resp_inst_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instrukcja_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrukcja_2"-------
for thisComponent in Instrukcja_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Inst_2.started', Inst_2.tStartRefresh)
thisExp.addData('Inst_2.stopped', Inst_2.tStopRefresh)
# check responses
if key_resp_inst_2.keys in ['', [], None]:  # No response was made
    key_resp_inst_2.keys = None
thisExp.addData('key_resp_inst_2.keys',key_resp_inst_2.keys)
if key_resp_inst_2.keys != None:  # we had a response
    thisExp.addData('key_resp_inst_2.rt', key_resp_inst_2.rt)
thisExp.addData('key_resp_inst_2.started', key_resp_inst_2.tStartRefresh)
thisExp.addData('key_resp_inst_2.stopped', key_resp_inst_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instrukcja_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



#In case of moving,start here

# ------Prepare to start Routine "scoreBoard"-------
t = 0
scoreBoardClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_scoreBoard = keyboard.Keyboard()
# keep track of which components have finished
scoreBoardComponents = [scoreBoard, key_resp_scoreBoard]
for thisComponent in scoreBoardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED


# -------Start Routine "scoreBoard"-------
while continueRoutine:
    # get current time
    t = scoreBoardClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *scoreBoard* updates
    if t >= 0.0 and scoreBoard.status == NOT_STARTED:
        # keep track of start time/frame for later
        scoreBoard.tStart = t  # not accounting for scr refresh
        scoreBoard.frameNStart = frameN  # exact frame index
        win.timeOnFlip(scoreBoard, 'tStartRefresh')  # time at next scr refresh
        scoreBoard.setAutoDraw(True)

    # *key_resp_scoreBoard* updates
    if t >= 0.0 and key_resp_scoreBoard.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_scoreBoard.tStart = t  # not accounting for scr refresh
        key_resp_scoreBoard.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_scoreBoard, 'tStartRefresh')  # time at next scr refresh
        key_resp_scoreBoard.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_scoreBoard.clock.reset)  # t=0 on next screen flip
        key_resp_scoreBoard.clearEvents(eventType='keyboard')
    if key_resp_scoreBoard.status == STARTED:
        theseKeys = key_resp_scoreBoard.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_scoreBoard.keys = theseKeys.name  # just the last key pressed
            key_resp_scoreBoard.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scoreBoardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scoreBoard"-------
for thisComponent in scoreBoardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('scoreBoard.started', scoreBoard.tStartRefresh)
thisExp.addData('scoreBoard.stopped', scoreBoard.tStopRefresh)
# check responses
if key_resp_scoreBoard.keys in ['', [], None]:  # No response was made
    key_resp_scoreBoard.keys = None
thisExp.addData('key_resp_scoreBoard.keys',key_resp_scoreBoard.keys)
if key_resp_inst_1.keys != None:  # we had a response
    thisExp.addData('key_resp_inst_1.rt', key_resp_scoreBoard.rt)
thisExp.addData('key_resp_scoreBoard.started', key_resp_scoreBoard.tStartRefresh)
thisExp.addData('key_resp_scoreBoard.stopped', key_resp_scoreBoard.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instrukcja_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# set up handler to look after randomisation of conditions etc

#BELOW nREPs defines number of repetition in trial, change when you know how
#many trials should be

trial_block_1 = data.TrialHandler(nReps=10, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_block_1')
thisExp.addLoop(trial_block_1)  # add the loop to the experiment
thisTrial_block_1 = trial_block_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_block_1.rgb)
if thisTrial_block_1 != None:
    for paramName in thisTrial_block_1:
        exec('{} = thisTrial_block_1[paramName]'.format(paramName))

for thisTrial_block_1 in trial_block_1:
    currentLoop = trial_block_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_block_1.rgb)
    if thisTrial_block_1 != None:
        for paramName in thisTrial_block_1:
            exec('{} = thisTrial_block_1[paramName]'.format(paramName))

    # ------Prepare to start Routine "Przerwa"-------
    t = 0
    PrzerwaClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # routineTimer.add(2.000000)
    routineTimer.add(0.5)

    # update component parameters for each repeat
    key_resp2 = keyboard.Keyboard()
    # keep track of which components have finished
    PrzerwaComponents = [Clear_screen,key_resp2]
    for thisComponent in PrzerwaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Przerwa"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PrzerwaClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Clear_screen* updates
        if t >= 0.0 and Clear_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            Clear_screen.tStart = t  # not accounting for scr refresh
            Clear_screen.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Clear_screen, 'tStartRefresh')  # time at next scr refresh
            Clear_screen.setAutoDraw(True)
        frameRemains = 0.0 + breakDuration - win.monitorFramePeriod * 0.75  # most of one frame period left
        if Clear_screen.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Clear_screen.tStop = t  # not accounting for scr refresh
            Clear_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Clear_screen, 'tStopRefresh')  # time at next scr refresh
            Clear_screen.setAutoDraw(False)
            theseKeys = key_resp2.getKeys(keyList=['space'], waitRelease=False)


        # *key_resp* updates
        if t >= 0.0 and key_resp2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp2.tStart = t  # not accounting for scr refresh
            key_resp2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
            key_resp2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
            key_resp2.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + breakDuration - win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp2.tStop = t  # not accounting for scr refresh
            key_resp2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp2, 'tStopRefresh')  # time at next scr refresh
            key_resp2.status = FINISHED

        if key_resp2.status == STARTED:
            theseKeys = key_resp2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp2.keys = theseKeys.name  # just the last key pressed
                key_resp2.rt = theseKeys.rt
                too_fast = True


        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PrzerwaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

        breakDuration = np.random.uniform(1,2)


    # -------Ending Routine "Przerwa"-------
    for thisComponent in PrzerwaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Clear_screen.started', Clear_screen.tStartRefresh)
    thisExp.addData('Clear_screen.stopped', Clear_screen.tStopRefresh)

    # ------Prepare to start Routine "fix"-------
    t = 0
    fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    key_resp2 = keyboard.Keyboard()
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [Fixation,key_resp2]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Fixation* updates
        if t >= 1 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t  # not accounting for scr refresh
            Fixation.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        frameRemains = fixDuration - win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Fixation.tStop = t  # not accounting for scr refresh
            Fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(False)

        # *key_resp* updates
        if t >= 0.0 and key_resp2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp2.tStart = t  # not accounting for scr refresh
            key_resp2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
            key_resp2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
            key_resp2.clearEvents(eventType='keyboard')
        frameRemains = fixDuration - win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp2.tStop = t  # not accounting for scr refresh
            key_resp2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp2, 'tStopRefresh')  # time at next scr refresh
            key_resp2.status = FINISHED

        if key_resp2.status == STARTED:
            theseKeys = key_resp2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp2.keys = theseKeys.name  # just the last key pressed
                key_resp2.rt = theseKeys.rt
                too_fast = True



        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_block_1.addData('Fixation.started', Fixation.tStartRefresh)
    trial_block_1.addData('Fixation.stopped', Fixation.tStopRefresh)
    fixDuration = np.random.uniform(1,2)


    # ------Prepare to start Routine "Trial_2"-------
    t = 0
    Trial_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    key_resp = keyboard.Keyboard()
    # keep track of which components have finished
    Trial_2Components = [Bodziec, key_resp]
    for thisComponent in Trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Trial_2"-------
    while continueRoutine and routineTimer.getTime() > 0 and too_fast != True:
        # get current time
        t = Trial_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Bodziec* updates
        if t >= 0.0 and Bodziec.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bodziec.tStart = t  # not accounting for scr  refresh
            Bodziec.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Bodziec, 'tStartRefresh')  # time at next scr refresh
            Bodziec.setAutoDraw(True)
            #below variable duration defines how long the stimulus is shown
        frameRemains = 0.0 + duration - win.monitorFramePeriod * 0.75  # most of one frame period left
        if Bodziec.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Bodziec.tStop = t  # not accounting for scr refresh
            Bodziec.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Bodziec, 'tStopRefresh')  # time at next scr refresh
            Bodziec.setAutoDraw(False)

        # *key_resp* updates
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            key_resp.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED


        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                print(test_resp.rt) #print response, testing purposes
                meanRT.append(test_resp.rt) #append response to previous ones
                baseline = np.mean(meanRT) #calculate new baseline
                print(baseline)
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Trial_2"-------
    for thisComponent in Trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_block_1.addData('Bodziec.started', Bodziec.tStartRefresh)
    trial_block_1.addData('Bodziec.stopped', Bodziec.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trial_block_1.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trial_block_1.addData('key_resp.rt', key_resp.rt)
    trial_block_1.addData('key_resp.started', key_resp.tStartRefresh)
    trial_block_1.addData('key_resp.stopped', key_resp.tStopRefresh)


    # ------Prepare to start Routine "Przerwa"-------
    t = 0
    PrzerwaClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    PrzerwaComponents = [Clear_screen]
    for thisComponent in PrzerwaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Przerwa"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PrzerwaClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Clear_screen* updates
        if t >= 0.0 and Clear_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            Clear_screen.tStart = t  # not accounting for scr refresh
            Clear_screen.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Clear_screen, 'tStartRefresh')  # time at next scr refresh
            Clear_screen.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Clear_screen.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Clear_screen.tStop = t  # not accounting for scr refresh
            Clear_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Clear_screen, 'tStopRefresh')  # time at next scr refresh
            Clear_screen.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PrzerwaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()


    # -------Ending Routine "Przerwa"-------
    for thisComponent in PrzerwaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Clear_screen.started', Clear_screen.tStartRefresh)
    thisExp.addData('Clear_screen.stopped', Clear_screen.tStopRefresh)


    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    print(key_resp.rt)

    if too_fast == True:
        fdb = feedbackfile[3] #reaction before stimuli
        feedVal.append(0)
        too_fast = False
    else:
        if key_resp.rt != list(): #test if there was response
            if key_resp.rt < duration:
                fdb = feedbackfile[0] #positive feedback
                feedVal.append(1)
            else:
                fdb = feedbackfile[1] #negative feedback
                feedVal.append(0)
        else:
            fdb = feedbackfile[2] #no-response feedback
            feedVal.append(0)


    image.setImage(fdb)
    # keep track of which components have finished
    feedbackComponents = [image]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
            #set duration of next stimulus
            if (np.count_nonzero(feedVal)/len(feedVal))<0.5:
                duration = np.round(np.random.uniform(0.1,2*baseline),2)
            else:
                duration = np.round(np.random.uniform(0.1,baseline),2)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_block_1.addData('image.started', image.tStartRefresh)
    trial_block_1.addData('image.stopped', image.tStopRefresh)
    thisExp.nextEntry()

# completed 5 repeats of 'trial_block_1'

print(feedVal)
print('Procent poprawnych odpowiedzi: {}%'.format((np.count_nonzero(feedVal)/len(feedVal)*100)))

print('Participant is {}'.format(expInfo['participant']))

save_score('scores.txt',expInfo['participant'],baseline)


# ------Prepare to start Routine "Koniec"-------
t = 0
KoniecClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = keyboard.Keyboard()
# keep track of which components have finished
KoniecComponents = [End, key_resp_2]
for thisComponent in KoniecComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Koniec"-------
while continueRoutine:
    # get current time
    t = KoniecClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *End* updates
    if t >= 1 and End.status == NOT_STARTED:
        # keep track of start time/frame for later
        End.tStart = t  # not accounting for scr refresh
        End.frameNStart = frameN  # exact frame index
        win.timeOnFlip(End, 'tStartRefresh')  # time at next scr refresh
        End.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 1 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # not accounting for scr refresh
        key_resp_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in KoniecComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Koniec"-------
for thisComponent in KoniecComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('End.started', End.tStartRefresh)
thisExp.addData('End.stopped', End.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Koniec" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
