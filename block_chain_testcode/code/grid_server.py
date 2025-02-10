import socket
from Blockchain import *

def start_server(ip, port):
    UDP_IP = ip#"127.0.0.1"
    UDP_PORT = port#5005

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    print('Server Listening', ip, port)
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        #print("received message: %s" % data)
        data = data.decode('ASCII')
        if data.startswith('block'):
            vals = data.split(',')
            bvals = vals[0]
            dvals = vals[1]
            if bvals.endswith('new'):
                print(dvals)
                dataset = dvals.split(':') 
                blockchain = Blockchain(fromFile=False)
                blockchain.add_new_transaction(dataset[1])
                blockchain.mine()
                print(blockchain.get_chain())
                blockchain.save_chain('test_block1.json')
            else:
                dataset = dvals.split(':') 
                blockchain2 = Blockchain(fromFile=True)
                blockchain2.load_chain('test_block1.json')
                blockchain2.add_new_transaction(dataset[1])
                blockchain2.mine()
                blockchain2.save_chain('test_block1.json')

start_server('localhost', 5005)