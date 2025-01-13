

connectedDevices = ['Pi_ico', 'Pi_5'] # TODO: Make python file to update device list
                                       # TODO: In order to add more devices that can be controlled from central device

# Create a recursive function to continually until exit cmd is recieved
def terminal(device, exit = False):
  if exit:
    return
  print('\nPlease enter a command')
  print('Type "help" for command help')
  cmdIn = input(f'@{device}$: ')
  print(cmdIn)
  terminal('Pi_5', True)


# Welcome message and terminal initalization
print('Welcome, you have opened the Home Automation Main Terminal')
terminal('Pi_5')