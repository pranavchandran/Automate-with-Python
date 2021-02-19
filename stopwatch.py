# My StopWatch

"""

Track the amount of time elapsed between presses of the ENTER key, 
with each key press starting a new “lap” on the timer.
Print the lap number, total time, and lap time.

This means your code will need to do the following:

Find the current time by calling time.time() and store it as a 
timestamp at the start of the program, as well as at the start of 
each lap.
Keep a lap counter and increment it every time the user presses ENTER.
Calculate the elapsed time by subtracting timestamps.
Handle the KeyboardInterrupt exception so the user can
 press CTRL-C to quit.
"""

import time

print('Press Enter to begin.Afterward, press Enter to click the stopwatch.\
Press Cntrl-C to quit')

input()
print('Started')
starttime = time.time()
lasttime = starttime
lapnum = 1

"""Now that we’ve written the code to display the instructions,
start the first lap, note the time, and set our lap count to 1."""

# start tracking lap times
try:
    while True:
        input()
        laptime = round(time.time() - lasttime, 2)
        totaltime = round(time.time() - starttime, 2)
        print('Lap #%s: %s: (%s)'%(lapnum, totaltime, laptime), end='')
        lapnum += 1
        lasttime = time.time()
except KeyboardInterrupt:
    # handle the cntrl+c exception to keep error message
    print('\nDone')
