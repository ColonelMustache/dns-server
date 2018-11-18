def get_flags(header):
    relevant_word = header[2:4].encode('hex')
    query_id = get_request_id(header)
    qr_flag = get_flag_qr(relevant_word)
    query_opcode = get_opcode(relevant_word)
    aa_flag = get_flag_aa(relevant_word)
    tc_flas = get_flag_tc(relevant_word)
    rd_flad = get_flag_rd(relevant_word)
    ra_flag = get_flag_ra(relevant_word)
    z_thing = get_z(relevant_word)
    query_rcode = get_rcode(relevant_word)
    num_of_queries = get_num_of_queries(header)
    num_of_answers = get_num_of_answers(header)
    other = get_nscount_and_arcount(header)


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


def get_flag_tc():
    # bit 6
    pass


def get_flag_rd():
    # bit 7
    pass


def get_flag_ra():
    # bit 8
    pass


def get_z():
    # bits 9-11, not sure what z is
    pass


def get_rcode():
    # bits 12-15
    pass


def get_num_of_queries():
    # third word
    pass


def get_num_of_answers():
    # fourth word
    pass


def get_nscount_and_arcount():
    # fifth and sixth words
    pass
