import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pars = ('127.0.0.1', 80) 
s.bind(pars)
s.listen(5)

def serveClient(clientsocket, address):
    # we need a loop to continuously receive messages from the client
        # then receive at most 1024 bytes message and store these bytes in a variable named 'data'
        # you can set the buffer size to any value you like
        data = clientsocket.recv(1024)
        # print("from client", data)
        msg = bytes.decode(data)
        request = msg.split(' ')
        method = request[0]
        url = request[1]
        
        if method =="GET":
            if(url == '/get.html'):
                response_header = ("HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\r\n" + "\r\n").encode()
                response_content = b"<html><body><p>good.html</p></body></html>"
                clientsocket.send(response_header + response_content)
                clientsocket.close()
                return
            if(url == '/redirect.html'):
                response_header = ("HTTP/1.1 301 Moved Permanently\r\n" + "Content-Type: text/html\r\n" +"Content-Location:/get.html\r\n" + "Location:/get.html\r\n"+"\r\n").encode()
                # response_content = b"<html><body><h1>301 Moved Permanently</h1><p>Redirected to good.html</p></body></html>"
                clientsocket.send(response_header)
                clientsocket.close()
                return
            if(url == '/notfound.html'):
                response_header = ("HTTP/1.1 404 Not Found\r\n" + "Content-Type: text/html\r\n" + "\r\n").encode()
                response_content = b"<html><body><h1>404 Not Found</h1></body></html>"
                clientsocket.send(response_header + response_content)
                clientsocket.close()
                return
        if method =="HEAD":
            if(url == '/head.html'):
                response_header = ("HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\r\n" + "\r\n").encode()
                clientsocket.send(response_header)
                print(response_header)
                clientsocket.close()
                return
        if method =="POST":
            if(url == '/post.html'):
                response_header = ("HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\r\n" + "\r\n").encode()
                response_content = ("<html><body>" + data.decode()[data.decode().find("id=")+3:] + "</body></html>").encode()
                clientsocket.send(response_header + response_content)
                print(response_header + response_content)
                clientsocket.close()
                return

while True:
    # accept a new client and get it's information
    (clientsocket, address) = s.accept()
    
    # create a new thread to serve this new client
    # after the thread is created, it will start to execute 'target' function with arguments 'args' 
    threading.Thread(target = serveClient, args = (clientsocket, address)).start()
    break