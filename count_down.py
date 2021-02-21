'''
Project: Simple Countdown Program

Just like it’s hard to find a simple stopwatch application, it can be hard to find a simple countdown application. Let’s write a countdown program that plays an alarm at the end of the countdown.

At a high level, here’s what your program will do:

    Count down from 60.
    Play a sound file (alarm.wav) when the countdown reaches zero.

This means your code will need to do the following:

    Pause for 1 second in between displaying each number in the countdown by calling time.sleep().
    Call subprocess.Popen() to open the sound file with the default application.

Open a new file editor tab and save it as countdown.py.
'''

# a simple countdown script
import time, subprocess
import wave
from playsound import playsound

timeleft = 5
while timeleft > 0:
    print(timeleft, end='\n')
    time.sleep(1)
    timeleft = timeleft - 1
    # todo end of the countdown play sound file
# subprocess.Popen(['start', 'alarm.wav'])
# subprocess.call(['/home/pythonista/Automate_the_boring_stuff/alarm.WAV'])
# subprocess.Popen('/home/pythonista/Automate_the_boring_stuff/alarm.WAV')
# print(wave.open('/home/pythonista/Automate_the_boring_stuff/alarm.WAV', mode='rb'))
playsound('alarm.WAV')