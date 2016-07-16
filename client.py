#!/usr/bin/python3

import socket  
import time  
import struct  
import os  

host = input("please enter the target ip addr:")
port = 2345
upload_path = "upload//"

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
sock.settimeout(3)  
e=0  
try:  
    sock.connect((host,port))  
    print ('connected!target ip:'+host)
except socket.timeout as e:  
    print ('timeout',e)  
except socket.error as e:  
    print ('error',e) 
except e:  
    print ('any',e)
if not e:  
    while 1:  
        filename_origin = input("please enter the filename:")
        filename = upload_path + filename_origin    
        FILEINFO_SIZE = struct.calcsize('128sI')  
        fhead = struct.pack('128sI',filename_origin.encode('utf-8'),os.stat(filename).st_size)
        sock.send(fhead) 
        fp = open(filename,'rb')  
        while 1:        
            filedata = fp.read()  
            if not filedata:  
                break  
            sock.send(filedata)  
        print ("sending over...") 
        break
        fp.close()  


