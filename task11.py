from enum import Enum
from struct import unpack_from, calcsize


class Types(Enum):
    float = "f"
    double = "d"
    uint8 = "B"
    uint16 = "H"
    uint32 = "I"
    uint64 = "Q"
    int8 = "b"
    int16 = "h"
    int32 = "i"
    int64 = "q"
    char = "c"


class BinaryReader():
    def __init__(self, offset, buffer):
        self.offset = offset
        self.buffer = buffer

    def read(self, _pattern):
        pattern = _pattern.value
        result = unpack_from(pattern, self.buffer, self.offset)
        self.offset += calcsize(pattern)
        return result[0]

    def readWithSize(self, _pattern, size):
        res = []
        for i in range(0, size):
            pattern = _pattern.value
            result = unpack_from(pattern, self.buffer, self.offset)
            self.offset += calcsize(pattern)
            res.append(result[0])
        return res

    def copy(self, offset):
        return BinaryReader(offset, self.buffer)


def readB(reader, buffer):
    size1 = reader.read(Types.uint16)
    adress1 = reader.read(Types.uint16)
    b1 = []
    ar = BinaryReader(offset=adress1, buffer=buffer)
    for i in range(0, size1):
        b1.append(readC(BinaryReader(offset=ar
                                     .read(Types.uint16), buffer=buffer)))
    b2 = readD(reader.copy(offset=reader.read(Types.uint32)))
    b3 = reader.read(Types.int8)
    return dict(B1=b1, B2=b2, B3=b3)


def readC(reader):
    c1 = reader.read(Types.float)
    c2 = reader.read(Types.int32)
    return dict(C1=c1, C2=c2)


def readD(reader):
    d1 = reader.read(Types.double)
    d2 = reader.read(Types.uint32)
    d3 = reader.read(Types.int32)
    d4 = reader.readWithSize(Types.int64, 4)
    d5 = reader.readWithSize(Types.int8, 4)
    d6 = reader.read(Types.uint8)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6)


def readE(reader, buffer):
    size1 = reader.read(Types.uint32)
    adress1 = reader.read(Types.uint32)
    e1 = []
    forEReader = BinaryReader(offset=adress1, buffer=buffer)
    for i in range(0, size1):
        e1.append(forEReader.read(Types.uint16))
    e2 = reader.read(Types.int64)
    e3 = reader.read(Types.uint8)
    e4 = reader.read(Types.int8)
    e5 = reader.read(Types.float)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5)


def main(buffer):
    reader = BinaryReader(offset=4, buffer=buffer)
    a1 = reader.read(Types.uint16)
    a2 = reader.read(Types.double)
    size3 = 7
    tempA3 = reader.readWithSize(Types.char, size3)
    a3 = b''.join(tempA3).decode("ASCII")
    a4 = readB(reader=reader.copy(offset=reader
                                  .read(Types.uint16)), buffer=buffer)
    a5 = readE(reader=reader, buffer=buffer)
    a6 = reader.read(Types.int64)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)

if __name__ == '__main__':
    print(main(b"EYU\x1a\\@\x80\x8f\x10\x03\x1c\xe7\xac\xbfrmumnpg~\x00\x02\x00\x00\x00\x87\x00\x00\x00\x90z\xaa\xcd\xd6\xc4\x17\x1a\x14+\x92\xf0\x1d?~\xc0\xab\xde\xac\xba\x96O9\x1dh=\xc2G\xd888\n>\xbf\xca\\\xc4\xfe5\x00=\x00 1\xa4 \x98\x96\xb0?\xed\x1a\xe0\x8f\xfcw\\\xd8\x00\x16f\xd8\xc5\xc5\xa0e\xdc\r\x82q^\xe22#L\x80\x94\xff\x1a\x1e\x19l\xb9Z\xc8t0\xa8'6H\x83\x1c\x10m\x02\x00E\x00I\x00\x00\x00\xd1\xc9\x08j\xd1"))
    #https://github.com/Tidinari/python-student-help/wiki/%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0-11.-%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F.#35-%D0%9F%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8E-%D0%B2-%D0%901-%D0%BD%D0%B0%D1%85%D0%BE%D0%B4%D0%B8%D1%82%D1%81%D1%8F-%D0%A0%D0%B0%D0%B7%D0%BC%D0%B5%D1%80-uint32-%D0%B8-%D0%B0%D0%B4%D1%80%D0%B5%D1%81-uint32-%D0%BC%D0%B0%D1%81%D1%81%D0%B8%D0%B2%D0%B0-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%BE%D0%B2-uint32-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80-b