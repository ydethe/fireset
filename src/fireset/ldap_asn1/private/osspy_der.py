# ************************************************************
#   Copyright (C) 2023 OSS Nokalva, Inc.  All rights reserved.
# ************************************************************

#   THIS FILE IS PROPRIETARY MATERIAL OF OSS NOKALVA, INC.
#   AND MAY BE USED ONLY BY DIRECT LICENSEES OF OSS NOKALVA, INC.
#   THIS COPYRIGHT STATEMENT MAY NOT BE REMOVED.

#   THIS FILE SHOULD BE USED FOR TRIAL/EVALUATION PURPOSES ONLY.
#   YOUR EVALUATION PERIOD ENDS ON '2/19/2025 11:36:56 AM'
#   NO COMMERCIAL USES ARE PERMITTED.

#   Python 3.7 or higher is required!
#   This file was generated for 'Yann de The' by 'https://asn1.io/ASN1-Python-Compiler/' at '1/20/2025 11:36:56 AM'

import io
import struct
from datetime import datetime, timezone
from decimal import Decimal
from sys import byteorder
from typing import Union, Tuple, List, Any
from math import isnan, log10, pow, floor, trunc, ceil


def byte2int(array: list) -> int:
    if len(array) == 0:
        return 0
    return array[0]


class der:
    class decodingstream:
        def __init__(self, source, encoding_rule: str):
            if isinstance(source, io.BufferedReader):
                self.buffer = source
            elif isinstance(source, io.BytesIO):
                self.buffer = io.BufferedReader(source)
            else:
                self.buffer = io.BufferedReader(io.BytesIO(source))

            self._ppos = 0
            self.__enc_rule = encoding_rule.upper()

        @property
        def canonical(self) -> bool:
            return self.__enc_rule == "DER"

        def read(self, size):
            bts = self.buffer.read(size)
            if len(bts) < 0:
                raise ValueError(
                    "70026: The end of the encoding was encountered instead of length octets!"
                )
            self._ppos += size
            return bts

        def read_byte(self):
            bts = self.buffer.read(1)
            if len(bts) != 1:
                raise ValueError(
                    "70026: The end of the encoding was encountered instead of length octets!"
                )
            self._ppos += 1
            return bts

        def peek_bytes(self, size, offset=0):
            peeked = self.buffer.read(size + offset)
            self.buffer.seek(self.buffer.tell() - len(peeked))
            return peeked[offset : offset + size]

        def skip_bytes(self, size):
            bts = self.buffer.read(size)
            if len(bts) != size:
                raise ValueError(
                    "70026: The end of the encoding was encountered instead of length octets!"
                )
            self._ppos += size

        def get_buffer(self) -> bytearray:
            if isinstance(self.buffer, bytearray):
                return self.buffer
            return None

        def get_pos(self):
            return self.buffer.tell()

        def is_eof(self):
            return len(self.buffer.peek(1)) == 0

        def seek(self, pos):
            self.buffer.seek(pos)

        def size(self):
            return self.__sizeof__

    class encodingstream:
        def __init__(self, encoding_rule: str):
            self.buffer = bytearray()
            self.pos = 0
            self.__enc_rule = encoding_rule.upper()

        @property
        def canonical(self) -> bool:
            return self.__enc_rule == "DER"

        def append(self, value):
            self.pos += len(value)
            self.buffer.extend(value)

        def add_length(self, length):
            self.pos = length

        def get_byte(self, offset):
            if len(self.buffer) >= offset:
                return self.buffer[offset]
            return None

        def get_buffer(self) -> bytearray:
            return self.buffer

        def get_pos(self) -> int:
            return self.pos

    @staticmethod
    def sortByTag(stream) -> int:
        decoding_stream = der.decodingstream(stream.buffer)
        _, read_tag = der.peek_tag(decoding_stream, 0, 0)

        return read_tag

    @staticmethod
    def int_bytes_len(num: int, byte_len=8) -> int:
        if num == 0:
            return 1
        return int(ceil(float(num.bit_length()) / byte_len))

    @staticmethod
    def zero_ended_encode(num: int) -> bytes:
        octets = bytearray(der.int_bytes_len(num, 7))
        i = len(octets) - 1
        octets[i] = num & 0x7F
        num >>= 7
        i -= 1
        while num > 0:
            octets[i] = 0x80 | (num & 0x7F)
            num >>= 7
            i -= 1
        return bytes(octets)

    @staticmethod
    def encode_tags(stream: bytearray, tags: Any) -> None:
        if isinstance(tags, list):
            for tag in tags:
                der.encode_tag(stream, tag)
        else:
            tag = tags
            der.encode_tag(stream, tag)

    @staticmethod
    def encode_tag(stream, tag: int) -> None:
        if tag > 255:
            if tag > 65535:
                bts = struct.pack(">Q", tag)[5:]
            else:
                bts = struct.pack(">H", tag)
        else:
            bts = struct.pack(">H", tag)[1:]

        stream.extend(bts)

    @staticmethod
    def encode_tags_lens(stream: bytearray, tags: list, length: int) -> None:
        buftmp = bytearray()
        for tag in reversed(tags):
            bufnew = bytearray()
            der.encode_tags(bufnew, tag)
            bufnew.extend(der.encode_len(length + len(buftmp)))
            bufnew.extend(buftmp)
            buftmp = bufnew

        stream.extend(buftmp)

    @staticmethod
    def encode_tags_lens_ber(
        stream: bytearray,
        tags: list,
        buffer: bytearray,
        form: str = "primitive",
        length: int = None,
    ) -> None:
        buftmp = bytearray()
        length = length if length is not None else len(buffer)
        for idx, tag in enumerate(tags):
            der.encode_tags(buftmp, tag)

            if idx + 1 < len(tags):
                der.encode_tags(buftmp, [0x80])
                if buffer is not None:
                    der.encode_eoc(buffer)
            else:
                if form == "primitive":
                    buftmp.extend(der.encode_len(length))
                else:
                    der.encode_tags(buftmp, [0x80])
                    der.encode_eoc(buffer)

        stream.extend(buftmp)

    @staticmethod
    def encode_eoc(stream: bytearray) -> None:
        stream.append(0x00)
        stream.append(0x00)

    @staticmethod
    def encode_len(length: Any) -> bytearray:
        if length < 0x80:
            return bytearray(struct.pack(">H", length)[1:])
        octets = bytearray(der.int_bytes_len(length) + 1)
        octets[0] = 0x80 | (len(octets) - 1)
        for i in range(len(octets) - 1, 0, -1):
            octets[i] = length & 0xFF
            length >>= 8
        return octets

    @staticmethod
    def encode_integer(stream: encodingstream, value: int, tags: list) -> None:
        buffer = bytearray()
        octets = bytearray()

        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if value == 0:
            octets = bytearray([0])
        elif value < 0:
            value = -value
            value -= 1
            octets = bytearray()
            while value > 0:
                octets.append((value & 0xFF) ^ 0xFF)
                value >>= 8
            if len(octets) == 0 or octets[-1] & 0x80 == 0:
                octets.append(0xFF)
        else:
            octets = bytearray()
            while value > 0:
                octets.append(value & 0xFF)
                value >>= 8
            if octets[-1] & 0x80 > 0:
                octets.append(0x00)
        octets.reverse()

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_real(
        stream: encodingstream, value: Union[float, str, dict, int], tags: list
    ) -> None:
        if (
            not isinstance(value, int)
            and not isinstance(value, float)
            and not isinstance(value, Decimal)
            and not isinstance(value, str)
            and not isinstance(value, dict)
        ):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        buffer = bytearray()
        octets = shared.encode_real(value)

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_asciistring(
        stream: encodingstream, value: Union[str, bytearray], tags: list
    ) -> None:
        octets = None
        buffer = bytearray()
        if not isinstance(value, bytearray):
            if not isinstance(value, str):
                try:
                    value = str(value)
                except Exception as exc:
                    raise TypeError(
                        "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                    ) from exc

            if not isinstance(value, str):
                value = str(value)

            octets = bytearray(value.encode("ascii"))
        else:
            octets = value

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_utf8string(stream: encodingstream, value: str, tags: list) -> None:
        octets = None
        buffer = bytearray()
        if not isinstance(value, bytearray):
            if not isinstance(value, str):
                try:
                    value = str(value)
                except Exception as exc:
                    raise TypeError(
                        "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                    ) from exc

            if not isinstance(value, str):
                value = str(value)

            octets = bytearray(value.encode("utf-8"))
        else:
            octets = value

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_utf16string(stream: encodingstream, value: str, tags: list) -> None:
        octets = None
        buffer = bytearray()
        if not isinstance(value, bytearray):
            if not isinstance(value, str):
                try:
                    value = str(value)
                except Exception as exc:
                    raise TypeError(
                        "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                    ) from exc

            if not isinstance(value, str):
                value = str(value)

            octets = bytearray(value.encode("utf-16-be"))
        else:
            octets = value

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_utf32string(stream: encodingstream, value: str, tags: list) -> None:
        octets = None
        buffer = bytearray()
        if not isinstance(value, bytearray):
            if not isinstance(value, str):
                try:
                    value = str(value)
                except Exception as exc:
                    raise TypeError(
                        "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                    ) from exc

            if not isinstance(value, str):
                value = str(value)

            octets = bytearray(value.encode("utf-32-be"))
        else:
            octets = value

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_boolean(stream: encodingstream, value: bool, tags: list) -> None:
        if not isinstance(value, bool):
            try:
                value = bool(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        buffer = bytearray()
        octets = bytearray()
        if value != 0:
            octets.append(0xFF)
        else:
            octets.append(0x00)

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, 1)
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_null(stream: encodingstream, value: None, tags: list = None) -> None:
        # tag = [5]
        # if tags is not None:
        #     tag = tags

        buffer = bytearray()
        octets = bytearray()

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, 0)
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_unknown_extensions(value: str) -> bytearray:
        try:
            buffer = bytearray.fromhex(value)
            return buffer
        except Exception as exc:
            raise ValueError(
                "63405: The 'unknown encoding' is missing from the open type value!"
            ) from exc

    @staticmethod
    def encode_bit_string(stream: encodingstream, value: Any, tags: list, **kwargs) -> None:
        buffer = bytearray()
        buftmp = bytearray.fromhex(value["value"])

        length = value["length"]
        unused_bits = len(value["value"]) * 4 - length

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(value["value"]) // 2 + 1)
            buffer.append(unused_bits)
        else:
            der.encode_tags_lens_ber(
                buffer, tags, buftmp, "primitive", len(value["value"]) // 2 + 1
            )

            if kwargs.get("has_named_bits"):
                bit_list = shared.bit_array_from_bytes(length, buftmp)
                shared.trim(bit_list)
                length = len(bit_list)

            unused_bits = len(value["value"]) * 4 - length
            buffer.append(unused_bits)

        if value["value"] != "''B":
            buffer.extend(buftmp)

        stream.append(buffer)

    @staticmethod
    def encode_octet_string(stream: encodingstream, value: bytearray, tags: list) -> None:
        buffer = bytearray()

        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(value))
        else:
            der.encode_tags_lens_ber(buffer, tags, value)

        buffer.extend(value)

        stream.append(buffer)

    @staticmethod
    def encode_absolute_oid(stream: encodingstream, value: str, tags: list) -> None:
        if isinstance(value, str):
            value = value.replace(".", " ").split()

        if isinstance(value, list):
            for idx, val in enumerate(value):
                if not isinstance(val, int):
                    try:
                        oid_val = int(val)
                        value[idx] = oid_val
                    except Exception as exc:
                        raise TypeError(
                            "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                        ) from exc
        else:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        octets = shared.encode_absolute_oid(value)

        buffer = bytearray()
        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_relative_oid(stream: encodingstream, value: str, tags: list) -> None:
        if not isinstance(value, str):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        if isinstance(value, str):
            value = value.replace(".", " ").split()

        if isinstance(value, list):
            for idx, val in enumerate(value):
                if not isinstance(val, int):
                    try:
                        oid_val = int(val)
                        value[idx] = oid_val
                    except Exception as exc:
                        raise TypeError(
                            "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                        ) from exc
        else:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        octets = shared.encode_relative_oid(value)

        buffer = bytearray()
        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_oid_iri(stream: encodingstream, value: str, tags: list) -> None:
        if not isinstance(value, str):
            try:
                value = str(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        octets = shared.encode_oid_iri(value)

        buffer = bytearray()
        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_generalized_time(stream: encodingstream, value: Any, tags: list) -> None:
        octets = shared.encode_time(value, False)

        buffer = bytearray()
        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def encode_utc_time(stream: encodingstream, value: Any, tags: list) -> None:
        octets = shared.encode_time(value, True)

        buffer = bytearray()
        if stream.canonical:
            der.encode_tags_lens(buffer, tags, len(octets))
        else:
            der.encode_tags_lens_ber(stream.buffer, tags, octets)

        buffer.extend(octets)
        stream.append(buffer)

    @staticmethod
    def decode_tags(stream: decodingstream, tags: list) -> Tuple[int, int, int]:
        if len(tags) == 0:
            return 1, 0, 0

        correct = 1
        last_len = 0
        num_indefs = 0

        for tag in tags:
            _, read_tag = der.decode_tag_sets(stream, tag)
            _, length = der.decode_len(stream)
            if length < 0:
                num_indefs += 1
            if read_tag != tag:
                correct = 0

        last_len = length

        return correct, last_len, num_indefs

    @staticmethod
    def decode_tag_sets(
        stream: decodingstream, tags: list
    ) -> Union[Tuple[int, list], Tuple[int, int]]:
        if isinstance(tags, list):
            tag_list = []
            sum_idx = 0
            for _ in tags:
                tag_idx, read_tag = der.decode_tag(stream)
                sum_idx += tag_idx
                tag_list.append(read_tag)
            return sum_idx, tag_list

        return der.decode_tag(stream)

    @staticmethod
    def do_read_tag(stream: decodingstream) -> Tuple[int, bool, bool]:
        bts = int.from_bytes(stream.read_byte(), byteorder)

        if bts < 0:
            raise ValueError(
                "70030: The length is larger than the number of bytes remaining before the end of the encoded data!"
            )

        _ = (bts & 0xC0) >> 6
        is_constructed = (bts & 0x20) != 0
        end_of_content_marker = bts == 0

        num = 0

        if (bts & 0x1F) != 0x1F:
            num = bts & 0x1F
        else:
            while True:
                bts = int.from_bytes(stream.read_byte(), byteorder)
                if bts < 0:
                    raise ValueError(
                        "70030: The length is larger than the number of bytes remaining before the end of the encoded data!"
                    )

                num <<= 7
                num |= bts & 0x7F

                if (bts & 0x80) == 0:
                    break

        if end_of_content_marker:
            bts = int.from_bytes(stream.read_byte(), byteorder)

            if bts < 0:
                raise ValueError(
                    "70020: End-of-content octets encountered instead of the next tag of the type to be decoded!"
                )
            elif bts > 0:
                raise ValueError(
                    "70004: The next tag present in the encoding does not match the next tag of the type to be decoded!"
                )

        return (bts, is_constructed, end_of_content_marker)

    @staticmethod
    def decode_first_tag(stream: encodingstream, offset: int = 0):
        first_byte = stream.get_byte(offset)
        offset += 1

        if first_byte < 0:
            raise ValueError(
                "70030: The length is larger than the number of bytes remaining before the end of the encoded data!"
            )

        tag_class = (first_byte & 0xC0) >> 6
        _ = (first_byte & 0x20) != 0
        is_end_of_content_marker = first_byte == 0
        tag_num = 0

        if (first_byte & 0x1F) != 0x1F:
            tag_num = first_byte & 0x1F
        else:
            while True:
                first_byte = stream.get_byte(offset)
                offset += 1

                if first_byte < 0:
                    raise ValueError(
                        "70030: The length is larger than the number of bytes remaining before the end of the encoded data!"
                    )
                tag_num <<= 7
                tag_num |= first_byte & 0x7F

                if (first_byte & 0x80) == 0:
                    break
        if is_end_of_content_marker:
            first_byte = stream.get_byte(
                offset
            )  # we also read the following octet, which must be a 0
            offset += 1

            if first_byte < 0:
                raise ValueError(
                    "70020: End-of-content octets encountered instead of the next tag of the type to be decoded!"
                )
            if first_byte > 0:
                raise ValueError(
                    "70004: The next tag present in the encoding does not match the next tag of the type to be decoded!"
                )

        return (tag_class, tag_num)

    @staticmethod
    def peek_at_tag(stream: decodingstream) -> bool:
        pos = stream.get_pos()
        _, _, end_of_content_marker = der.do_read_tag(stream)

        stream.seek(pos)

        return end_of_content_marker

    @staticmethod
    def is_indefinite(stream: decodingstream, offset: int, is_decoded=False) -> bool:
        if is_decoded:
            return False

        pos = stream.get_pos()
        stream.seek(offset)
        der.do_read_tag(stream)

        length = der.read_len(stream)

        stream.seek(pos)
        return length < 0

    @staticmethod
    def read_len(stream: decodingstream) -> int:
        bts = int.from_bytes(stream.read_byte(), byteorder)
        length = 0

        if bts < 0:
            raise ValueError(
                "70026: The end of the encoding was encountered instead of length octets!"
            )

        if bts <= 0x7F:
            length = bts
        elif bts == 0x80:
            length = -1
        else:
            num_octets_len = bts - 0x80
            ui_len = 0

            for _ in range(0, num_octets_len):
                bts = int.from_bytes(stream.read_byte(), byteorder)

                if bts < 0:
                    raise ValueError(
                        "70027: The end of the encoding was encountered instead of a subsequent length octet!"
                    )

                if (ui_len & 0xFF000000) != 0:
                    raise ValueError(
                        "64701: An unsupported length (over 2147483647 or 0x7FFFFFFF bytes) was detected in the encoded data!"
                    )

                ui_len <<= 8
                ui_len |= bts

            length = ui_len

        return length

    @staticmethod
    def peek_tags(stream: decodingstream, tags: list, offset: int = 0) -> Tuple[int, int, int]:
        if len(tags) == 0:
            return 1, 0, offset

        result = 1
        initial_pos = stream.get_pos()
        for tag in tags:
            try:
                idx, read_tag = der.peek_tag_sets(stream, tag, offset)
                offset += idx
                idxlen, length = der.peek_len(stream, offset)
                offset += idxlen if idxlen >= 0 else 1

                if read_tag != tag:
                    result = 0
                    break
            except Exception as _exc:  # pylint: disable=broad-except
                stream.seek(initial_pos)
                return 0, 0, 0

        return result, length, offset

    @staticmethod
    def peek_tag_sets(
        stream: decodingstream, tags: list, offset: int
    ) -> Union[Tuple[int, list], Tuple[int, int]]:
        if isinstance(tags, list):
            tag_list = []
            idx = 0
            for _ in tags:
                updated_idx, read_tag = der.peek_tag(stream, offset)
                offset += updated_idx
                idx += updated_idx
                tag_list.append(read_tag)
            return idx, tag_list
        else:
            return der.peek_tag(stream, offset)

    @staticmethod
    def peek_discriminating_tags(
        stream: decodingstream, tagsets: list, offset: int = 0
    ) -> Tuple[int, int, int]:
        correct = 0
        length = 0
        offset = 0

        if len(tagsets) == 0:
            return 1, 0, 0

        for tagset in tagsets:
            tags = tagset
            if isinstance(tagset, list) and isinstance(tagset[0], list):
                tags = tagset[0]

            idx, found_tags = der.peek_tag_sets(stream, tags, offset)

            if found_tags == tags:
                correct = 1
                length = len(found_tags)
                offset = idx

        return correct, length, offset

    @staticmethod
    def peek_tags_sets(stream: decodingstream, tagssets: list) -> int:
        correct = 0
        for tagset in tagssets:
            correct = correct | der.peek_tags(stream, tagset)

        return correct

    @staticmethod
    def decode_constructed_string(
        stream: decodingstream, buffer: bytearray, is_bitString: bool, unused_bits: list
    ) -> None:
        length = der.read_len(stream)

        loc_end = stream.get_pos() + length if length >= 0 else 0

        while True:
            if loc_end != 0:
                if stream.get_pos() >= loc_end:
                    break
            else:
                end_of_content_marker = der.peek_at_tag(stream)
                if end_of_content_marker:
                    der.skip_eoc(stream)
                    break

            der.decode_string_tlv(stream, buffer, is_bitString, unused_bits)

    @staticmethod
    def decode_primitive_string(
        stream: decodingstream, buffer: bytearray, is_bitString: bool, unused_bits: list
    ) -> None:
        length = der.read_len(stream)

        if length < 0:
            raise ValueError(
                "70007: The primitive-encoding tag of a nested string fragment is followed by indefinite-length octets!"
            )

        if is_bitString:
            if unused_bits[0] != 0:
                raise ValueError(
                    "70015: A nested bit string fragment starts with an invalid octet (a number greater than 7)!"
                )
            if length >= 1:
                unused_bits[0] = int.from_bytes(stream.read_byte(), byteorder)
                length -= 1

                if unused_bits[0] > 7:
                    unused_bits[0] = 0
            else:
                unused_bits[0] = 0

        bts = stream.read(length)
        buffer.extend(bytearray(bts))

    @staticmethod
    def decode_string_tlv(
        stream: decodingstream, buffer: bytearray, is_bit_string: bool, unused_bits: list
    ) -> None:
        _, is_constructed, end_of_content_marker = der.do_read_tag(stream)

        if end_of_content_marker:
            raise ValueError(
                "70023: End-of-content octets encountered instead of the tag of a nested string fragment!"
            )

        if not is_constructed:
            der.decode_primitive_string(stream, buffer, is_bit_string, unused_bits)
        else:
            der.decode_constructed_string(stream, buffer, is_bit_string, unused_bits)

    @staticmethod
    def skip_eoc(stream: decodingstream, times=None) -> None:
        if not stream.is_eof() and times is not None:
            for _ in range(times):
                if not stream.is_eof() and der.is_eoc(stream):
                    stream.skip_bytes(2)
        elif not stream.is_eof() and der.is_eoc(stream):
            stream.skip_bytes(2)

    @staticmethod
    def is_eoc(stream: decodingstream, length: int = -1) -> bool:
        if length >= 0:
            return False

        if stream.is_eof():
            return True

        pos = stream.get_pos()
        bts = byte2int(stream.read_byte())

        if bts == 0x00:
            bts = byte2int(stream.read_byte())

            if bts == 0x00:
                stream.seek(pos)
                return True

        stream.seek(pos)
        return False

    @staticmethod
    def decode_tag(stream: decodingstream) -> Tuple[int, int]:
        first_octet = byte2int(stream.read_byte())
        cls = first_octet & 0xC0
        form = first_octet & 0x20
        first_octet = first_octet & 0x1F
        if first_octet < 31:
            return 1, first_octet | cls | form

        val = first_octet | cls | form
        return 1, val

    @staticmethod
    def peek_tag(
        stream: decodingstream, offset: int = 0, includeClassForm: int = 1
    ) -> Tuple[int, int]:
        _offset = offset
        byte = stream.peek_bytes(1, _offset)
        if len(byte) == 0:
            return 0, 0

        first_octet = byte2int(byte)
        cls = first_octet & 0xC0
        form = first_octet & 0x20
        first_octet = first_octet & 0x1F
        if first_octet < 31:
            if includeClassForm == 1:
                return 1, first_octet | cls | form
            else:
                return 1, first_octet | cls

        val = first_octet | cls
        if includeClassForm == 1:
            val = val | form
        _offset += 1

        return 1, val

    @staticmethod
    def decode_len(stream: decodingstream) -> Tuple[int, int]:
        idx = 0
        byte = stream.read_byte()
        first_octet = byte2int(byte)
        if first_octet == 0x80:
            return first_octet, -1
        if first_octet & 0x80 == 0:
            return 1, first_octet
        octets_num = first_octet & 0x7F
        idx = idx + 1
        if octets_num < 0:
            raise ValueError(
                "70025: The end of the encoding was encountered instead of a subsequent tag octet!"
            )
        if byte2int(stream.peek_bytes(1)) == 0:
            raise ValueError("70010: Invalid length octets!")
        ui_len = 0
        for _ in range(octets_num):
            octet = byte2int(stream.read_byte())
            ui_len <<= 8
            ui_len |= octet

        if ui_len > 2147483647:
            raise ValueError("70010: Invalid length octets!")

        return octets_num + 1, ui_len

    @staticmethod
    def peek_len(stream: decodingstream, initial_offset: int = 0) -> Tuple[int, int]:
        offset = initial_offset

        idx = 0
        bts = stream.peek_bytes(1, offset)
        if len(bts) == 0:
            return 0, 0
        first_octet = byte2int(bts)
        offset += 1
        if first_octet == 0x80:
            return 1, -1
        if first_octet & 0x80 == 0:
            return 1, first_octet
        num_octets = first_octet & 0x7F
        idx = idx + 1

        if num_octets == 0:
            return 0, 0

        ui_len = 0
        for _ in range(num_octets):
            bts = stream.peek_bytes(1, offset)
            offset += 1
            octet = byte2int(bts)
            if octet < 0:
                raise ValueError(
                    "70027: The end of the encoding was encountered instead of a subsequent length octet!"
                )
            if (ui_len & 0xFF00_0000) != 0:
                raise ValueError(
                    "64701: An unsupported length (over 2147483647 or 0x7FFFFFFF bytes) was detected in the encoded data!"
                )
            ui_len <<= 8
            ui_len |= octet
        return offset - initial_offset, ui_len

    @staticmethod
    def read_tags(stream: decodingstream) -> int:
        offset = stream.get_pos()
        byte = stream.read_byte()
        first_octet = byte2int(byte)
        counter = 1

        if (first_octet & 0x1F) != 0x1F:
            return counter
        else:
            while True:
                counter = counter + 1
                offset = offset + 1
                byte = stream.read_byte()
                first_octet = byte2int(byte)

                if (first_octet & 0x80) == 0:
                    return counter

    @staticmethod
    def decode_integer(stream: decodingstream, tags: list, _=None) -> int:
        result, length, offset = der.peek_tags(stream, tags)
        if result == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        stream.skip_bytes(offset)

        bts = stream.read(length)
        first_octet = byte2int(bts)

        value = 0
        if first_octet & 0x80 > 0:
            octets = bytearray()
            for octet in bytearray(bts):
                octets.append(octet ^ 0xFF)
            for octet in octets:
                value = (value << 8) | octet
            value += 1
            value = -value
        else:
            for octet in bytearray(bts):
                value = (value << 8) | octet

        return value

    @staticmethod
    def decode_real(stream: decodingstream, tags: list, _) -> Union[Any, dict]:
        correct, length, offset = der.peek_tags(stream, tags)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        if length < 0:
            raise ValueError(
                "70006: A primitive-encoding tag is followed by indefinite-length octets!"
            )

        stream.skip_bytes(offset)

        buffer = stream.read(length)
        return shared.decode_real(buffer)

    @staticmethod
    def decode_null(stream: decodingstream, tags: list = None, _=None) -> None:
        if tags is None:
            tags = [5]

        result, length, _ = der.decode_tags(stream, tags)
        if result == 0 or length != 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

    @staticmethod
    def decode_asciistring(
        stream: decodingstream, tags: list, c_tags: list
    ) -> Union[str, None, bytearray]:
        buffer = bytearray()
        result, length, offset = der.peek_tags(stream, tags)

        if result != 0:
            stream.skip_bytes(offset)
            bts = stream.read(length)
            try:
                return bts.decode("ascii")
            except BaseException:
                return bytearray(bts)
        elif c_tags is not None and len(c_tags) > 0:
            result, length, offset = der.peek_tags(stream, c_tags)

            if result != 0:
                unused_bits = [0]
                der.do_read_tag(stream)
                der.decode_constructed_string(stream, buffer, False, unused_bits)
                try:
                    return bytes(buffer).decode("ascii")
                except BaseException:
                    return buffer

        raise ValueError(
            "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
        )

    @staticmethod
    def decode_utf8string(
        stream: decodingstream, tags: list, c_tags: list = None
    ) -> Union[str, None, bytearray]:
        buffer = bytearray()
        result, length, offset = der.peek_tags(stream, tags)

        if result != 0:
            stream.skip_bytes(offset)
            bts = stream.read(length)
            try:
                return bts.decode("utf-8")
            except BaseException:
                return bytearray(bts)
        elif c_tags is not None and len(c_tags) > 0:
            result, length, offset = der.peek_tags(stream, c_tags)

            if result != 0:
                unused_bits = [0]
                der.do_read_tag(stream)
                der.decode_constructed_string(stream, buffer, False, unused_bits)
                try:
                    return bytes(buffer).decode("utf-8")
                except BaseException:
                    return buffer

        raise ValueError(
            "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
        )

    @staticmethod
    def decode_utf16string(
        stream: decodingstream, tags: list, c_tags: list
    ) -> Union[str, None, bytearray]:
        buffer = bytearray()
        result, length, offset = der.peek_tags(stream, tags)

        if result != 0:
            stream.skip_bytes(offset)
            bts = stream.read(length)
            try:
                return bts.decode("utf-16-be")
            except BaseException:
                return bytearray(bts)
        elif c_tags is not None and len(c_tags) > 0:
            result, length, offset = der.peek_tags(stream, c_tags)

            if result != 0:
                unused_bits = [0]
                der.do_read_tag(stream)
                der.decode_constructed_string(stream, buffer, False, unused_bits)
                try:
                    return bytes(buffer).decode("utf-16-be")
                except BaseException:
                    return buffer

        raise ValueError(
            "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
        )

    @staticmethod
    def decode_utf32string(
        stream: decodingstream, tags: list, c_tags: list = None
    ) -> Union[str, None, bytearray]:
        buffer = bytearray()
        result, length, offset = der.peek_tags(stream, tags)

        if result != 0:
            stream.skip_bytes(offset)
            bts = stream.read(length)
            try:
                return bts.decode("utf-32-be")
            except BaseException:
                return bytearray(bts)
        elif c_tags is not None and len(c_tags) > 0:
            result, length, offset = der.peek_tags(stream, c_tags)

            if result != 0:
                unused_bits = [0]
                der.do_read_tag(stream)
                der.decode_constructed_string(stream, buffer, False, unused_bits)
                try:
                    return bytes(buffer).decode("utf-32-be")
                except BaseException:
                    return buffer

        raise ValueError(
            "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
        )

    @staticmethod
    def decode_boolean(stream: decodingstream, tags: list, _: list = None) -> bool:
        result, _, offset = der.peek_tags(stream, tags)
        if result == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        dec_val = byte2int(stream.peek_bytes(1, offset))
        stream.skip_bytes(offset + 1)
        return bool(dec_val)

    @staticmethod
    def decode_octet_string(stream: decodingstream, tags: list, c_tags: list = None) -> bytearray:
        buffer = bytearray()
        result, length, offset = der.peek_tags(stream, tags)

        if result != 0:
            stream.skip_bytes(offset)

            bts = stream.read(length)
            return bytearray(bts).hex().upper()
        elif c_tags is not None and len(c_tags) > 0:
            result, length, offset = der.peek_tags(stream, c_tags)

            if result != 0:
                unused_bits = [0]
                der.do_read_tag(stream)
                der.decode_constructed_string(stream, buffer, False, unused_bits)

                return bytearray(buffer).hex().upper()

        raise ValueError(
            "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
        )

    @staticmethod
    def decode_bit_string(stream: decodingstream, tags: list, c_tags: list, **kwargs) -> dict:
        buffer = bytearray()
        result, length, offset = der.peek_tags(stream, tags)

        if result != 0:
            stream.skip_bytes(offset)

            buffer.extend(bytearray(stream.read(length)))
        elif c_tags is not None and len(c_tags) > 0:
            result, length, offset = der.peek_tags(stream, c_tags)

            if result != 0:
                unused_bits = [0]
                der.do_read_tag(stream)
                der.decode_constructed_string(stream, buffer, True, unused_bits)

                buffer.insert(0, unused_bits[0])
            else:
                raise ValueError(
                    "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
                )

        length = (len(buffer) - 1) * 8 - buffer[0]
        tmp_buffer = buffer[1:]
        bit_list = shared.bit_array_from_bytes(length, tmp_buffer)
        if kwargs.get("has_named_bits"):
            shared.trim(bit_list)

        tmp_buffer = shared.bit_array_to_bytes(bit_list)

        tmpVal = ""
        for b in tmp_buffer:
            tmpVal += "%02X" % b

        retVal = {}
        retVal["length"] = length
        retVal["value"] = tmpVal

        return retVal

    @staticmethod
    def decode_absolute_oid(stream: decodingstream, tags: list, _: list = None) -> str:
        result, length, offset = der.peek_tags(stream, tags)
        if result == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        stream.skip_bytes(offset)
        buffer = stream.read(length)

        oid_list = shared.decode_absolute_oid(buffer)
        return ".".join([str(oid) for oid in oid_list])

    @staticmethod
    def decode_relative_oid(stream: decodingstream, tags: list, _: list = None) -> str:
        result, length, offset = der.peek_tags(stream, tags)
        if result == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        stream.skip_bytes(offset)
        buffer = stream.read(length)

        oid_list = shared.decode_relative_oid(buffer)
        return ".".join([str(oid) for oid in oid_list])

    @staticmethod
    def decode_oid_iri(stream: decodingstream, tags: list, _: list = None) -> str:
        result, length, offset = der.peek_tags(stream, tags)
        if result == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        stream.skip_bytes(offset)
        buffer = stream.read(length)

        return shared.decode_oid_iri(buffer)

    @staticmethod
    def decode_enum(stream: decodingstream, tags: list, _: list = None) -> str:
        value = der.decode_integer(stream, tags)
        return str(value)

    @staticmethod
    def decode_generalized_time(stream: decodingstream, tags: list, _: list = None) -> str:
        result, length, offset = der.peek_tags(stream, tags)
        if result == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        stream.skip_bytes(offset)
        buffer = stream.read(length)

        return shared.decode_time(buffer, False)

    @staticmethod
    def decode_utc_time(stream: decodingstream, tags: list, _: list = None) -> str:
        result, length, offset = der.peek_tags(stream, tags)
        if result == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        stream.skip_bytes(offset)
        buffer = stream.read(length)

        return shared.decode_time(buffer, True)

    @staticmethod
    def decode_undecoded_type(stream: decodingstream) -> bytearray:
        offset = stream.get_pos()
        num_tags = der.read_tags(stream)

        idxlen, length = der.peek_len(stream, 0)
        bts = bytearray()

        if idxlen == 0 and length == 0:
            stream.seek(offset)
            while not stream.is_eof():
                bts.extend(stream.read_byte())
        elif length == -1:
            stream.seek(offset)
            bts.extend(stream.read(num_tags + 1))
            while not der.is_eoc(stream):
                try:
                    bts.extend(der.decode_undecoded_type(stream))
                except Exception as _exc:  # pylint: disable=broad-except
                    while not der.is_eoc(stream):
                        bts.extend(stream.read_byte())
            bts.extend(stream.read(2))

            return bts
        else:
            stream.seek(offset)
            bts = stream.read(length + idxlen + num_tags)

        return bts

    @staticmethod
    def decode_unknown_extensions(stream: decodingstream, length: int) -> bytes:
        if length >= 0:
            return bytes(stream.read(length)).hex().upper()

        der.do_read_tag(stream)
        _, length = der.decode_len(stream)

        if length >= 0:
            return bytes(stream.read(length)).hex().upper()

        return der.decode_unknown_extensions(stream, length)


class shared:
    @staticmethod
    def decode_absolute_oid(byte_array: bytearray) -> list:
        oids = []
        length = len(byte_array)
        num = 0

        if length < 1:
            raise ValueError("61903: The encoding of the object identifier value is empty!")

        for idx in range(0, length):
            curr_byte = byte_array[idx]
            num <<= 7
            num |= curr_byte & 0x7F

            if (curr_byte & 0x80) == 0:
                if len(oids) == 0:
                    idx0 = 2 if num >= 80 else int(num / 40)
                    oids.append(idx0)
                    oids.append(num - idx0 * 40)
                else:
                    oids.append(num)
                num = 0

        if num != 0:
            raise ValueError(
                "61904: The encoding of the object identifier value is not well-formed!"
            )

        return oids

    @staticmethod
    def decode_relative_oid(byte_array: bytearray) -> list:
        num_list = []
        length = len(byte_array)

        if length < 1:
            raise ValueError("63603: The encoding of the relative OID value is empty!")

        num = 0

        for idx in range(length):
            by0 = byte_array[idx]
            num <<= 7
            num |= by0 & 0x7F

            if by0 & 0x80 == 0:
                num_list.append(num)
                num = 0

        if num != 0:
            raise ValueError("63604: The encoding of the relative OID value is not well-formed!")

        return num_list

    @staticmethod
    def decode_oid_iri(byte_array: bytearray) -> str:
        return byte_array.decode("utf-8")

    @staticmethod
    def decode_real(byte_array: bytearray) -> Union[str, Decimal, int, dict]:
        length = len(byte_array)

        if length == 0:
            return "0"

        if length == 1:
            if byte_array[0] == 0x40:
                return "INF"
            elif byte_array[0] == 0x41:
                return "-INF"
            elif byte_array[0] == 0x42:
                return "NaN"
            elif byte_array[0] == 0x43:
                return "-0"
            else:
                Decimal(0)

        first_octet = byte_array[0]

        if first_octet & 0x80 != 0:
            is_negative = (first_octet & 0x40) != 0
            scaling = (first_octet & 0x0C) >> 2
            base = (first_octet & 0x30) >> 4
            exponent = first_octet & 0x03
            len_exponent = 0
            loc_exponent = 1

            if exponent <= 2:
                len_exponent = exponent + 1
            else:
                len_exponent = byte_array[1]
                loc_exponent = loc_exponent + 1

            if len_exponent == 0:
                raise ValueError(
                    "63508: The exponent of the real value in the encoded data is empty!"
                )
            if loc_exponent + len_exponent > length:
                raise ValueError(
                    "63509: The exponent of the real value in the encoded data is incomplete!"
                )

            exponent_array = bytearray(len_exponent)
            loc_src = loc_exponent

            for idx in range(len_exponent - 1, -1, -1):
                exponent_array[idx] = byte_array[loc_src]
                loc_src += 1

            exponent = int.from_bytes(exponent_array, byteorder=byteorder, signed=True)

            if base == 1:
                exponent = exponent << 3
            elif base == 2:
                exponent = exponent << 4
            elif base == 3:
                raise ValueError(
                    "63507: The encoding of the real value in the encoded data is not well-formed!"
                )

            loc_mantissa = loc_src
            len_mantissa = length - loc_mantissa
            mantissa = 0

            if len_mantissa != 0:
                needs_leading_zeros = byte_array[loc_mantissa] >= 0x80
                if needs_leading_zeros:
                    loc_mantissa -= 1
                    len_mantissa += 1

                mantissa_array = bytearray(len_mantissa)
                loc_src = loc_mantissa

                for idx in range(len_mantissa - 1, -1, -1):
                    mantissa_array[idx] = byte_array[loc_src]
                    loc_src += 1

                if needs_leading_zeros:
                    mantissa_array[len_mantissa - 1] = 0

                mantissa = (
                    int.from_bytes(mantissa_array, byteorder=byteorder, signed=True) << scaling
                )
                if is_negative:
                    mantissa = -mantissa

            if mantissa == 0:
                return Decimal(0)

            return {"mantissa": mantissa, "base": 2, "exponent": exponent}
        else:
            is_negative = True if byte_array[1] == ord("-") else False
            loc_start = 2 if is_negative else 1

            ascii_real = byte_array[loc_start:].decode("ascii")
            value = Decimal(ascii_real)

            if is_negative:
                value = -value

            if "." not in str(value) and "e" not in str(value):
                return int(value)

            return value

    @staticmethod
    def get_base2_real(dec_val: Decimal, base10_value: int) -> Union[str, dict]:
        is_negative = True if base10_value < 0 else False

        if str(dec_val) == "-0.0":
            return "-0"
        elif str(dec_val) == "0.0":
            return 0
        elif isnan(dec_val):
            return "NaN"
        elif dec_val == Decimal("inf"):
            return "INF"
        elif dec_val == Decimal("-inf"):
            return "-INF"
        else:
            ui_exponent = (base10_value >> 52) & 0x7FF
            ui_mantissa = base10_value & 0xF_FFFF_FFFF_FFFF
            idx_exponent = None

            if ui_exponent == 0:
                idx_exponent = ui_exponent - 1023 - 52 + 1
            else:
                idx_exponent = ui_exponent - 1023 - 52
                ui_mantissa += 0x10_0000_0000_0000

            if ui_mantissa != 0:
                while (ui_mantissa & 0xFFFF) == 0:
                    ui_mantissa >>= 16
                    idx_exponent += 16

                while (ui_mantissa & 0xF) == 0:
                    ui_mantissa >>= 4
                    idx_exponent += 4

                while (ui_mantissa & 1) == 0:
                    ui_mantissa >>= 1
                    idx_exponent += 1

            return {
                "mantissa": -ui_mantissa if is_negative else ui_mantissa,
                "base": 2,
                "exponent": idx_exponent,
            }

    @staticmethod
    def get_real_value(value: Union[str, int, dict]) -> Union[int, Decimal]:
        if isinstance(value, int):
            return Decimal(value)

        if isinstance(value, str):
            if value == "-INF":
                return Decimal("-inf")
            elif value == "INF":
                return Decimal("inf")
            elif value == "NaN":
                return Decimal("nan")
            elif value == "-0":
                return Decimal(-0.0)
            elif value == "0":
                return Decimal(0.0)
            else:
                if "E" in value:
                    mantissa, exponent = value.split("E")
                    value = shared.base2_real_from_base10_real(int(mantissa), int(exponent))

        if isinstance(value, dict) and "base" in value and value["base"] == 2:
            mantissa = value["mantissa"]
            exponent = value["exponent"]

            exponent_max = 1023 - 52
            exponent_min = -1023 - 52 + 1
            cnt_bits = 0
            is_negative = True if mantissa < 0 else False

            num = abs(mantissa)

            if num > 0:
                while num >= 0x80000000:
                    num >>= 32
                    cnt_bits += 32
                while num >= 0x80:
                    num >>= 8
                    cnt_bits += 8
                while num >= 1:
                    num >>= 1
                    cnt_bits += 1
            elif num < 0:
                while num < -0xFFFFFFFF:
                    num >>= 32
                    cnt_bits += 32
                while num < -0xFF:
                    num >>= 8
                    cnt_bits += 8
                while num < 1:
                    num >>= 1
                    cnt_bits += 1

            if cnt_bits < 53:
                mantissa = abs(mantissa) << (53 - cnt_bits)
                exponent = exponent - (53 - cnt_bits)
            elif cnt_bits > 53:
                mantissa = abs(mantissa) >> (cnt_bits - 53)
                exponent = exponent + (cnt_bits - 53)
            else:
                mantissa = abs(mantissa)

            if mantissa < 0x10_0000_0000_0000 or mantissa > 0x1F_FFFF_FFFF_FFFF:
                raise ValueError("Invalid Usage exception!")

            ui_mantissa = mantissa + 2**32 if mantissa < 0 else mantissa

            if exponent > exponent_max:
                raise ValueError("Invalid Usage exception!")

            if exponent < exponent_min:
                raise ValueError("Invalid Usage exception!")

            ui_exponent = exponent - exponent_min + 1
            ui_exponent = ui_exponent + 2**32 if ui_exponent < 0 else ui_exponent
            uid = ui_exponent << 52 | ui_mantissa & 0xF_FFFF_FFFF_FFFF

            if is_negative:
                uid |= 0x8000_0000_0000_0000

            return uid

    @staticmethod
    def base2_real_from_base10_real(base10_mantissa: int, base10_exponent: int) -> dict:
        log_base2 = base10_exponent / log10(2)
        floor_log = floor(log_base2)
        factor = pow(2, log_base2 - floor_log)
        base2_mantissa = base10_mantissa * factor
        base2_exponent = floor_log

        is_negative = True if base2_mantissa < 0 else False

        if is_negative:
            base2_mantissa = -base2_mantissa

        epsilon = 1e-12
        while base2_mantissa >= 2:
            base2_mantissa /= 2
            base2_exponent += 1

        while 2 * base2_mantissa <= 999_999_999_999_999:
            int_part = trunc(base2_mantissa)
            fract_part = base2_mantissa - int_part

            if fract_part < epsilon:
                base2_mantissa = int_part
                break

            if fract_part > 1 - epsilon:
                base2_mantissa = int_part + 1
                break

            base2_mantissa *= 2
            base2_exponent -= 1
            epsilon *= 2

        if is_negative:
            base2_mantissa = -base2_mantissa

        return {"mantissa": base2_mantissa, "base": 2, "exponent": base2_exponent}

    @staticmethod
    def decode_time(byte_array: bytearray, utc_time: bool) -> str:
        return shared.fix_tail(shared.bytes_to_utf8string(byte_array), utc_time)

    @staticmethod
    def fix_tail(time_val: str, utc_time: bool) -> str:
        if "+" in time_val:
            idx = time_val.index("+")
            tail_len = len(time_val) - (idx + 1)
            while tail_len < 4:
                time_val += "0"
                tail_len += 1
        elif "-" in time_val:
            idx = time_val.index("-")
            tail_len = len(time_val) - (idx + 1)
            while tail_len < 4:
                time_val += "0"
                tail_len += 1
        return time_val

    @staticmethod
    def to_bit_list(length: int, byte_array: bytearray) -> list:
        bit_str = "".join([format(num, "08b") for num in byte_array])
        bits = [True if bit == "1" else False for bit in bit_str[0:length]]
        return bits

    @staticmethod
    def encode_absolute_oid(oids: list) -> bytearray:
        num_components = len(oids)
        if num_components < 2:
            raise ValueError("61902: The object identifier value has too few components!")

        num0 = oids[0]
        num1 = oids[1]

        if num0 < 0 or num0 > 2 or num1 < 0 or num0 < 2 and num1 >= 40:
            raise ValueError("61901: The object identifier value contains an invalid component!")

        length = 0
        for idx in range(2, num_components + 1):
            num = num0 * 40 + num1 if idx == 2 else oids[idx - 1]

            if num < 0:
                raise ValueError(
                    "61901: The object identifier value contains an invalid component!"
                )

            length += 1
            num >>= 7

            while num != 0:
                length += 1
                num >>= 7

        byte_array = bytearray(length)
        loc_comp = 0

        for idx in range(2, num_components + 1):
            num = num0 * 40 + num1 if idx == 2 else oids[idx - 1]
            num2 = num
            len_comp = 0

            len_comp += 1
            num2 >>= 7

            while num2 != 0:
                len_comp += 1
                num2 >>= 7

            loc = loc_comp + len_comp - 1
            byte_plus = 0x00
            loc_comp = loc + 1

            byte_array[loc] = num & 0x7F | byte_plus
            num >>= 7
            loc -= 1
            byte_plus = 0x80

            while num != 0:
                byte_array[loc] = num & 0x7F | byte_plus
                num >>= 7
                loc -= 1
                byte_plus = 0x80

        return byte_array

    @staticmethod
    def encode_relative_oid(oids: list) -> bytearray:
        num_oids = len(oids)

        if num_oids < 1:
            raise ValueError("63602: The relative OID value does not have any components!")

        length = 0
        for oid in oids:
            num = oid

            if num < 0:
                raise ValueError("63601: The relative OID value contains an invalid component!")

            length += 1
            num >>= 7

            while num != 0:
                length += 1
                num >>= 7

        byte_array = bytearray(length)
        loc_comp = 0

        for oid in oids:
            num = oid
            num2 = num
            len_comp = 0

            len_comp += 1
            num2 >>= 7

            while num2 != 0:
                len_comp += 1
                num2 >>= 7

            loc = loc_comp + len_comp - 1
            by_more = 0x00
            loc_comp = loc + 1

            byte_array[loc] = num & 0x7F | by_more
            num >>= 7
            loc -= 1
            by_more = 0x80

            while num != 0:
                byte_array[loc] = num & 0x7F | by_more
                num >>= 7
                loc -= 1
                by_more = 0x80

        return byte_array

    @staticmethod
    def encode_oid_iri(value: str) -> bytearray:
        return bytearray(value.encode("utf-8"))

    @staticmethod
    def encode_real(value: Union[str, Decimal, float, int, dict]) -> bytearray:
        if isinstance(value, dict) and "base10Value" in value:
            try:
                value = Decimal(value["base10Value"])
            except BaseException:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                )

        if isinstance(value, float):
            value = Decimal(value)

        if isinstance(value, str):
            if value == "INF":
                return bytearray([0x40])
            elif value == "-INF":
                return bytearray([0x41])
            elif value == "NaN":
                return bytearray([0x42])
            elif value == "-0" or value == "-0.0":
                return bytearray([0x43])
            elif value == "0" or value == "0.0":
                return bytearray()
            else:
                try:
                    decimal_value = Decimal(value)
                    decimal_tuple = decimal_value.as_tuple()
                    exponent = decimal_tuple.exponent
                    mantissa_digits = decimal_tuple.digits
                    mantissa = int("".join(map(str, mantissa_digits)))
                    value = shared.base2_real_from_base10_real(mantissa, exponent)
                except BaseException:
                    raise TypeError(
                        "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                    )

        if isinstance(value, Decimal):
            if value == Decimal("inf"):
                return bytearray([0x40])
            elif value == Decimal("-inf"):
                return bytearray([0x41])
            elif isnan(value):
                return bytearray([0x42])
            elif value == -0.0 and value < 0:
                return bytearray([0x43])
            elif value == Decimal(0.0):
                return bytearray()
            else:
                decimal_tuple = value.as_tuple()
                exponent = decimal_tuple.exponent
                mantissa_digits = decimal_tuple.digits
                mantissa = int("".join(map(str, mantissa_digits)))

                if value < 0 and mantissa > 0:
                    mantissa = -mantissa

                value = {"base": 10, "mantissa": mantissa, "exponent": exponent}

        if isinstance(value, int):
            value = {"base": 10, "mantissa": value, "exponent": 0}

        if isinstance(value, dict):
            if "mantissa" not in value:
                raise ValueError("63502: The mantissa is missing from the real value!")
            if "base" not in value:
                raise ValueError("63503: The base is missing from the real value!")
            if "exponent" not in value:
                raise ValueError("63504: The exponent is missing from the real value!")

            base = int(value["base"])
            mantissa = int(value["mantissa"])
            exponent = int(value["exponent"])

            if base == 2:
                if mantissa != 0:
                    while (mantissa & 1) == 0:
                        mantissa >>= 1
                        exponent += 1

                by0 = 0x80
                if mantissa < 0:
                    by0 |= 0x40
                    mantissa = -mantissa

                num_bytes = (8 + (exponent + (exponent < 0)).bit_length()) // 8
                exponent_arr = bytearray(
                    exponent.to_bytes(num_bytes, byteorder=byteorder, signed=True)
                )
                exponent_arr.reverse()
                len_exponent = len(exponent_arr)
                len_total = 1

                if len_exponent >= 4:
                    by0 |= 0x03
                    len_total += 1
                else:
                    by0 |= len_exponent - 1

                len_total += len_exponent

                num_bytes = (8 + (mantissa + (mantissa < 0)).bit_length()) // 8
                mantissa_arr = bytearray(
                    mantissa.to_bytes(num_bytes, byteorder=byteorder, signed=True)
                )
                mantissa_arr.reverse()
                len_mantissa = len(mantissa_arr)
                has_leading_zeros = True if len_mantissa > 1 and mantissa_arr[0] == 0 else False

                if has_leading_zeros:
                    len_total += len_mantissa - 1
                else:
                    len_total += len_mantissa

                byte_array = bytearray(len_total)
                byte_array[0] = by0

                loc_exponent = 1
                if len_exponent >= 4:
                    if len_exponent > 255:
                        raise ValueError(
                            "63505: The exponent inside the real value is not supported (over 2040 bits)!"
                        )
                    byte_array[1] = len_exponent
                    loc_exponent += 1

                loc_mantissa = loc_exponent + len_exponent

                if has_leading_zeros:
                    loc_mantissa -= 1

                byte_array[loc_mantissa : loc_mantissa + len(mantissa_arr)] = mantissa_arr
                byte_array[loc_exponent : loc_exponent + len(exponent_arr)] = exponent_arr
                return byte_array
            elif base == 10:
                if mantissa != 0:
                    while (mantissa % 10) == 0:
                        mantissa //= 10
                        exponent = exponent + 1
                by0 = 0x03

                mantissa_arr = bytearray(str(mantissa).encode("ascii"))
                exponent_arr = "+0".encode("ascii")
                if exponent != 0:
                    exponent_arr = str(exponent).encode("ascii")

                len_mantissa = len(mantissa_arr)
                len_exponent = len(exponent_arr)
                len_total = 1 + len_mantissa + 1 + 1 + len_exponent

                byte_array = bytearray(len_total)
                byte_array[0] = by0

                byte_array[1 : 1 + len(mantissa_arr)] = mantissa_arr
                byte_array[1 + len_mantissa] = ord(".")
                byte_array[1 + len_mantissa + 1] = ord("E")
                byte_array[
                    1 + len_mantissa + 2 : 1 + len_mantissa + 2 + len(exponent_arr)
                ] = bytearray(exponent_arr)
                return byte_array
            else:
                raise ValueError("63506: The base inside the real value is invalid!")

    @staticmethod
    def encode_time(timevalue: Any, is_utc_time: bool = False) -> bytearray:
        timeobj = None
        strtime = ""

        if isinstance(timevalue, str):
            strtime = timevalue
            if not is_utc_time:
                strtime = shared.remove_trailing_zeroes(timevalue)
        elif isinstance(timevalue, datetime):
            timeobj = timevalue
            timeformat = shared.get_format_from_time_object(timeobj, is_utc_time)
            strtime = timeobj.strftime(timeformat)
            strtime = shared.remove_trailing_zeros(strtime)

            if timeobj.tzinfo == timezone.utc:
                if timeobj.utcoffset().total_seconds() == 0:
                    strtime = strtime + "Z"
        else:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        return shared.bytes_from_utf8string(strtime)

    @staticmethod
    def remove_trailing_zeroes(time_val: str) -> str:
        position = None
        if "-" in time_val:
            position = time_val.find("-")
        elif "+" in time_val:
            position = time_val.find("+")
        if position is not None:
            position = position + 2
            chars = list(time_val)
            rng = len(chars) - 1 - position
            for i in range(len(chars) - 1, position, -1):
                if rng % 2 != 0:
                    chars.pop()
                    rng = rng - 1
                    continue
                if chars[i] == "0":
                    if i > 0 and chars[i - 1] == "0":
                        chars.pop()
                        rng = rng - 1
                else:
                    break
            return "".join(chars)
        return time_val

    @staticmethod
    def bytes_to_utf8string(byte_array: bytearray) -> str:
        return byte_array.decode("utf-8")

    @staticmethod
    def bytes_from_utf8string(value: str) -> bytearray:
        buffer = bytearray()

        if not isinstance(value, str):
            value = str(value)

        buffer.extend(value.encode("utf-8"))
        return buffer

    @staticmethod
    def remove_trailing_zeros(timevalue: str) -> str:
        if "." not in timevalue:
            return timevalue

        start = 0
        stop = len(timevalue) - 1

        if "+" in timevalue:
            stop = timevalue.index("+") - 1
        elif "-" in timevalue:
            stop = timevalue.index("-") - 1

        start = stop

        while timevalue[start] == "0":
            start = start - 1

        if timevalue[start] == ".":
            start = start - 1

        if "+" in timevalue or "-" in timevalue:
            return timevalue[0 : start + 1] + timevalue[stop::]

        return timevalue[0 : start + 1]

    @staticmethod
    def get_format_from_time_object(timeobj: datetime, utctime: bool = False) -> str:
        timeformat = ""

        if timeobj.year is not None:
            if not utctime:
                timeformat += "%Y"
            else:
                timeformat += "%y"
        if timeobj.month is not None:
            timeformat += "%m"
        if timeobj.day is not None:
            timeformat += "%d"
        if timeobj.hour is not None:
            timeformat += "%H"
        if timeobj.minute is not None:
            timeformat += "%M"
        if timeobj.second is not None:
            timeformat += "%S"
        if timeobj.microsecond != 0:
            timeformat += ".%f"
        if timeobj.utcoffset() is not None and timeobj.utcoffset().total_seconds() != 0:
            timeformat += "%z"

        return timeformat

    @staticmethod
    def bit_array_from_bytes(length: int, byte_array: bytearray) -> list:
        if length == 0:
            return []

        bin_list = []
        bin_list = [format(idx, "08b") for idx in byte_array]

        length2 = len(byte_array) * 8
        while length > length2:
            bin_list.append("0")
            length2 += 1

        remainder = length % 8
        bin_list[-1] = bin_list[-1][0 : length % 8] if remainder > 0 else bin_list[-1]
        bit_string = "".join(bin_list)
        bit_array = []
        bit_array = [True if bs == "1" else False for bs in bit_string]
        return bit_array

    @staticmethod
    def bit_array_to_bytes(bit_list: list) -> bytearray:
        byte_array = bytearray()

        while len(bit_list) % 8 != 0:
            bit_list.append(False)

        num_bytes = len(bit_list) // 8

        for idx in range(num_bytes):
            byte_array.append(
                int("".join(["1" if i else "0" for i in bit_list[idx * 8 : idx * 8 + 8]]), 2)
            )

        return byte_array

    @staticmethod
    def trim(bit_array: list) -> None:
        for idx in range(len(bit_array) - 1, -1, -1):
            if bit_array[idx] is False:
                bit_array.pop()
            else:
                break


class ValueTracker(dict):
    def __init__(self):
        self.__deferred_types = {}
        self.__deferred_context = False
        self.__stack = []
        self.__curent_depth = 0

    @property
    def deferred_context(self) -> bool:
        return self.__deferred_context

    @property
    def depth(self) -> int:
        return self.__curent_depth

    @depth.setter
    def depth(self, level: int) -> None:
        while self.__curent_depth > level:
            self.__stack.pop()
            self.__decrement_level()

    def reset_context(self) -> None:
        self.__deferred_context = False

    def add_ancestor(self, value: Any, def_values: Any = None) -> None:
        self.__stack.append(value)

        if def_values is not None:
            for key, _ in def_values.items():
                if key not in value:
                    value[key] = def_values[key]

        self.__increment_level()

    def remove_ancestor(self) -> None:
        self.__stack.pop()
        self.__decrement_level()

    def get_ancestor(self, depth: int) -> Any:
        if depth is None:
            return None
        if self.__deferred_context:
            return self.__stack[self.__curent_depth - 1]
        if self.__curent_depth < depth:
            return None
        level = self.__curent_depth - depth
        return self.__stack[level]

    def get_discriminator(self, indetifier_paths: list) -> Any:
        discriminator = self.__stack[self.__curent_depth - 1]
        for identifier in indetifier_paths:
            if identifier in discriminator:
                discriminator = discriminator[identifier]
            else:
                discriminator = None
                break
        return discriminator

    def add_deferred(self, depth: int, deferred_data: dict) -> None:
        if depth is not None:
            level = self.__curent_depth - depth
            if level >= 0:
                if level not in self.__deferred_types:
                    self.__deferred_types[level] = []
                self.__deferred_types[level].append(deferred_data)

    def are_equivalent(self, value1: list, value2: list) -> bool:
        if value1 == value2:
            return True
        return False

    def are_def_eq(self, value1: Any, value2: Any, component: type) -> bool:
        component = component()
        if (
            isinstance(value1, dict)
            and isinstance(value2, dict)
            and hasattr(component, "_def_vals")
        ):
            if len(value2) > len(value1):
                return False
            for key in value1:
                if key not in value2:
                    if key not in component._def_vals or not self.are_def_eq(
                        value1[key], component._def_vals[key], component._comp_types[key]
                    ):
                        return False
                elif not self.are_def_eq(value1[key], value2[key], component._comp_types[key]):
                    return False
            return True
        else:
            if isinstance(value1, Decimal):
                return str(value1) == str(value2)
            return value1 == value2

    def get_selected_entities(self, entities: Tuple[int, List[str]]) -> list:
        discriminators = []
        for segments in entities:
            (depth, paths) = segments
            discriminator = self.get_ancestor(depth)
            if discriminator is not None:
                for identifier in paths:
                    if identifier in discriminator:
                        discriminator = discriminator[identifier]
                if discriminator is not None:
                    discriminators.append(discriminator)
        return discriminators

    def value_exists(self, dictionary, keys):
        nested_dict = dictionary
        for key in keys:
            try:
                nested_dict = nested_dict[key]
            except KeyError:
                return False
        return True

    def is_empty_buffer(self, buffer: bytearray) -> bool:
        if buffer is None or len(buffer) == 0:
            return True
        elif len(buffer) == 1 and 0x00 in buffer:
            return True
        return False

    def __increment_level(self):
        self.__curent_depth = self.__curent_depth + 1

    def __decrement_level(self):
        self.__curent_depth = self.__curent_depth - 1

    def __has_deferred(self):
        if self.__curent_depth - 1 in self.__deferred_types:
            return True
        return False

    def execute_deferred(self, value: dict) -> Any:
        if self.__has_deferred():
            stored_proc = self.__deferred_types[self.__curent_depth - 1]
            decoded_values = self.__execute_stored_procedures(stored_proc)
            self.__deferred_types.pop(self.__curent_depth - 1)
            if len(decoded_values) > 0:
                value = self.__fill(decoded_values, value)
        self.__deferred_context = False
        self.remove_ancestor()
        return value

    def __execute_stored_procedures(self, stored_proc: list) -> None:
        self.__deferred_context = True
        decoded_values = []
        for data in stored_proc:
            func = getattr(data["type"], "decode")
            encoding_rule = data["encoding_rule"]
            encoding = data["encoding"]
            try:
                self.__deferred_context = True
                deferred_val = func(encoding_rule, encoding, self)
                decoded_values.append(deferred_val)
            except Exception as _exc:  # pylint: disable=broad-except
                return decoded_values
        return decoded_values

    def __fill(self, decoded_values: list, value: Any) -> Any:
        if isinstance(value, dict):
            for key in value:
                if (
                    len(decoded_values) > 0
                    and isinstance(value[key], dict)
                    and "_unknown_encoding" in value[key]
                ):
                    value[key] = decoded_values[0]
                    decoded_values.pop(0)
                value[key] = self.__fill(decoded_values, value[key])
        if isinstance(value, list):
            for idx, item in enumerate(value):
                if (
                    len(decoded_values) > 0
                    and isinstance(item, dict)
                    and "_unknown_encoding" in item
                ):
                    value[idx] = decoded_values[0]
                    decoded_values.pop(0)
                self.__fill(decoded_values, value[idx])
        return value
