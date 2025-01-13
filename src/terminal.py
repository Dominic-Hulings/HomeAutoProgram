

connectedDevices = ['Pi_pico', 'Pi_5'] # TODO: Make python file to update device list
                                       # TODO: In order to add more devices that can be controlled from central device

# Create a recursive function to continually until exit cmd is recieved
def terminal(device, exit = False):
  print(f'Current device: {device}')
  print(f'Current exit flag status: {exit}')
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
    'help': 1,
    'devswap': 2
  }

  toExit = False
  device = currentDevice

  commandUpper = cmd.split()
  command = [x.lower() for x in commandUpper]
  
  numOfCmds = len(command)

  match (Commands[command[0]]):
    case 0: #* EXIT CMD    -----------------------------------------------------------------------
      print('Exiting terminal')
      toExit = True

    case 1: #* HELP CMD    -----------------------------------------------------------------------
      with open('helpdocs.txt', 'r') as file:
        print (file.read())

    case 2: #* DEVSWAP CMD -----------------------------------------------------------------------
      while True:
          print('\nSelect a device to swap to on the list')

          i = 0
          for x in connectedDevices:
            i += 1
            if x != currentDevice:
              print(f'{i} {x}')
            else:
              print(f'{i} {x} [SELECTED]')

          deviceSelected = int(input('Enter device number: '))

          if deviceSelected > len(connectedDevices):
            print(f'Device number {deviceSelected} not found!')
            continue

          choice = input(f'Swap to {connectedDevices[deviceSelected - 1]}? y/n')

          if choice.lower() == 'n':
            print('Please reselect a device')
            continue
          elif choice.lower() == 'y':
            print(f'Swapped to device {connectedDevices[deviceSelected - 1]}')
            device = connectedDevices[deviceSelected - 1]
            break;
          else:
            print(f'Input {choice} not recognized as "y" or "n". Please try again')
            continue

    case _: #* DEFAULT CASE -----------------------------------------------------------------------
      print(f'Command number {Commands[command[0]]} not found in dictionary')
      print('Default case evaluated')
    
  terminal(device, toExit)


# Welcome message and terminal initalization
print('Welcome, you have opened the Home Automation Main Terminal')
terminal('Pi_5')