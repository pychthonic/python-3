import socket
import sys


class PortProbe:
    """This is a simple port scanner. It asks the user for an ip
    address, a starting and an ending port. It then sends a lil packet
    to each port, and if it receives an ack, adds the port to a list of
    open ports. When it's finished with the scan, it prints a list of
    the open ports. If it's run with the -v verbose flag, it prints out
    every port that it scans as it goes along, and then again lists
    which ports were found to be open at the end of the scan.
    """
    def __init__(self):
        """Get IP address and port numbers to scan from user. Scan ports
        and put open ones into list open_ports. Print list open_ports.
        """
        self.ip = input("\nEnter an ip address you have permission to scan: ")
        self.start_port = int(input("\nEnter a port to start at, "
                                    "from 1-65534: "))
        self.end_port = int(input("\nStarting at port {} and scan up to "
                                  "what port? ".format(self.start_port)))
        self.open_ports = []
        print("\nScanning...", end="")

        for port in range(self.start_port, self.end_port + 1):
            sys.stdout.flush()
            response = self.probe_port(port)
            if response == 0:
                self.open_ports.append(port)
                print("\nFound open port: ", port, "\n")
            else:
                if len(sys.argv) == 2:
                    if sys.argv[1] == '-v':
                        print(port, end=" ")

        self.open_ports = sorted(self.open_ports)
        self.print_open_ports()

    def probe_port(self, port, result=1):
        """Sends a packet to an individual port and returns the
        response, if there is one.
        """
        try:
            sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_obj.settimeout(2)
            r = sock_obj.connect_ex((self.ip, port))
            if r == 0:
                result = r
            sock_obj.close()
        except Exception:
            pass
        return result

    def print_open_ports(self):
        """Prints the list of open ports."""
        if self.open_ports:
            print("\n\nOpen Ports: ", end="")
            for p in self.open_ports:
                print(p, end=' ')
        else:
            print("\n\nSorry, no open ports found.")
        print("")


if __name__ == '__main__':
    new_scan = PortProbe()
