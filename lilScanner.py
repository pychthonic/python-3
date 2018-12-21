import socket, sys

class port_probe:

    """
    This is a simple port scanner. It asks the user for an ip address,
    a starting and an ending port. It then sends a lil packet to each port, 
    and if it receives an ack, adds the port to a list of open ports. When 
    it's finished with the scan, it prints a list of the open ports.
    If it's run with the -v verbose flag, it prints out every port that 
    it scans as it goes along, and then again lists which ports were 
    found to be open at the end of the scan.

    """

    def __init__ (self):

        self.ip = input("\nEnter an ip address you have permission to scan: ")
        self.start_port = int(input("\nEnter a port to start at, from 1-65534: "))
        self.end_port = int(input("\nStarting at port {} and scan up to what port? ".format(self.start_port)))
        self.open_ports = []
        print("\nScanning... ", end="")
        
        for port in range(self.start_port, self.end_port + 1):
            sys.stdout.flush()
            response = self.probeport(port)
            if response == 0:
                self.open_ports.append(port)
                print("\n\nFound open port: ", port, "\n")
            else:
                if len(sys.argv) == 2:
                    if sys.argv[1] == '-v':
                        print(port, end=" ")
                
        self.open_ports = sorted(self.open_ports)
        self.printOpenPorts()
        
    def probeport(self, port, result = 1):
        try:
            sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockObj.settimeout(2)
            r = sockObj.connect_ex((self.ip, port))
            if r == 0:
                result = r
            sockObj.close()
        except Exception:
            pass
        return result

    def printOpenPorts(self):
        if self.open_ports:
            print("\n\nOpen Ports: ", end="")
            for p in self.open_ports:
                print(p)
        else:
            print("\n\nSorry, no open ports found.")
        print("")


if __name__ == '__main__':
    newScan = port_probe()

