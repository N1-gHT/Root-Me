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

try:
    s.send((("NICK " + nom + " \r\n").encode()))
    time.sleep(2)
    s.send((("USER " + nom + " 0 * :Python IRC\r\n").encode()))
    time.sleep(2)
    s.send((("JOIN " + canal + " \r\n").encode()))
    
except socket.error:
    print("Erreur lors de l'envoi des commandes")
    sys.exit()
#Début challenge
msg1 = "PRIVMSG " + robot + " !ep1\r\n"
s.send((msg1.encode()))
while True:
    msg_serv1 = s.recv(2048).decode()
    print(msg_serv1)
    if ":Candy!Candy@root-me.org PRIVMSG N1h :" in msg_serv1:
        msg_parts1 = msg_serv1.split(":")
        msg_parts = msg_parts1[2].split("/")
        c=sqrt(int(msg_parts[0]))
        c= c*int(msg_parts[1])
        print(f"!ep1 -rep {c:.2f}")
        msg2 = "PRIVMSG " + robot + f" !ep1 -rep {c:.2f}\r\n"
        s.send(msg2.encode())
        while True:
            msg_serv2 = s.recv(2048).decode()
            print(msg_serv2)
    

