import usocket as socket
s = socket.socket()
ai = socket.getaddrinfo("192.168.0.50", 8001)
print("Address infos:", ai)
addr = ai[0][-1]
print("Connect address:", addr)
s.connect(addr)
s.send(b'korte')
s.close()

#2. tobbszori kereskor:
s = socket.socket()
s.connect(addr)
s.send(b'alma')
s.close()