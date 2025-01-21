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

from io import BufferedReader, BytesIO
from typing import Union, Any
from time import time

from .bindings import LDAPMessage as bLDAPMessage


class Lightweight_Directory_Access_Protocol_V3:
    class LDAPMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            """Encodes a value of type ``Lightweight_Directory_Access_Protocol_V3.LDAPMessage`.

            Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

            Accepts the input value as  LDAPMessage.

            Returns the encoded values as ``bytearray``.
            """
            if 1739983016 < time():
                raise Exception(
                    "Your trial license has expired! Please contact OSS if you wish to continue to use this software."
                )

            value = value.to_native_type()

            encoding_rule = encoding_rule if encoding_rule is not None else "BER"

            if encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER":
                try:
                    from .private.mycodec_der import LDAPMessage
                    from .private.osspy_der import ValueTracker

                    return LDAPMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError(
                        "Could not load 'LDAPMessage' from 'private.mycodec_der' codec file"
                    ) from exc
            else:
                raise ValueError(
                    "Unsupported or invalid {} encoding rule argument!".format(encoding_rule)
                )

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            """Decodes a value of type ``Lightweight_Directory_Access_Protocol_V3.LDAPMessage``.

            Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

            Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

            Returns decoded values as LDAPMessage.

            """
            if 1739983016 < time():
                raise Exception(
                    "Your trial license has expired! Please contact OSS if you wish to continue to use this software."
                )

            encoding_rule = encoding_rule if encoding_rule is not None else "BER"

            if encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER":
                try:
                    from .private.mycodec_der import LDAPMessage
                    from .private.osspy_der import ValueTracker

                    decval = LDAPMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError(
                        "Could not load 'LDAPMessage' from 'private.mycodec_der' codec file"
                    ) from exc
            else:
                raise ValueError(
                    "Unsupported or invalid {} encoding rule argument!".format(encoding_rule)
                )
            return bLDAPMessage.from_native_type(decval)

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            """Validates a value of type ``Lightweight_Directory_Access_Protocol_V3.LDAPMessage``.

            Accepts the input value as LDAPMessage.

            Returns a ``list`` of constraint violations (if any) or an empty list.
            """
            if 1739983016 < time():
                raise Exception(
                    "Your trial license has expired! Please contact OSS if you wish to continue to use this software."
                )

            value = value.to_native_type()

            errors = []

            encoding_rule: str = "BER"
            if encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER":
                try:
                    from .private.mycodec_der import LDAPMessage

                    LDAPMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError(
                        f"Could not load 'LDAPMessage' from 'private.mycodec_der' codec file: {exc}"
                    ) from exc
            else:
                raise ValueError(
                    "Unsupported or invalid {} encoding rule argument!".format(encoding_rule)
                )
