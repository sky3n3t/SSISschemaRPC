import pickle
import os.path
from Get_Event2 import *
from En_Names import *

def get_name(room):
    (name,lef)=GetLesson(room)
    name2=name.split(" ")
    name3=en_name(name2[0])
    #print(name3)
    return(name3,lef)


