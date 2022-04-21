import paramiko
import yaml
import os
import glob

# gets the current active location of the file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(__location__+'\settings.yaml') as f:
    settings = yaml.safe_load(f)

def connect_ssh_sftp(host, user, password):
    # ssh client
    sshclient = paramiko.SSHClient() 
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshclient.connect(host, username=user, password=password)
    return sshclient, sshclient.open_sftp()

def disconnect_ssh_sftp(sshclient, sftpclient):
    sshclient.close()
    sftpclient.close()

def copy_files(sftpclient, local_files, remote_dir):
    # copying files from local dir to destination dir
    for local_file in local_files:
        # filename with folders
        file = local_file.split(local_dir)[-1]
        # changing the path format : windows format to linux
        file = file.replace('\\','/')
        remote_file = remote_dir + file
        # create remote subdir if doesn't exist
        try:
            sftpclient.mkdir(('/').join(remote_file.split('/')[:-1]))
        except OSError:
            pass
        sftpclient.put(local_file, remote_file, callback=None)
        print(remote_file+ ' copied succesfully')

# gets all files inside local_dir and subfolders inside local_dir
local_dir = settings['local_dir']
local_files = glob.glob(local_dir+'/*/*.*') + glob.glob(local_dir+'/*.*')

host1, user1, password1, remote_dir= settings['host1'], settings['username1'], settings['password1'], settings['remote_dir1']
# establish connection
ssh, sftp = connect_ssh_sftp(host1, user1, password1)
# copy files from local to remote
copy_files(sftp, local_files, remote_dir)
# close existing connections
disconnect_ssh_sftp(ssh, sftp)

host2, user2, password2, remote_dir = settings['host2'], settings['username2'], settings['password2'], settings['remote_dir2']
# establish connection
ssh, sftp = connect_ssh_sftp(host2, user2, password2)
# copy files from local to remote
copy_files(sftp, local_files, remote_dir)
# close existing connections
disconnect_ssh_sftp(ssh, sftp)
