import keyboard
from time import sleep
from queue import Queue

connectedDevices = ['Pi_pico', 'Pi_5'] # TODO: Make python file to update device list
                                       # TODO: In order to add more devices that can be controlled from central device

# Adds 
EventQueue = Queue()

def EventListener(eventMsg, device):
  EventQueue.put(f'@{device}: {eventMsg}')

exitFlag = False

while not exitFlag:
  if not EventQueue.empty():
    print(EventQueue.get())
  
  sleep(1)
  