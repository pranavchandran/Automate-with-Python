import time
print(time.ctime())

thismoment = time.time()
print(time.ctime(thismoment))


"""
# The time.sleep() Function

# If you need to pause your program for a while, call the time.sleep() 
# function and pass it the number of seconds you want
# your program to stay paused. Enter the following into the 
# interactive shell
# */
"""

for i in range(3):
    print('tikck')
    time.sleep(2)
    print('tock')