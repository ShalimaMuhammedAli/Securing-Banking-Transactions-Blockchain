import socket

def send_block(ip, port,flag, data):
    UDP_IP = ip#"127.0.0.1"
    UDP_PORT = port#5005
    MESSAGE = f"block:{flag},data:{data}".encode('ASCII')#b"Hello, World!"
    
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

import time

send_block('localhost', 5005, 'new', 'second')
time.sleep(1)
send_block('localhost', 5005, 'old', 'second')
time.sleep(1)
send_block('localhost', 5005, 'old', 'Third')
time.sleep(1)
send_block('localhost', 5005, 'old', 'Fourth')
