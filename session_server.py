import socket
from queue import Queue
import localsession

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
try:
    global host
    global port
    global s
    host = "localhost"
    port = 9090
    s = socket.socket()
    s.bind((host, port))
    s.listen(50)
except:
    print("Socket creation error: ")

while True:
    try:
        conn, address = s.accept()
        s.setblocking(1)  # prevents timeout
        print("Connection has been established :" + address[0])
        client_msg = conn.recv(20480).decode('utf-8')
        print(client_msg)
        msg = client_msg.split("-")
        if msg[0] == "add":
            print('login success')
            localsession.session[msg[1]] = msg[2]
        else:
            print('logout success')
            localsession.session.pop(msg[1])

        conn.close()
    except Exception as e:
        print(e)