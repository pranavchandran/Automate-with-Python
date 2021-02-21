import threading, time

print('Start of Program')
def takeanap():
    time.sleep(5)
    print('WakeUp')

threadobj = threading.Thread(target=takeanap)
threadobj.start()
print('End of program')


'''
Passing Arguments to the Thread’s Target Function
'''
t1threadobj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frog'],
                                kwargs={'sep':'&'})
t1threadobj.start()
print()
