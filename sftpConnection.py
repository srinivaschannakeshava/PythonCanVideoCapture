import paramiko
import os
#import  StringIO

#f = open('/home/bosch/Desktop/pythonvideocapture/test_sftp.private.pem','r')
#s = f.read()
#print s
#keyfile = StringIO.StringIO()
#keyfile.write(s)

private_key='/home/pi/Desktop/pythonvideocapture/unencrypted_openssh.pem'

#print keyfile

privkey = paramiko.RSAKey.from_private_key_file(private_key)

host = '52.6.132.169' # remote hostname where SSH server is running
port = 22
user_name = 'ubuntu'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#trans = paramiko.Transport((host, port))


ssh.connect(host, username=user_name, pkey=privkey )
#transport = paramiko.Transport((host, port))
#transport.connect(username = user_name, password ='')
sftp = ssh.open_sftp()
filepath = '/home/ubuntu/test/pi_1.avi'
localpath = '/home/pi/Desktop/pythonvideocapture/pi_1.avi'

#sftp.get(filepath, localpath)
sftp.put(localpath,filepath)


#stdin,stdout,stderr = ssh.exec_command("ls")
 
#for line in stdout.readlines():
 #        print line.strip()
sftp.close()
#transport.close()
ssh.close()

#ssh.connect(host, username=user_name, key_filename=private_key)



