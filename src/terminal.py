

connectedDevices = ['Pi_ico', 'Pi_5'] # TODO: Make python file to update device list
                                       # TODO: In order to add more devices that can be controlled from central device

# Create a recursive function to continually until exit cmd is recieved
def terminal(device, exit = False):
  if exit:
    return
  print('\nPlease enter a command')
  print('Type "help" for command help')
  cmdIn = input(f'@{device}$: ')
  terminalDecoder(cmdIn, device)
  
# Decodes terminal input to a command to run
def terminalDecoder(cmd, currentDevice):
  

  Commands = {
    'exit': 0,
    'devswap': 1
  }

  toExit = False

  commandUpper = cmd.split()
  command = [x.lower() for x in commandUpper]
  
  numOfCmds = command.Count()

  match (Commands[command[0]]):
    case 0: #* EXIT CMD    -----------------------------------------------------------------------
      print('Exiting terminal')
      toExit = True

    case 1: #* DEVSWAP CMD -----------------------------------------------------------------------
      while True:
          print('Select a device to swap to on the list')

          i = 0
          for x in connectedDevices:
            i += 1
            if x != currentDevice:
              print(f'{i} {x}')
            else:
              print(f'{i} {x} [SELECTED]')

          deviceSelected = input('Enter device number')
          

  terminal()


# Welcome message and terminal initalization
print('Welcome, you have opened the Home Automation Main Terminal')
terminal('Pi_5')