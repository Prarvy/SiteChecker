# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: Site Checker
# Version: 1.0: Base version by author
import sys
import socket

e_msg_1 = """Error: At least One argument is required.
    Usage: 
        python sitechecker.py <site_address> <site_port>
    Example:
        python sitechecker.py www.google.com 80
    Note: site_port defaults to 80 if not specified.
System exiting with Error Code: 1"""
e_msg_2 = 'Error: Port Number is not between 1 and 65535. System exiting with Error Code: 2'
e_msg_3 = 'Error: Connection Timed Out. System exiting with Error Code: 3'
e_msg_4 = 'Error: Connection Failed. System exiting with Error Code: 4'


def site_checker(site, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((site, port))
        request = "HEAD / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(site)
        sock.send(request.encode())
        response = sock.recv(1024).decode()
        print('Success. Address/IP: {} found. Response:'.format(site), response.split('\r\n', 1)[0])
        sock.close()
    except socket.timeout:
        print(e_msg_3)
        sys.exit(3)
    except (socket.error, ConnectionRefusedError):
        print(e_msg_4)
        sys.exit(4)


if __name__ == '__main__':
    if len(sys.argv) in [2, 3]:
        site_address = sys.argv[1]
        if len(sys.argv) == 2:
            print('Info: Port Number has been set to 80.')
            site_port = 80
        else:
            site_port = int(sys.argv[2])
        if site_port not in range(1, 65536):
            print(e_msg_2)
            sys.exit(2)
    else:
        print(e_msg_1)
        sys.exit(1)
    site_checker(site_address, site_port)
