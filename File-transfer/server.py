from posixpath import split
import socket
from time import sleep
import os

PORT = 1240
client = ''
SEPARATOR = "<SEPARATOR>"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(("", PORT))

tcp.listen(1)
con, addr = tcp.accept()

print("{addr} is connected!")

def main():
    msg = con.recv(1024).decode('utf-8')
    bufferSize, file, size = msg.split(SEPARATOR)
    print(bufferSize, file, size)
    try:
        arq = open(file, 'wb')
        while True:
            bytesRecv = con.recv(int(bufferSize))     
            if not bytesRecv:
                break
            arq.write(bytesRecv)
        arq.close()
    except Exception as e:
        print(e)
        pass
    arq = open(file, 'rb')
    print("Tamanho do arquivo: ", os.path.getsize(arq))
    arq.close()
    con.close()

main()