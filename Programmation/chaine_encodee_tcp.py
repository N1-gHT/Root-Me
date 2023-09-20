#This is the actual version
#Fully functionnal
import socket, sys, base64

#Informations du serveur
serveur = "challenge01.root-me.org"
port = 52023

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connexion
try:
    s.connect((serveur,port))
except socket.error:
    print("Connexion échoué")
    sys.exit()
print("Connexion réussi")

#Début challenge
while True:
    msg_serv1 = s.recv(2048).decode()
    print(msg_serv1)
    msg_parts1 = msg_serv1.split()
    msg_parts1 = msg_parts1[16]
    print(msg_parts1)
    c= base64.b64decode(msg_parts1).decode('utf-8')
    print(f"{c}\r\n")
    msg2 = f"{c}\n"
    print(msg2)
    s.send(msg2.encode())
    msg_serv2 = s.recv(2048).decode()
    print(msg_serv2)
    break
