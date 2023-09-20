#This is the old version with IRC

import socket, sys,time, base64, zlib

#Informations du serveur
serveur = "irc.root-me.org"
port = 6667
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
    time.sleep(1)
    s.send((("USER " + nom + " 0 * :Python IRC\r\n").encode()))
    time.sleep(1)
    s.send((("JOIN " + canal + " \r\n").encode()))
    
except socket.error:
    print("Erreur lors de l'envoi des commandes")
    sys.exit()
#Début challenge
msg1 = "PRIVMSG " + robot + " !ep4\r\n"
s.send((msg1.encode()))
while True:
    msg_serv1 = s.recv(2048).decode()
    print(msg_serv1)
    if ":Candy!Candy@root-me.org PRIVMSG N1h :" in msg_serv1:
        msg_parts1 = msg_serv1.split(":")
        print(msg_parts1[2])
        c= base64.b64decode(msg_parts1[2])
        a= (zlib.decompress(c)).decode()
        msg2 = "PRIVMSG " + robot + f" !ep4 -rep {a}\r\n"
        print(c)
        s.send(msg2.encode())
        while True:
            msg_serv2 = s.recv(2048).decode()
            print(msg_serv2)
