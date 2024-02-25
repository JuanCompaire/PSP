import paramiko
from scp import SCPClient 
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def examen():
    connectSSH()
    desEncrypt()

def connectSSH():
    print("connect SSH")

    ssh = paramiko.SSHClient()  
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  

    ssh.connect(hostname='127.0.0.1', port=2222, username='linuxserver', password='password')
    print("se conecta maricon de lsocojones")
    scp = SCPClient(ssh.get_transport())
    scp.get('/encryted_data.bin') 
    scp.get('/private.pem') 
    print("se descargaron los archvios correctamente")
    
    scp.close()  
    ssh.close()  
    print("SSH end")

def desEncrypt():
    print("Desencriptar")
    file_in = open("encryted_data.bin","rb")
    private_key = RSA.import_key(open("private.pem").read())
    enc_session_key = file_in.read(private_key.size_in_bytes())
    file_in.close()
    
    #Desencriptar
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    self.session_key = cipher_rsa.decrypt(enc_session_key)
    print(self.session_key)
    print("Desencriptar finish fish")
    
    
    

examen()

 

    
    
        
    