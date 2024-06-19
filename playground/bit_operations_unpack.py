import logging
import struct
import subprocess
import sys
from dataclasses import dataclass
from itertools import chain
from pathlib import Path
from typing import Iterator, Self

_logger = logging.getLogger(__name__)
STR_DS100_1_ALPHABET = (
    "0ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_ !\"#$%&'()*+,-./0123456789:;<=>?"
)


class BitValues:
    """Values from a bytes object based on bit slicing."""

    __slots__ = ["_source", "_length", "_as_int"]

    def __init__(self, source: bytes) -> None:
        r"""Init.

        >>> BitValues(b"\xf0")[2:5]
        6

        Args:
            source: bytes data.
        """
        self._source = source

        self._length = len(source) * 8
        self._as_int = int.from_bytes(source)

    def __getitem__(self, item: int | slice) -> int:
        """Get integer value from a bytes object using bit indexing.

        Provide either a bit index or a slice ([1:5]) notation.

        Args:
            item: Bit index or bit slice notation.
        """
        if isinstance(item, slice):
            return self._int_from_bytes(start=item.start, end=item.stop)
        return self._int_from_bytes(start=item, end=item + 1)

    def _int_from_bytes(self, *, start: int, end: int) -> int:
        offset = self._length - end

        mask = (2 ** (end - start)) - 1
        val = (self._as_int >> offset) & mask
        return val


def chars_from_6bits(bit_array: BitValues, *, start: int, end: int) -> Iterator[str]:
    """Return characters from the DS100-1 alphabet based on a 6 bit slice."""
    slice_start = start

    while slice_start < end:
        val = bit_array[slice_start : slice_start + 6]
        slice_start += 6
        yield STR_DS100_1_ALPHABET[val]


# @dataclass
# class KeyMetadata:
#     raw: bytes
#     short_title: str
#     edition: str
#     register: int
#     segment: int
#     use: int
#     classification: int
#     have_text: bool


#     @classmethod
#     def from_tag_data(cls, tag_data: bytes) -> Self:
#         # NOTE: according to NINE IS 1.0.5.4 Traffic Protection
#         # the DGSK tag should never have text and the short title should be:
#         # UDGSK = DG|HMAC|0000
#         # CDGSK = DB|HMAC|xxxx (where xxxx is the COI, see TP.CRYPT.DGSK.SUITEB.9)
#         # An issued DGSK for Out of Band Key Transfer an outer DS-100-1 tag
#         # is added.
#         cls._crc_check(tag_data)

#         bit_array = BitValues(tag_data)

#         cls._validate_tag_data(bit_array)
#         short_title = "".join(
#             chain(
#                 chars_from_6bits(bit_array, start=0, end=114),
#                 chars_from_6bits(bit_array, start=120, end=150),
#             )
#         )
#         edition = "".join(chars_from_6bits(bit_array, start=150, end=186)).rstrip("0")
#         register = bit_array[188:224]

#         segment = bit_array[224:232]
#         use = bit_array[232:236]
#         classification = bit_array[236:239]

#         return cls(
#             raw=tag_data,
#             short_title=short_title,
#             edition=edition,
#             register=register,
#             segment=segment,
#             use=use,
#             classification=classification,
#             have_text=False,
#         )

#     def __str__(self) -> str:
#         return f"ST={self.short_title} ED={self.edition}"


bts = bytes([12, 77, 85, 76, 84, 80, 80, 75, 67, 104, 97, 105, 110])

chars = list(chars_from_6bits(BitValues(bts), start=0, end=100))

print(chars)
