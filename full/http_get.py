#1. kéréskor:
import usocket as socket
s = socket.socket()
ai = socket.getaddrinfo("lovagutca.ddns.net", 80)
print("Address infos:", ai)
addr = ai[0][-1]
print("Connect address:", addr)
s.connect(addr)
s.send(b'GET /mysql_get.php?targonca=targi1&bala=1 HTTP/1.0\r\n\r\n')
print(s.recv(4096))
s.close()

#2. tobbszori kereskor:
s = socket.socket()
s.connect(addr)
s.send(b'GET /mysql_get.php?targonca=targi1&bala=1 HTTP/1.0\r\n\r\n')
s.close()