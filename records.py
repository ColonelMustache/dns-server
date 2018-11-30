co = {
    'il': '104.28.29.70'
}
google = {
    'www': '173.194.32.240',
    'co': co
}
com = {
    'google': google
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
