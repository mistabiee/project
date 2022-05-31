#define a list of devices ( import from a text file | import from excel)
#for each of the devices in the list
    #login into the device
    #enter username and password
    #grab pre config changes (write to file)
    #depoly config template (write to device)
    #grab post config changes (write to file)
import paramiko
import os.path

ssh = paramiko.SSHClient
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())           #Add SSH host key automatically if required
ssh.connect("10.57.128.1", port=22, username="olaleyea", password="Adedamola86")
print("I'm in")
ssh.close()