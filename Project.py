import paramiko
import os.path
device_file = open("Device.txt").read().splitlines()
cred = open("cred.txt").read().splitlines()
un = cred[0]
pwd =cred[1]
def login():
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Add SSH host key automatically if required
   ssh.connect(device, port=22, username=un, password=pwd)
   print("I'm in")
   ssh.close()
for device in device_file:
   login()
