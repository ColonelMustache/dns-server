google = {
    'www': '173.194.32.240'
}
com = {
    'google': google
}
root = {
    'com': com
}
print root['com']['google']['www']
print 'hello'

# host_name = [root, 'com', 'google', 'www'] | host_name[index][host_name[index+1]]
def get_ip(host_name):  # TODO fix this
    ip = ''
    for i, zone in range(len(host_name)), host_name:
        print host_name[i]
        ip = host_name[i][host_name[i+1]]
    print ip
    return ip


get_ip([root, 'com', 'google', 'www'])
