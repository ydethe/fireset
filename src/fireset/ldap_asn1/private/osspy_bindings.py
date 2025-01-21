#!/usr/bin/python3
# ************************************************************
# Copyright (C) 2023 OSS Nokalva, Inc.  All rights reserved.
# ************************************************************

# THIS FILE IS PROPRIETARY MATERIAL OF OSS NOKALVA, INC.
# AND MAY BE USED ONLY BY DIRECT LICENSEES OF OSS NOKALVA, INC.
# THIS COPYRIGHT STATEMENT MAY NOT BE REMOVED.

# THIS FILE SHOULD BE USED FOR TRIAL/EVALUATION PURPOSES ONLY.
# YOUR EVALUATION PERIOD ENDS ON '2/19/2025 11:36:56 AM'
# NO COMMERCIAL USES ARE PERMITTED.

# This file was generated for 'Yann de The' by 'https://asn1.io/ASN1-Python-Compiler/' at '1/20/2025 11:36:56 AM'

"""Contains base class definitions of ASN.1 types and other classes used by the bindings.

The classes in this module are not meant to be directly instanciated.

"""

import json
from typing import Optional, Any
from decimal import Decimal
from datetime import datetime
from string import hexdigits

# import simplejson as json

NoneType = type(None)

bindigs = set("01")
hexdigs = set(hexdigits)


class InvalidTypeParameter(TypeError):
    """Raised when a (parameter) value is of the wrong type"""

    def __init__(self, expected) -> None:
        super().__init__()
        self.expected = expected

    def __str__(self) -> str:
        return "Invalid type for value, expected: %s" % ", ".join(
            ["%s" % (t.__qualname__) for t in self.expected]
        )


class ASN1JSONEncoder(json.JSONEncoder):
    """Custom JSON serialization class"""

    def default(self, obj):
        if hasattr(obj, "to_json"):
            return obj.to_json()
        return json.JSONEncoder.default(self, obj)


class OSS_Type:
    """Base class of all ASN.1 types"""

    __slots__ = "_value"

    def __str__(self) -> str:
        return json.dumps(self, cls=ASN1JSONEncoder)

    def to_json(self):
        return self._value

    def to_native_type(self) -> dict:
        return json.loads(self.__str__())


class OSS_Boolean(OSS_Type):
    """Base class for ASN.1 BOOLEAN type values"""

    __slots__ = "_value"

    def __init__(self, value: Optional[bool] = None) -> None:
        if value is None:
            value = False
        self._value = value


class OSS_Integer(OSS_Type):
    """Base class for ASN.1 INTEGER types"""

    __slots__ = "_value"

    def __init__(self, value: Optional[int] = None) -> None:
        if value is None:
            value = 0
        self._value = value


class OSS_Real(OSS_Type):
    """Base class for ASN.1 REAL types"""

    __slots__ = "_value"

    def __init__(self, value: Optional[Any] = None) -> None:
        if value is None:
            value = 0.0
        self._value = value

    def to_json(self):
        if isinstance(self._value, Decimal):
            return {"base10Value": str(self._value)}
        return self._value

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_Real(jsond)


class OSS_GeneralizedTime(OSS_Type):
    """Base class for ASN.1 GeneralizedTime and UTCTime types"""

    __slots__ = "_value"

    def __init__(self, value: Optional[Any] = None) -> None:
        if value is None:
            value = ""
        self._value = value

    def to_json(self):
        if isinstance(self._value, datetime):
            return str(self._value)
        return self._value

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_GeneralizedTime(jsond)


class OSS_UTCTime(OSS_GeneralizedTime):
    """Base class for ASN.1 UTCTime types"""

    __slots__ = "_value"

    def __init__(self, value: Optional[Any] = None) -> None:
        if value is None:
            value = ""
        self._value = value

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_UTCTime(jsond)


