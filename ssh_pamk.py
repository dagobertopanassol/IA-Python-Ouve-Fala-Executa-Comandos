# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:42:02 2019

@author: BRQ
sshpass -p dagobrt rsync -avz --bwlimit=1048  /kunzler/setores/ root@192.168.25.5:/mnt/300set/set450/
root:dagobrt 33222
 # Make connection and create shell.
        client.connect(self.ipaddr, self._sshtun_port, self.ssh_user, self.ssh_user_pass)
        shell = client.invoke_shell()
"""
import paramiko
import sys

def restart_samba():
        
    ## EDIT SSH DETAILS ##
    SSH_PORT = "33222"
    SSH_ADDRESS = "177.73.0.158"
    SSH_USERNAME = "root"
    SSH_PASSWORD = "dagobrt"
    #SSH_COMMAND = "echo 'Hello World!' > comOK.txt"
    SSH_COMMAND = "service smb restart"
    
    ## CODE BELOW ##
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ssh_stdin = ssh_stdout = ssh_stderr = None
    
    try:
        ssh.connect(SSH_ADDRESS,port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND)
        print ("comando executado!")
    except Exception as e:
        sys.stderr.write("SSH connection error: {0}".format(e))
    
    if ssh_stdout:
        sys.stdout.write(ssh_stdout.read())
    if ssh_stderr:
        sys.stderr.write(ssh_stderr.read())
    return