def main(input):
    a = (input & 0b00000000000000000000000011111111) << 24
    b = (input & 0b00000000000000000011111100000000) << 10
    c = (input & 0b00000000000000000100000000000000) >> 14
    d = (input & 0b00000000000111111000000000000000) >> 11
    e = (input & 0b00011111111000000000000000000000) >> 11
    f = (input & 0b11100000000000000000000000000000) >> 28
    return a | b | c | d | e | f