class OSS_BitString(OSS_Type):
    """Base class for ASN.1 BIT STRING types"""

    __slots__ = "_value"

    _fields = None
    _csize = None
    _lb = None
    _ub = None
    _containing = None

    def _containing_t():
        return None

    def __init__(self, value: Optional[str] = None) -> None:
        """Instanciates a BIT STRING type object.
        By default, the object will contain an empty string.
        """
        self.__class__._containing = self.__class__._containing_t()
        self._value = self._check_value(value)

    def to_json(self):
        if self._value[0] == "containing":
            return {"containing": self._value[1]}
        else:
            return (
                self._value[1].hex()
                if self._csize
                else {"value": self._value[1].hex(), "length": self._value[0]}
            )

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_BitString(jsond)

    def __getitem__(self, index):
        idx = index
        if self._fields and isinstance(index, str):
            idx = self._fields.get(index)
            if idx is None:
                # raise ValueError("Type has no such named bit: %s" % val)
                raise ValueError("Type has no named bit")
        if idx >= self._value[0]:
            return None
        bidx = idx % 8  # index inside a byte
        byidx = (idx + 1) // 8  # index of byte inside the byte array
        return int(bool((1 << (7 - bidx)) & (self._value[1])[byidx]))

    def __setitem__(self, index, value):
        idx = index
        if self._fields and isinstance(index, str):
            idx = self._fields.get(index)
            if idx is None:
                # raise ValueError("Type has no such named bit: %s" % val)
                raise ValueError("Type has no named bit")
        bidx = idx % 8  # index inside a byte
        extlen = (idx + 1) // 8  # index of byte to mod. inside the byte array
        tmpbval = bytearray(self._value[1])  # get mutable value
        if extlen + 1 > len(self._value[1]):
            # we extend the value if need be
            # if (idx + 1) % 8 != 0:
            #    extlen += 1
            tmpbval.extend(bytes(extlen))
        # we set the bit at bidx to value, regardless of its initial value
        # we zero the bit at bidx, then OR to set the bit to value
        val = int(bool(value))
        tmpbval[extlen] = (tmpbval[extlen] & ~(1 << (7 - bidx))) | (val << (7 - bidx))
        tmplval = idx + 1 if self._value[0] < (idx + 1) else self._value[0]
        self._value = (tmplval, bytes(tmpbval))

    def _check_value(self, value):
        if value is None:
            return (0, bytes(0))
        if isinstance(value, dict):
            try:
                if "containing" in value:
                    # return ('containing', self._containing(value['containing']))
                    return ("containing", value["containing"])
                else:
                    le = value["length"]
                    val = value["value"]
                    if isinstance(le, int) and isinstance(val, str):
                        if set(val).issubset(hexdigs):
                            if len(val) % 2 != 0:
                                val = val + "0"
                            return (le, bytes.fromhex(val))
                        raise ValueError("Hex string contains unallowed characters")
                    raise ValueError("Unexpected dict value: invalid type of value(s)")
            except KeyError:
                raise ValueError("Unexpected dict value: missing key(s)")
        if isinstance(value, str):
            if value.startswith("'"):
                if value.endswith("'H"):
                    value = value[1:-2]
                    if set(value).issubset(hexdigs):
                        if len(value) % 2 != 0:
                            value = value + "0"
                        return (len(value) * 4, bytes.fromhex(value))
                    raise ValueError("Hex string contains unallowed characters")
                if value.endswith("'B"):
                    value = value[1:-2]
                    if set(value).issubset(bindigs):
                        return self._bits2bytes(value)
                    raise ValueError("Binary string contains unallowed characters")
            # we expct a plain string value to have hex digits, similar to ''H
            if set(value).issubset(hexdigs):
                if len(value) % 2 != 0:
                    value = value + "0"
                return (len(value) * 4, bytes.fromhex(value))
            raise ValueError(
                "Invalid string value, expecting either hex, bstrings or hstrings values"
            )
        if isinstance(value, tuple):
            if len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], bytes):
                return value
            # Value is, presumably, a tuple of strings, corresponding to the identifiers from the named bits list
            if not self._fields:
                raise ValueError("Type has no named bits")
            else:
                bitpos = []
                for name in value:
                    bitp = self._fields.get(name)
                    if bitp is None:
                        raise ValueError("Type has no such named bit: %s" % val)
                    bitpos.append(bitp)
                bistr = ""
                if bitpos:
                    lbistr = []
                    for bitp in range(max(bitpos) + 1):
                        lbistr.append("1" if bitp in bitpos else "0")
                    bistr = "".join(lbistr)
                return self._bits2bytes(bistr)
        if isinstance(value, bytes):
            return (len(value) * 8, value)
        raise InvalidTypeParameter((dict, str, bytes, tuple))

    def _bits2bytes(self, value):
        # converts binary strings (str of 0s and 1s) to bytes[]
        bitlen = len(value)
        # extend string with 0s to byte boundary
        value += "0" * ((8 - (bitlen % 8)) % 8)
        bytealen = len(value) // 8
        bytea = bytearray(bytealen)
        for i in range(bytealen):
            bytea[i] = int(value[i * 8 : (i * 8) + 8], 2)
        return (bitlen, bytes(bytea))


class OSS_BinaryString(OSS_Type):
    """(Future) Base class for ASN.1 OCTET STRING and BIT STRING types"""

    __slots__ = "_value"

    _containing = None

    def _containing_t():
        return None

    def __init__(self, value: Optional[str] = None) -> None:
        self._containing = self.__class__._containing_t()


