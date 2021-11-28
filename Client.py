import socket
import requests
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pars = ('127.0.0.1', 80) # server IP and server port
s.connect(pars)

request = 'POST /post.html HTTP/1.1\r\n + "\r\n"'
request += 'id=106209029'
s.send(request.encode())
print(request)

data = s.recv(1024)

print(data)

# while True:
    
#     # let the client talk firt
#     s.send(b'request')

#     # url = "127.0.0.1/head"
#     # response = requests.head(url)
#     # print(response)

#     data = {"id": "106209029"}
#     url = "/post.html"
#     response = requests.post(url, data)
#     print(response)

#     # then wait for server response
#     response = s.recv(1024)
#     if response:
#         print("data from server:", response)

#     # terminate
#     s.send(b'close')
#     break
    
# close directly
s.close()