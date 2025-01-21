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

import json

from fireset.ldap_asn1.mycodec import Lightweight_Directory_Access_Protocol_V3
from fireset.ldap_asn1.bindings import (
    LDAPMessage,
    MessageID,
    OSS_Integer,
    AttributeDescription,
    OSS_OctetString,
)

# For the sake of keeping the sample short we instantiate the bindings from a dictionary.
# See examples of setters for individual fields below.
valued = json.loads(
    r'{"messageID": 0,"protocolOp":{"bindRequest":{"version": 1,"name": "","authentication":{"simple": ""}}},"controls":[{"controlType": "","controlValue": ""}]}'
)

try:
    print('Obtaining an instance of "LDAPMessage" ... ')
    print()

    value = LDAPMessage.from_native_type(valued)

    print('Pre-validating "Lightweight_Directory_Access_Protocol_V3.LDAPMessage":')

    violations = Lightweight_Directory_Access_Protocol_V3.LDAPMessage.validate(value)

    print("Constraint violations: {}".format(json.dumps(violations, default=str)))
    print()

    # exercise bindings object creation and / or workings of the setter and getters
    value.messageID = MessageID(0)
    if value.protocolOp.has_BindRequest():
        value.protocolOp.bindRequest.version = OSS_Integer(1)
        value.protocolOp.bindRequest.name = AttributeDescription("")
        if value.protocolOp.bindRequest.authentication.has_Simple():
            value.protocolOp.bindRequest.authentication.simple = OSS_OctetString("")

    print('Encoding "Lightweight_Directory_Access_Protocol_V3.LDAPMessage":')

    encoded = Lightweight_Directory_Access_Protocol_V3.LDAPMessage.encode("BER", value)

    print("Encoded HEX: " + ", ".join(["0x{:02X}".format(val) for val in encoded]))
    print()

    print('Decoding "Lightweight_Directory_Access_Protocol_V3.LDAPMessage":')

    decoded = Lightweight_Directory_Access_Protocol_V3.LDAPMessage.decode("BER", encoded)

    print("Decoded value: {}".format(decoded))
    print()

    print('Validating "Lightweight_Directory_Access_Protocol_V3.LDAPMessage":')

    # the 'field reference' property can be used with a tool implementing the JSON Pointer spec
    violations = Lightweight_Directory_Access_Protocol_V3.LDAPMessage.validate(decoded)

    print("Constraint violations: {}".format(json.dumps(violations, default=str)))
    print()

except NotImplementedError as e:
    print("Not Implemented Error : {}".format(format(e)))
