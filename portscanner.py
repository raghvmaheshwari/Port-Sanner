import socket  # used to establish connection
from IPy import IP  # used to convert domain name to ip address

#Function to check if input is domain name or ip address
def check_ip(ip):
    try:
        # IP function return the given IPaddress which means user have given ipadress as input not domain name
        IP(ip)
        return (ip)
    #If user has given domain name it will give value error
    except ValueError:
        return socket.gethostbyname(ip)


# Scan Port function
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        # this is to make portscanner work faster. For higher the time of timeout the greater the accuracy of our portscanneer
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))

        # using str function because value of port is in integer.
        print('!!Port ' + str(port) + ' is OPEN!!')
    except:
        pass

def scan(target):
    #storing the input in another variable after conversion
    converted_ip = check_ip(target)
    print ('\n' + 'Scanning ' + str(target))
    # Loop To check for every port number
    for port in range(75, 85):
        scan_port(converted_ip, port)
        
#input from user:
target = input('[+] Enter The Target/s That You Want To Scan: (Split the multiple targets with ,)')
if ',' in target:
    for ip_add in target.split(','):
        scan(ip_add.strip(' '))
else:
    scan(target)

