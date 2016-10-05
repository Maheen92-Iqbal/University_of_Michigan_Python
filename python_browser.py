import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com', 80))
mysocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    
    received = mysocket.recv(512)
    if len(received) < 1:
        
        break
    
    print received
    
mysocket.close()