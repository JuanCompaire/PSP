import paramiko
from scp import SCPClient 

def connectSSH():
    print("connect SSH")

    ssh = paramiko.SSHClient()  
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  

    ssh.connect(hostname='127.0.0.1', port=2222, username='linuxserver', password='password')
    print("se conecta maricon de lsocojones")
    scp = SCPClient(ssh.get_transport())
    scp.get('/home/encrypted_data.bin') 
    scp.get('/home/private.pem') 
    print("se descargaron los archvios correctamente")
    
    scp.close()  
    ssh.close()  
    print("SSH end")

connectSSH()  

    
    
        
    