import ctypes

# val = ord("A")

# # print(bin(val))

# shift = val <<2

# print(f"{shift:08b}")
# print(f"{63:08b}")
# print(f"{shift & 64:08b}")

# # hex
# # 01 : A
# # 02 : B
# # 15 : U

# A = ord("A")
# print(f"{A=} {A:08b}")
# truncA= A << 2
# print(f"{truncA=} {truncA:08b}")
# six_bit = truncA & 63
# print(f"{six_bit=} {six_bit:08b}")


def encode_6bit(chars="AAAAA"):
    def trunc_ascii(char) -> str:
        return f"{ord(char):08b}"[2:]

    all_bits = "".join((trunc_ascii(char) for char in chars))
    print(f"length: {len(all_bits)}")

    remainder = len(all_bits) % 8
    if remainder:
        all_bits += (8 - remainder) * "0"

    print(f"length: {len(all_bits)}")

    for octet in range(0, len(all_bits), 8):
        bt = all_bits[octet : octet + 8]
        print(f"{bt=} {int(bt,2)}")


# encode_6bit()


def using_ctypes(chars=b"AAAAA"):
    class SixBit(ctypes.BigEndianStructure):
        _pack_ = 1
        _fields_ = [
            ("rest", ctypes.c_uint8, 5),
            ("val1", ctypes.c_uint8, 5),
            ("val2", ctypes.c_uint8, 5),
            # ("val2", ctypes.c_uint8, 6),
            # ("val3", ctypes.c_uint8, 5),
        ]

    def to_bits(self):
        return f"{self.char,}"

    # sbit = SixBit.from_buffer_copy(b"\xf8\xff")

    print(SixBit.rest)
    print(SixBit.val1)
    # print(SixBit.val2)
    # print(SixBit.val3)

    # print(sbit.rest)
    # print(sbit.val1)
    # print(sbit.val2)
    print(ctypes.sizeof(SixBit))


using_ctypes()
