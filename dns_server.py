import socket
import dns_server_handling as dsh
# TODO change every time the IPv4 settings so this server will get DNS requests
DNS_SERVER_IP = '0.0.0.0'
DNS_SERVER_PORT = 53
DEFAULT_BUFFER_SIZE = 1024


def dns_handler(data, address):
    print '-gap-'
    print address
    print data
    # print '==='
    header = data[:12]
    request = dsh.DnsQuery(header, data[12:])
    # print request.qname
    # dsh.get_query_url(data[12:])
    """
    id_hex = data[:2].encode('hex')  # ID
    header_hex = data[2:12]  # .encode('hex')  # flags
    domain_name = data[12:].encode('hex')
    print id_hex, header_hex, domain_name
    for char in data:
        print char.encode('hex')
    print
    for char in header:
        print char.encode('hex'),
    """
    print 'sup'
    return request


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
            request = dns_handler(data, address)
            print request.resolved_ip
            server_socket.sendto(request.response, address)
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


