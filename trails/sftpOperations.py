import paramiko
import os

class sftpOperations:
  private_key='/home/pi/Desktop/pythonvideocapture/unencrypted_openssh.pem'  
  privkey = paramiko.RSAKey.from_private_key_file(private_key)
  host = '52.6.132.169' # remote hostname where SSH server is running
  port = 22
  user_name = 'ubuntu'
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  sftp=None;

  @staticmethod	
  def connectToSftp():
	sftpOperations.ssh.connect(sftpOperations.host, username=sftpOperations.user_name, pkey=sftpOperations.privkey )
  
  @staticmethod	
  def pushToServer(fileName):

	print('Compressing the Video .... ')
	print("----------------------------------------------------")
	os.system('avconv -i '+fileName+' -s 640x360 -pass 1 com_'+fileName)
	print("-------------------------------------------------------------")	
	print('File compressed')
	print("-------------------------------------------------------------")
	print("Pushing file to SFTP server ...")
	sftpOperations.sftp = sftpOperations.ssh.open_sftp()
	filepath = '/home/ubuntu/test/'+fileName
	localpath = '/home/pi/Desktop/pythonvideocapture/trails/com_'+fileName
	sftpOperations.sftp.put(localpath,filepath)
	print("----------------------------------------------------")
	print('SFTP Operation done')

  @staticmethod	
  def closeConnection():
	sftpOperations.sftp.close()
	sftpOperations.ssh.close()
