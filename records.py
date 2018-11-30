co = {
    'il': '104.28.29.70'
}
google = {
    'www': '127.0.0.1',
    'co': co
}
itay = {
    'www': '127.0.0.1'  # '23.221.143.117'
}
com = {
    'google': google,
    'itay': itay
}
root = {
    'com': com
}


# host_name = ['root', 'com', 'google', 'www'] | host_name[index][host_name[index+1]]
def get_ip(host_name):  # TODO fix this
    ip = globals()[host_name[0]]
    for i in range(1, len(host_name)):
        ip = ip[host_name[i]]
    return ip


# get_ip(['root', 'com', 'google', 'www'])
