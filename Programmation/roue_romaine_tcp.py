#This is the actual version
#Fully fuctionnal but response is wrong

import socket, sys, codecs
#Informations du serveur
serveur = "challenge01.root-me.org"
port = 52021

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
print(msg_serv1)
msg_parts1 = msg_serv1.split()
msg_parts1 = msg_parts1[16]
c = codecs.decode(msg_parts1, "rot_13")
msg2 = f"{c}\n"
print(msg2)
s.send(msg2.encode())
msg_serv2 = s.recv(655350).decode()
print(msg_serv2)
