#!/usr/bin/python3

import socket
import os
import struct
import time
import threading
import fcntl

port = 2345
download_path = "download//"

def get_local_ip(ifname = "eth0"):
    inet = fcntl.ioctl(sock.fileno(),0x8915,struct.pack('256s',ifname[:15]))
    ret = socket.inet_ntoa(inet[20:24])
    return ret

def function(newsock, address):  
    FILEINFO_SIZE = struct.calcsize('128sI')  
   
    while 1:       
        try:  
            fhead = newsock.recv(FILEINFO_SIZE)  
            filename, filesize = struct.unpack('128sI', fhead)  
            print ("address is: ",address)  
            print (filename, len(filename),type(filename))  
            print (filesize)  
            filename = filename.decode('utf-8')
            filename = download_path+filename.strip('\x00')
            fp = open(filename,'wb')
            restsize = filesize  
            print ("recving...")  
            while 1:   
                filedata = newsock.recv(restsize)  
                fp.write(filedata)  
                break  
                if not filedata:  
                    break  
                fp.write(filedata)  
                restsize = testsize - len(filedata)
                if restsize <= 0:  
                    break  
            fp.close()  
            print ("recv succeeded !!File named:",filename)  
        except:  
            print ("he socket partner maybe closed") 
            newsock.close()  
            break

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = get_local_ip()
sock.bind((host,port))
sock.listen(5)
print("server started.\nipv4 : "+host+r"|port: "+str(port))

while True:  
    newsock, address = sock.accept()  
    print ("accept another connection")  
    tmpThread = threading.Thread(target=function,args=(newsock,address))  
    tmpThread.start()
print ('end')