class OSS_OctetString(OSS_Type):
    """Base class for ASN.1 OCTET STRING types"""

    __slots__ = "_value"

    def __init__(self, value: Optional[str] = None) -> None:
        """Instanciates an OCTET STRING type object.
        By default, the object will contain an empty string.
        """
        if value is None:
            value = ""
        self._value = self._check_value(value)

    def to_json(self):
        if isinstance(self._value, str):
            return self._value
        else:
            return {"containing": self._value[1]}

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_OctetString(jsond)

    def _check_value(self, value):
        if isinstance(value, str):
            return value
        if isinstance(value, dict):
            try:
                if "containing" in value:
                    return ("containing", value["containing"])
            except KeyError:
                raise ValueError("Unexpected dict value: missing key(s)")
        raise InvalidTypeParameter(
            (
                dict,
                str,
            )
        )


class OSS_String(OSS_Type):
    """Base class for ASN.1 STRING types"""

    __slots__ = "_value"

    def __init__(self, value: Optional[str] = None) -> None:
        """Instanciates a STRING type object.
        By default, the object will contain an empty string.
        """
        if value is None:
            value = ""
        self._value = value

    def to_json(self):
        return self._value

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_String(jsond)


class OSS_ObjectIdentifier(OSS_Type):
    """Base class for ASN.1 OBJECT IDENTIFIER types"""

    __slots__ = "_value"

    def __init__(self, value: Optional[str] = None) -> None:
        """Instanciates an OBJECT IDENTIFIER type object.
        By default, the object will contain an empty string.
        """
        if value is None:
            value = ""
        self._value = value

    def to_json(self):
        return self._value

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_ObjectIdentifier(jsond)


class OSS_RelativeOid(OSS_ObjectIdentifier):
    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_RelativeOid(jsond)


class OSS_Sequence(OSS_Type):
    """Base class for ASN.1 SEQUENCE types"""

    __slots__ = "_value"

    def _field_map():
        return {}

    def __init__(self) -> None:
        self._fields = self.__class__._field_map()

    def to_json(self):
        return dict(
            sorted(self._value.items(), key=lambda x: (list(self._fields.keys())).index(x[0]))
        )


class OSS_Set(OSS_Sequence):
    """Base class for ASN.1 SET types"""

    __slots__ = "_value"

    def to_json(self):
        return self._value


class OSS_SequenceOf(OSS_Type):
    """Base class for ASN.1 SEQUENCE OF types"""

    __slots__ = "_value"

    def __len__(self):
        return len(self._value)

    def _field_map():
        return {}

    def __init__(self) -> None:
        self._fields = self.__class__._field_map()

    def to_json(self):
        return self._value


class OSS_SetOf(OSS_SequenceOf):
    """Base class for ASN.1 SET OF types"""

    __slots__ = "_value"

    def _field_map():
        return {}

    def __init__(self) -> None:
        self._fields = self.__class__._field_map()


class OSS_Choice(OSS_Type):
    """Base class for ASN.1 CHOICE types"""

    __slots__ = "_value"

    def _field_map():
        return {}

    def __init__(self, val: Optional[Any] = None) -> None:
        """Instanciates a CHOICE type object.
        The object will have the first alternative chosen.
        """
        self._fields = self.__class__._field_map()
        # Choice is stored as a single value dict
        self._value = {}
        # Build implicit value with first choice alternative
        self._value[list(self._fields.keys())[0]] = val

    def to_json(self):
        return self._value


class OSS_Enum(OSS_Type):
    """Base class for ASN.1 ENUMERATED types"""

    __slots__ = "_value"

    def to_json(self):
        return self._value


class OSS_OpenType(OSS_Type):
    __slots__ = ("_value", "_fields")

    def _field_map():
        return {}

    def __init__(self, val: Optional[Any] = None) -> None:
        self._fields = {}
        if hasattr(self.__class__, "_field_map"):
            self._fields = self.__class__._field_map()
        self._value = {}
        if val is not None:
            self.value = val
            # TODO: checks for expected types here

    def to_json(self):
        return list(self._value.values())[0]

    @staticmethod
    def from_native_type(jsond: dict):
        obj = OSS_OpenType()
        obj.value = jsond
        return obj

    @property
    def value(self) -> Any:
        return list(self._value.values())[0]

    @value.setter
    def value(self, val: Optional[Any] = None) -> None:
        self._value.clear()
        if isinstance(val, dict):
            if "_unknown_encoding" in val:
                self._value["unknown_encoding"] = val
                return
        # TODO: checks for expected types here
        self._value["unknown"] = val


class OSS_NullType(OSS_Type):
    """Base class for the ASN.1 NULL type. It's only instance is ``OSS_Null``"""

    __slots__ = "_value"

    def __init__(self, val: Optional[Any] = None) -> None:
        self._value = None

    def to_json(self):
        return self._value

    @staticmethod
    def from_native_type(jsond: dict):
        return OSS_Null


OSS_Null = OSS_NullType()
"""Global object that represents the ASN.1 NULL value """
