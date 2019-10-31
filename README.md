# MonetIncentTask
Monetary Incentive Task for experimental purposes, developed at Poznań Laboratory of Affective Neuroscience
v2.0

To run an experiment without setting up ports, run dev.py (but it is developement version, so it may not always be stable).
To run full-lab experiment, run MIT.py.

## Progress
First version finished, now it is going to encounter cosmetical changes.

## Technologies
Psychopy3, Python3, Numpy

## Scope of functionalities
Code presented above is performing Monetary Incentive Task

Firstly there is trial that measures subject's responses, from which it creates a baseline for duration of stimuli
in block of experiment. Subject's task is to response before stimuli disappear.
Then it adapts to subject, making duration of stimuli shorter or longer dependantly on subject's responses,
thus the overall score is always advancing toward 50% for right and bad responses.

### Stimuli 

Stimuli is a simple white rectangle, before it's appearance the cue (cross) is suggesting it's position

### Feedback

After performing single trial in task, the feeback is provided to the user, positive is:

![alt text](https://github.com/stakar/MonetIncentTask/blob/master/stimuli/happy.png "Logo Title Text 1")

and negative:

![alt text](https://github.com/stakar/MonetIncentTask/blob/master/stimuli/sad.png "Logo Title Text 1")

Also, lack of, or too fast reaction are providing feedback.

## References
FMRI Visualization of Brain Activity during a Monetary Incentive Delay Task (2000)

Peirce, JW  Generating stimuli for neuroscience using PsychoPy.(2009)

Peirce, JW  PsychoPy - Psychophysics software in Python.(2007)
