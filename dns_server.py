import socket
# TODO go to http server project and add *if main*
DNS_SERVER_IP = '0.0.0.0'
DNS_SERVER_PORT = 53
DEFAULT_BUFFER_SIZE = 1024


def dns_handler(data, address):
    print '-gap-'
    print address
    print data
    print '==='
    for char in data:
        print char.encode('hex'),
    print


def dns_udp_server(ip, port):
    """
        Starts a UDP server on a given IP:PORT, and calls
        dns_handler(data, client_address)
        prototyped function on any client request data.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ip, port))
    print 'Server started successfully! Waiting for data...'
    while True:
        try:
            data, address = server_socket.recvfrom(DEFAULT_BUFFER_SIZE)
            dns_handler(data, address)
        except Exception, ex:
            print 'Client exception! %s' % (str(ex), )


def main():
    """
        Main execution point of the program
    """
    print "Starting UDP server..."
    dns_udp_server(DNS_SERVER_IP, DNS_SERVER_PORT)


if __name__ == '__main__':
    main()


