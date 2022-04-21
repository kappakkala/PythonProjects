import paramiko
import yaml
import os
import glob

# gets the current active location of the file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(__location__+'\settings.yaml') as f:
    settings = yaml.safe_load(f)

host1, user1, password1, remote_dir, local_dir = settings['host1'], settings['username1'], settings['password1'], settings['remote_dir2'], settings['local_dir']
# gets all files inside local_dir and subfolders inside local_dir
local_files = glob.glob(local_dir+'/*/*.*') + glob.glob(local_dir+'/*.*')

# ssh client
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host1, username=user1, password=password1)
sftp = ssh.open_sftp()

# copying files from local dir to destination dir
for local_file in local_files:
    # filename with folders
    file = local_file.split(local_dir)[-1]
    # changing the path format : windows format to linux
    file = file.replace('\\','/')
    remote_file = remote_dir + file
    # create remote subdir if doesn't exist
    try:
        sftp.mkdir(('/').join(remote_file.split('/')[:-1]))
    except OSError:
        pass
    sftp.put(local_file, remote_file, callback=None)
    print(remote_file+ ' copied succesfully')
# close existing connections
sftp.close()
ssh.close()