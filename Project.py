#define a list of devices ( import from a text file | import from excel)
#for each of the devices in the list
    #login into the device
    #enter username and password
    #grab pre config changes (write to file)
    #depoly config template (write to device)
    #grab post config changes (write to file)
import paramiko
import os.path
device_file = open("Device.txt").read().splitlines()
cred = open("cred.txt").read().splitlines()
un = cred[0]
pwd =cred[1]
for device in device_file:
#For each device in device_file login
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())           #Add SSH host key automatically if required
   ssh.connect(device, port=22, username=un, password=pwd)
   print("I'm in")
   ssh.close()
