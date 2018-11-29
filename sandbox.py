print hex(213)
print (29 & 0b00010000) >> 3  # 0001000 -> 00100000
print bin(int('80', 16) & 128)
print (int('8100', 16) >> 15) & 0b1

test_hex = '03' + 'www'.encode('hex') + '06' + 'google'.encode('hex') + '03' + 'com'.encode('hex') + '00' + '00010001'
test_hex_list = []
for c in range(0, len(test_hex), 2):
    test_hex_list.append(test_hex[c] + test_hex[c+1])

print test_hex_list

print 'HERE'

"""
def recursive_test_full(bytes_list):
    zones = []

    def recursive_test(byte_list):
        counter = int(byte_list[0], 16)
        zone = ''
        if byte_list[0] == '00':
            return ''
        for i in range(1, counter + 1):
            zone += byte_list[i].decode('hex')
        print counter + 1
        print byte_list[counter + 1:]
        return [zone, " " + recursive_test(byte_list[counter + 1:])]
    return recursive_test(bytes_list)  # [::-1]

zones = recursive_test_full(test_hex_list)
print zones
"""
ls = ['root'] + ['com', 'google', 'www']
print ls