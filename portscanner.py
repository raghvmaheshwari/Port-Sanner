import socket  # used to establish connection
from IPy import IP  # used to convert domain name to ip address

def scan(target,port_start,port_end):
    #storing the input in another variable after conversion
    converted_ip = check_ip(target)
    print ('\n' + 'Scanning ' + str(target))
    # Loop To check for every port number
    for port in range(port_start,port_end):
        scan_port(converted_ip, port)

#Function to check if input is domain name or ip address
def check_ip(ip):
    try:
        # IP function return the given IPaddress which means user have given ipadress as input not domain name
        IP(ip)
        return (ip)
    #If user has given domain name it will give value error
    except ValueError:
        return socket.gethostbyname(ip)
def get_banner(s):
    return s.recv(1024)

# Scan Port function
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        # this is to make portscanner work faster. For higher the time of timeout the greater the accuracy of our portscanneer
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner =  get_banner(sock)
            # using str function because value of port is in integer.
            print('Open Port ' + str(port) + ':' + str(banner.decode().stripe('\n')))
        except:
            print('Open Port ' + str(port) )
    except:
        #not intrested in which ports are closed so pass
        pass

#input from user:
target = input('[+] Enter The Target/s That You Want To Scan: (Split the multiple targets with ,)')
port_start = int(input('Enter Starting Port Number:'))
port_end = int(input('Enter Ending Port Number:'))
if ',' in target:
    for ip_add in target.split(','):
        scan(ip_add.strip(' '),port_start,port_end)
else:
    scan(target,port_start,port_end)

