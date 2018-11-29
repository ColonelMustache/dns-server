from records import *

class DnsQuery:
    def __init__(self, header, data):
        relevant_word = header[2:4].encode('hex')
        self.id = get_request_id(header)
        self.qr = get_flag_qr(relevant_word)
        self.opcode = get_opcode(relevant_word)
        self.aa = get_flag_aa(relevant_word)
        self.tc = get_flag_tc(relevant_word)
        self.rd = get_flag_rd(relevant_word)
        self.ra = get_flag_ra(relevant_word)
        self.z = get_z(relevant_word)
        self.rcode = get_rcode(relevant_word)
        self.num_of_queries = get_num_of_queries(header)
        self.num_of_answers = get_num_of_answers(header)
        self.other = get_nscount_and_arcount(header)
        self.qname = [root] + self.get_query_url([x.encode('hex') for x in data]).split()[::-1]
        self.qtype = get_record_type(data)
        self.qclass = get_query_class(data)

    def get_query_url(self, bytes_list):
        # until null (00 byte)
        counter = int(bytes_list[0], 16)
        zone = ''
        if bytes_list[0] == '00':
            return ''
        for i in range(1, counter + 1):
            zone += bytes_list[i].decode('hex')
        # print counter + 1
        # print bytes_list[counter + 1:]
        return zone + " " + self.get_query_url(bytes_list[counter + 1:])

    def create_response(self):
        pass

    def basic_response(self):
        response = ''
        response += self.id
        response += 0b1  # sending response; qr = 1ss


def get_request_id(header):
    # first word
    # print header[:2].encode('hex')
    return header[:2].encode('hex')  # first word


# second word
def get_flag_qr(word):
    # bit 0
    # print relevant_word
    # print int('80', 16)
    result = ((int(word, 16) >> 15) & 0b1)  # mask for left most bit
    return result


def get_opcode(word):
    # bits 1-4
    result = (int(word, 16) >> 11) & 0b01111
    return int(str(result), 2)


def get_flag_aa(word):
    # bit 5
    flag = (int(word, 16) >> 10) & 0b1
    return flag


def get_flag_tc(word):
    # bit 6
    flag = (int(word, 16) >> 9) & 0b1
    return flag


def get_flag_rd(word):
    # bit 7
    flag = (int(word, 16) >> 8) & 0b1
    return flag


def get_flag_ra(word):
    # bit 8
    flag = (int(word, 16) >> 7) & 0b1
    return flag


def get_z(word):
    # bits 9-11, not sure what z is
    flag = (int(word, 16) >> 4) & 0b111
    return flag


def get_rcode(word):
    # bits 12-15
    flag = int(word, 16) & 0b1111
    return flag


def get_num_of_queries(header):
    # third word
    return header[4:6].encode('hex')


def get_num_of_answers(header):
    # fourth word
    return header[6:8].encode('hex')  # first word


def get_nscount_and_arcount(header):
    # fifth and sixth words
    return header[8:].encode('hex')  # first word


def get_record_type(data):
    # one before las word
    index = len(data) - 4
    return data[index: index + 2].encode('hex')


def get_query_class(data):
    # last word
    return data[len(data) - 2:].encode('hex')

