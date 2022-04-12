import os
from funs import *

######## VNC
if os.system("hostname -I | cut -d \" \" -f 2") is None:
    IPv4Address = os.system("hostname -I")
else:
    IPv4Address = os.system("hostname -I | cut -d \" \" -f 2")

LOCALIP="127.0.0.1"

def vncokdialog(port):
    return "vncserver started on "\
        +"\n"+magneta(str(LOCALIP)+":"+str(port))\
        +"\n"+magneta(str(IPv4Address)+":"+str(port))\
        +"\n"+"To stop it, run:\n"\
        +green("vncserver -kill :"+str(port))\
        +" or "+blue("stopvnc")

def vncrunningdialog(port):
    return "vncserver already started on "\
        +"\n"+magneta(str(LOCALIP)+":"+str(port))\
        +"\n"+magneta(str(IPv4Address)+":"+str(port))\
        +"\n"+"To stop it, run:\n"\
        +green("vncserver -kill :"+str(port))\
        +" or "+blue("stopvnc")
