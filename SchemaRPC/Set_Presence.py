from pypresence import Presence
import time as tm
import pickle
import os.path
from School_From_Home import *
from Get_Name import *
import datetime
import dateutil.parser
from Get_Image_Names import *
with open('Klass.txt','r+') as klass:
    room=klass.read()
client_id = 'yourDiscordApplicationID'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
(temp,lef)=get_name(room)
(limg,simg)=ImageNames(temp,AtHome())
if(isinstance(lef,int) or isinstance(lef,float)):
    RPC.update(details="At Home" if AtHome() else "At School", state=(f"class:\n{temp}"),end=(lef),large_image=limg,large_text=f"Class:{temp}",small_image=simg,small_text=f"At {simg.capitalize()}")
else:
    RPC.update(details="At Home" if AtHome() else "At School", state=(temp),large_image=limg,large_text=temp,small_image=simg,small_text=f"At {simg.capitalize()}")
while True:  # The presence will stay on as long as the program is running
    tm.sleep(15) # Can only update rich presence every 15 seconds
    (temp1,lef1)=get_name(room)
    if(temp1==('break' and not temp) and not (isinstance(lef1,int) or isinstance(lef1,float)) and lef1=='dont'):
        (temp,lef)=get_name(room)
        (limg,simg)=ImageNames(temp,AtHome())
        RPC.update(details="At Home" if AtHome() else "At School", state=(temp),large_image=limg,large_text=temp,small_image=simg,small_text=f"At {simg.capitalize()}")
    elif(temp!=temp1 and (isinstance(lef1,int) or isinstance(lef1,float))):
        (temp,lef)=get_name(room)
        (limg,simg)=ImageNames(temp,AtHome())
        print(temp)
        RPC.update(details="At Home" if AtHome() else "At School", state=(f"class:\n{temp}"),end=(lef),large_image=limg,large_text=f"Class:{temp}",small_image=simg,small_text=f"At {simg.capitalize()}")
        
