import paramiko
import yaml
import os

# gets the current active location of the file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(__location__+'\credentials.yaml') as f:
    credentials = yaml.safe_load(f)


host1, user1, password1, source_directory = credentials['host1'], credentials['username1'], credentials['password1'], credentials['source_directory2']

transport = paramiko.Transport((host1, 22))
transport.connect(username =user1, password = password1)
sftp = paramiko.SFTPClient.from_transport(transport)
try:
    # creates a directory if it doesn't exists
    sftp.mkdir(source_directory)
except OSError:
    pass
inbound_files=sftp.listdir(source_directory)
sftp.close()
transport.close()

ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host1, username=user1, password=password1)
sftp = ssh.open_sftp()
# copying a single file to the destination
sftp.put(__location__+'\credentials.yaml', source_directory+'credentials.yaml', callback=None)
sftp.close()
ssh.close()
