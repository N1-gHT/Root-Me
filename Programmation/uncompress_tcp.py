
import socket, sys,time, base64, zlib
m = 0
#Informations du serveur
serveur = "challenge01.root-me.org"
port = 52022

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connexion
try:
    s.connect((serveur,port))
except socket.error:
    print("Connexion échoué")
    sys.exit()
print("Connexion réussi")

#Début challenge

msg_serv1 = s.recv(2048).decode()
msg_parts1 = msg_serv1.split()
msg_parts1 = msg_parts1[16]
c= base64.b64decode(msg_parts1)
a= (zlib.decompress(c)).decode()
msg2 = f"{a}\n"
while m < 5:
    s.send(msg2.encode())
    m+=1
    msg_serv2 = s.recv(2048).decode()
    print(msg_serv2)
