#This is the actual version
#Fully functionnal

from math import sqrt
import socket, sys, re
import time

#Informations du serveur
serveur = "challenge01.root-me.org"
port = 52002
nom = "N1h"
canal = "#root-me_challenge"
robot = "candy"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connexion
try:
    s.connect((serveur,port))
except socket.error:
    print("Connexion échoué")
    sys.exit()
print("Connexion réussi")

#Début challenge
#msg1 = "PRIVMSG " + robot + " !ep1\r\n"
#s.send((msg1.encode()))
while True:
    msg_serv1 = s.recv(2048).decode()
    print(msg_serv1)
    msg_parts1 = msg_serv1.split()
    n1=msg_parts1[27]
    msg_parts = msg_parts1[31]
    c=sqrt(int(n1))
    c= c*int(msg_parts)
    #print(f"{c:.2f}")
    msg2 = f"{c:.2f}\r\n"
    #print(msg2)
    s.send(msg2.encode())
    msg_serv2 = s.recv(2048).decode()
    print(msg_serv2)
    break
    

