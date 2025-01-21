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

from warnings import warn
from typing import Union
import private.osspy_der as osspy
from private.ossvalidate import (
    Asn1Type,
    validate_value_type,
    validate_value,
    report_empty_value,
    report_missing_field,
    report_extra_field,
)


class AbsoluteOidType:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = None
        self._asn1Type = Asn1Type.OID

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, list],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = AbsoluteOidType()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: Union[str, list], tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x06]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_absolute_oid(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> Union[str, list]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = AbsoluteOidType()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> Union[str, list]:
        used_tag = [[0x06]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_absolute_oid(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = AbsoluteOidType()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class LDAPMessage:
    def __init__(self):
        self._comp_types = {
            "messageID": MessageID,
            "protocolOp": LDAPMessage__23,
            "controls": LDAPMessage__24,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.LDAPMessage"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = LDAPMessage()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "messageID" in value:
            tmpstream.append(
                MessageID.encode(
                    encoding_rule, value["messageID"], value_tracker, [[0x02]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "protocolOp" in value:
            tmpstream.append(
                LDAPMessage__23.encode(
                    encoding_rule, value["protocolOp"], value_tracker, []
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "controls" in value:
            tmpstream.append(
                LDAPMessage__24.encode(
                    encoding_rule, value["controls"], value_tracker, [[0xA0]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = LDAPMessage()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["messageID"] = MessageID.decode(encoding_rule, stream, value_tracker, [[0x02]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x22], [0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["messageID"] = MessageID.decode(
                encoding_rule, stream, value_tracker, [[0x22], [0x02]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "messageID" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x22]])[0]
        ):
            value["messageID"] = MessageID.decode(encoding_rule, stream, value_tracker, [[0x02]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_discriminating_tags(
            stream,
            [
                [[0x60]],
                [[0x61]],
                [[0x42]],
                [[0x63]],
                [[0x64]],
                [[0x65]],
                [[0x73]],
                [[0x66]],
                [[0x67]],
                [[0x68]],
                [[0x69]],
                [[0x4A]],
                [[0x6B]],
                [[0x6C]],
                [[0x6D]],
                [[0x6E]],
                [[0x6F]],
                [[0x50]],
                [[0x77]],
                [[0x78]],
                [[0x79]],
            ],
        )[
            0
        ]:
            value["protocolOp"] = LDAPMessage__23.decode(encoding_rule, stream, value_tracker, [])
        elif stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            value["protocolOp"] = LDAPMessage__23.decode(encoding_rule, stream, value_tracker, [])
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA0]])[0]:
            value["controls"] = LDAPMessage__24.decode(
                encoding_rule, stream, value_tracker, [[0xA0]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = LDAPMessage()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "messageID" in value:
            MessageID.validate(value["messageID"], errors, "{}/{}".format(comp_path, "messageID"))
        elif "messageID" not in value:
            report_missing_field(type(self).__name__, "messageID", errors, comp_path)
        if "protocolOp" in value:
            LDAPMessage__23.validate(
                value["protocolOp"], errors, "{}/{}".format(comp_path, "protocolOp")
            )
        elif "protocolOp" not in value:
            report_missing_field(type(self).__name__, "protocolOp", errors, comp_path)
        if "controls" in value:
            LDAPMessage__24.validate(
                value["controls"], errors, "{}/{}".format(comp_path, "controls")
            )

        return errors


class LDAPMessage__23:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.LDAPMessage.protocolOp"
        self._asn1Type = Asn1Type.CHOICE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        choice_type = LDAPMessage__23()
        return choice_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        is_encoded = False

        if not isinstance(value, dict) or len(value.keys()) != 1:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value)

        for identifier, alternative in value.items():
            if identifier == "bindRequest":
                tmpstream.append(
                    BindRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x60]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "bindResponse":
                tmpstream.append(
                    BindResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x61]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "unbindRequest":
                tmpstream.append(
                    UnbindRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x42]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "searchRequest":
                tmpstream.append(
                    SearchRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x63]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "searchResEntry":
                tmpstream.append(
                    SearchResultEntry.encode(
                        encoding_rule, alternative, value_tracker, [[0x64]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "searchResDone":
                tmpstream.append(
                    SearchResultDone.encode(
                        encoding_rule, alternative, value_tracker, [[0x65]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "searchResRef":
                tmpstream.append(
                    SearchResultReference.encode(
                        encoding_rule, alternative, value_tracker, [[0x73]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "modifyRequest":
                tmpstream.append(
                    ModifyRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x66]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "modifyResponse":
                tmpstream.append(
                    ModifyResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x67]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "addRequest":
                tmpstream.append(
                    AddRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x68]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "addResponse":
                tmpstream.append(
                    AddResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x69]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "delRequest":
                tmpstream.append(
                    DelRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x4A]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "delResponse":
                tmpstream.append(
                    DelResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x6B]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "modDNRequest":
                tmpstream.append(
                    ModifyDNRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x6C]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "modDNResponse":
                tmpstream.append(
                    ModifyDNResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x6D]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "compareRequest":
                tmpstream.append(
                    CompareRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x6E]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "compareResponse":
                tmpstream.append(
                    CompareResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x6F]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "abandonRequest":
                tmpstream.append(
                    AbandonRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x50]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "extendedReq":
                tmpstream.append(
                    ExtendedRequest.encode(
                        encoding_rule, alternative, value_tracker, [[0x77]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "extendedResp":
                tmpstream.append(
                    ExtendedResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x78]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "intermediateResponse":
                tmpstream.append(
                    IntermediateResponse.encode(
                        encoding_rule, alternative, value_tracker, [[0x79]]
                    ).get_buffer()
                )
                is_encoded = True
                break

        if not is_encoded:
            if "_unknown_extension" in value:
                tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extension"]))
                is_encoded = True
            else:
                raise ValueError(
                    "62403: The choice alternative identifier is missing from the choice value!"
                )

        used_tag = []
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        choice_type = LDAPMessage__23()
        return choice_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = []
        is_decoded = False

        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, offset = osspy.der.peek_tags(stream, used_tag)
        if correct == 1:
            stream.skip_bytes(offset)

        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x60]])[0] or osspy.der.peek_tags(stream, [[0x60]])[0]
        ):
            value["bindRequest"] = BindRequest.decode(
                encoding_rule, stream, value_tracker, [[0x60]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x61]])[0] or osspy.der.peek_tags(stream, [[0x61]])[0]
        ):
            value["bindResponse"] = BindResponse.decode(
                encoding_rule, stream, value_tracker, [[0x61]]
            )
            is_decoded = True
        if not is_decoded and (osspy.der.peek_tags(stream, [[0x42]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["unbindRequest"] = UnbindRequest.decode(
                encoding_rule, stream, value_tracker, [[0x42]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0x62]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["unbindRequest"] = UnbindRequest.decode(
                encoding_rule, stream, value_tracker, [[0x42]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x63]])[0] or osspy.der.peek_tags(stream, [[0x63]])[0]
        ):
            value["searchRequest"] = SearchRequest.decode(
                encoding_rule, stream, value_tracker, [[0x63]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x64]])[0] or osspy.der.peek_tags(stream, [[0x64]])[0]
        ):
            value["searchResEntry"] = SearchResultEntry.decode(
                encoding_rule, stream, value_tracker, [[0x64]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x65]])[0] or osspy.der.peek_tags(stream, [[0x65]])[0]
        ):
            value["searchResDone"] = SearchResultDone.decode(
                encoding_rule, stream, value_tracker, [[0x65]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x73]])[0] or osspy.der.peek_tags(stream, [[0x73]])[0]
        ):
            value["searchResRef"] = SearchResultReference.decode(
                encoding_rule, stream, value_tracker, [[0x73]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x66]])[0] or osspy.der.peek_tags(stream, [[0x66]])[0]
        ):
            value["modifyRequest"] = ModifyRequest.decode(
                encoding_rule, stream, value_tracker, [[0x66]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x67]])[0] or osspy.der.peek_tags(stream, [[0x67]])[0]
        ):
            value["modifyResponse"] = ModifyResponse.decode(
                encoding_rule, stream, value_tracker, [[0x67]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x68]])[0] or osspy.der.peek_tags(stream, [[0x68]])[0]
        ):
            value["addRequest"] = AddRequest.decode(encoding_rule, stream, value_tracker, [[0x68]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x69]])[0] or osspy.der.peek_tags(stream, [[0x69]])[0]
        ):
            value["addResponse"] = AddResponse.decode(
                encoding_rule, stream, value_tracker, [[0x69]]
            )
            is_decoded = True
        if not is_decoded and (osspy.der.peek_tags(stream, [[0x4A]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["delRequest"] = DelRequest.decode(encoding_rule, stream, value_tracker, [[0x4A]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0x6A]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["delRequest"] = DelRequest.decode(encoding_rule, stream, value_tracker, [[0x4A]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x6B]])[0] or osspy.der.peek_tags(stream, [[0x6B]])[0]
        ):
            value["delResponse"] = DelResponse.decode(
                encoding_rule, stream, value_tracker, [[0x6B]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x6C]])[0] or osspy.der.peek_tags(stream, [[0x6C]])[0]
        ):
            value["modDNRequest"] = ModifyDNRequest.decode(
                encoding_rule, stream, value_tracker, [[0x6C]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x6D]])[0] or osspy.der.peek_tags(stream, [[0x6D]])[0]
        ):
            value["modDNResponse"] = ModifyDNResponse.decode(
                encoding_rule, stream, value_tracker, [[0x6D]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x6E]])[0] or osspy.der.peek_tags(stream, [[0x6E]])[0]
        ):
            value["compareRequest"] = CompareRequest.decode(
                encoding_rule, stream, value_tracker, [[0x6E]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x6F]])[0] or osspy.der.peek_tags(stream, [[0x6F]])[0]
        ):
            value["compareResponse"] = CompareResponse.decode(
                encoding_rule, stream, value_tracker, [[0x6F]]
            )
            is_decoded = True
        if not is_decoded and (osspy.der.peek_tags(stream, [[0x50]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["abandonRequest"] = AbandonRequest.decode(
                encoding_rule, stream, value_tracker, [[0x50]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0x70]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["abandonRequest"] = AbandonRequest.decode(
                encoding_rule, stream, value_tracker, [[0x50]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x77]])[0] or osspy.der.peek_tags(stream, [[0x77]])[0]
        ):
            value["extendedReq"] = ExtendedRequest.decode(
                encoding_rule, stream, value_tracker, [[0x77]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x78]])[0] or osspy.der.peek_tags(stream, [[0x78]])[0]
        ):
            value["extendedResp"] = ExtendedResponse.decode(
                encoding_rule, stream, value_tracker, [[0x78]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0x79]])[0] or osspy.der.peek_tags(stream, [[0x79]])[0]
        ):
            value["intermediateResponse"] = IntermediateResponse.decode(
                encoding_rule, stream, value_tracker, [[0x79]]
            )
            is_decoded = True

        if not is_decoded:
            value["_unknown_extension"] = osspy.der.decode_undecoded_type(stream).hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, len(used_tag))

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        choice_type = LDAPMessage__23()
        return choice_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        is_checked = False
        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "bindRequest" in value:
            BindRequest.validate(
                value["bindRequest"], errors, "{}/{}".format(comp_path, "bindRequest")
            )
            is_checked = True
        if "bindResponse" in value:
            BindResponse.validate(
                value["bindResponse"], errors, "{}/{}".format(comp_path, "bindResponse")
            )
            is_checked = True
        if "unbindRequest" in value:
            UnbindRequest.validate(
                value["unbindRequest"], errors, "{}/{}".format(comp_path, "unbindRequest")
            )
            is_checked = True
        if "searchRequest" in value:
            SearchRequest.validate(
                value["searchRequest"], errors, "{}/{}".format(comp_path, "searchRequest")
            )
            is_checked = True
        if "searchResEntry" in value:
            SearchResultEntry.validate(
                value["searchResEntry"], errors, "{}/{}".format(comp_path, "searchResEntry")
            )
            is_checked = True
        if "searchResDone" in value:
            SearchResultDone.validate(
                value["searchResDone"], errors, "{}/{}".format(comp_path, "searchResDone")
            )
            is_checked = True
        if "searchResRef" in value:
            SearchResultReference.validate(
                value["searchResRef"], errors, "{}/{}".format(comp_path, "searchResRef")
            )
            is_checked = True
        if "modifyRequest" in value:
            ModifyRequest.validate(
                value["modifyRequest"], errors, "{}/{}".format(comp_path, "modifyRequest")
            )
            is_checked = True
        if "modifyResponse" in value:
            ModifyResponse.validate(
                value["modifyResponse"], errors, "{}/{}".format(comp_path, "modifyResponse")
            )
            is_checked = True
        if "addRequest" in value:
            AddRequest.validate(
                value["addRequest"], errors, "{}/{}".format(comp_path, "addRequest")
            )
            is_checked = True
        if "addResponse" in value:
            AddResponse.validate(
                value["addResponse"], errors, "{}/{}".format(comp_path, "addResponse")
            )
            is_checked = True
        if "delRequest" in value:
            DelRequest.validate(
                value["delRequest"], errors, "{}/{}".format(comp_path, "delRequest")
            )
            is_checked = True
        if "delResponse" in value:
            DelResponse.validate(
                value["delResponse"], errors, "{}/{}".format(comp_path, "delResponse")
            )
            is_checked = True
        if "modDNRequest" in value:
            ModifyDNRequest.validate(
                value["modDNRequest"], errors, "{}/{}".format(comp_path, "modDNRequest")
            )
            is_checked = True
        if "modDNResponse" in value:
            ModifyDNResponse.validate(
                value["modDNResponse"], errors, "{}/{}".format(comp_path, "modDNResponse")
            )
            is_checked = True
        if "compareRequest" in value:
            CompareRequest.validate(
                value["compareRequest"], errors, "{}/{}".format(comp_path, "compareRequest")
            )
            is_checked = True
        if "compareResponse" in value:
            CompareResponse.validate(
                value["compareResponse"], errors, "{}/{}".format(comp_path, "compareResponse")
            )
            is_checked = True
        if "abandonRequest" in value:
            AbandonRequest.validate(
                value["abandonRequest"], errors, "{}/{}".format(comp_path, "abandonRequest")
            )
            is_checked = True
        if "extendedReq" in value:
            ExtendedRequest.validate(
                value["extendedReq"], errors, "{}/{}".format(comp_path, "extendedReq")
            )
            is_checked = True
        if "extendedResp" in value:
            ExtendedResponse.validate(
                value["extendedResp"], errors, "{}/{}".format(comp_path, "extendedResp")
            )
            is_checked = True
        if "intermediateResponse" in value:
            IntermediateResponse.validate(
                value["intermediateResponse"],
                errors,
                "{}/{}".format(comp_path, "intermediateResponse"),
            )
            is_checked = True

        if not is_checked and "_unknown_extension" not in value:
            report_empty_value(value, type(self).__name__, errors, comp_path)
        return errors


class LDAPMessage__24:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.LDAPMessage.controls"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = LDAPMessage__24()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    Control.encode(encoding_rule, val, value_tracker, [[0x30]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    Control.encode(encoding_rule, val, value_tracker, [[0x30]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0xA0]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = LDAPMessage__24()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0xA0]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(Control.decode(encoding_rule, stream, value_tracker, [[0x30]]))
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(Control.decode(encoding_rule, stream, value_tracker, [[0x30]]))
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = LDAPMessage__24()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                Control.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class maxInt__1:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = None
        self._asn1Type = Asn1Type.INTEGER

    @staticmethod
    def encode(
        encoding_rule: str,
        value: int,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = maxInt__1()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: int, tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x02]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_integer(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> int:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = maxInt__1()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> int:
        used_tag = [[0x02]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_integer(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = maxInt__1()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class AttributeValueAssertion:
    def __init__(self):
        self._comp_types = {"attributeDesc": AssertionValue, "assertionValue": AssertionValue}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["attributeDesc", "assertionValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AttributeValueAssertion"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = AttributeValueAssertion()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "attributeDesc" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["attributeDesc"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "assertionValue" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["assertionValue"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = AttributeValueAssertion()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "attributeDesc" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "assertionValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = AttributeValueAssertion()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "attributeDesc" in value:
            AssertionValue.validate(
                value["attributeDesc"], errors, "{}/{}".format(comp_path, "attributeDesc")
            )
        elif "attributeDesc" not in value:
            report_missing_field(type(self).__name__, "attributeDesc", errors, comp_path)
        if "assertionValue" in value:
            AssertionValue.validate(
                value["assertionValue"], errors, "{}/{}".format(comp_path, "assertionValue")
            )
        elif "assertionValue" not in value:
            report_missing_field(type(self).__name__, "assertionValue", errors, comp_path)

        return errors


class PartialAttribute:
    def __init__(self):
        self._comp_types = {"type": AssertionValue, "vals": PartialAttribute__3}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["type"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.PartialAttribute"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = PartialAttribute()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "type" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["type"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "vals" in value:
            tmpstream.append(
                PartialAttribute__3.encode(
                    encoding_rule, value["vals"], value_tracker, [[0x31]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = PartialAttribute()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "type" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x31]])[0]:
            value["vals"] = PartialAttribute__3.decode(
                encoding_rule, stream, value_tracker, [[0x31]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = PartialAttribute()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "type" in value:
            AssertionValue.validate(value["type"], errors, "{}/{}".format(comp_path, "type"))
        elif "type" not in value:
            report_missing_field(type(self).__name__, "type", errors, comp_path)
        if "vals" in value:
            PartialAttribute__3.validate(value["vals"], errors, "{}/{}".format(comp_path, "vals"))
        elif "vals" not in value:
            report_missing_field(type(self).__name__, "vals", errors, comp_path)

        return errors


class PartialAttribute__3:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.PartialAttribute.vals"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = PartialAttribute__3()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = True
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x31]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = PartialAttribute__3()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x31]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                if is_indefinite and osspy.der.is_eoc(stream):
                    osspy.der.skip_eoc(stream, 1)
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = PartialAttribute__3()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                AssertionValue.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class Attribute:
    def __init__(self):
        self._comp_types = {"type": AssertionValue, "vals": PartialAttribute_1__2}
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "inner type constraint", "components": [{"vals": {}}]},
            }
        ]
        self._def_vals = {}
        self._frag_components = ["type"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Attribute"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Attribute()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "type" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["type"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "vals" in value:
            tmpstream.append(
                PartialAttribute_1__2.encode(
                    encoding_rule, value["vals"], value_tracker, [[0x31]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Attribute()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "type" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x31]])[0]:
            value["vals"] = PartialAttribute_1__2.decode(
                encoding_rule, stream, value_tracker, [[0x31]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Attribute()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "type" in value:
            AssertionValue.validate(value["type"], errors, "{}/{}".format(comp_path, "type"))
        elif "type" not in value:
            report_missing_field(type(self).__name__, "type", errors, comp_path)
        if "vals" in value:
            PartialAttribute_1__2.validate(value["vals"], errors, "{}/{}".format(comp_path, "vals"))
        elif "vals" not in value:
            report_missing_field(type(self).__name__, "vals", errors, comp_path)

        return errors


class LDAPResult:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.LDAPResult"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = LDAPResult()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = LDAPResult()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = LDAPResult()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))

        return errors


class LDAPResult__1:
    def __init__(self):
        self._constraints = []
        self._identifiers = {
            "success": 0,
            "operationsError": 1,
            "protocolError": 2,
            "timeLimitExceeded": 3,
            "sizeLimitExceeded": 4,
            "compareFalse": 5,
            "compareTrue": 6,
            "authMethodNotSupported": 7,
            "strongerAuthRequired": 8,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 16,
            "undefinedAttributeType": 17,
            "inappropriateMatching": 18,
            "constraintViolation": 19,
            "attributeOrValueExists": 20,
            "invalidAttributeSyntax": 21,
            "noSuchObject": 32,
            "aliasProblem": 33,
            "invalidDNSyntax": 34,
            "aliasDereferencingProblem": 36,
            "inappropriateAuthentication": 48,
            "invalidCredentials": 49,
            "insufficientAccessRights": 50,
            "busy": 51,
            "unavailable": 52,
            "unwillingToPerform": 53,
            "loopDetect": 54,
            "namingViolation": 64,
            "objectClassViolation": 65,
            "notAllowedOnNonLeaf": 66,
            "notAllowedOnRDN": 67,
            "entryAlreadyExists": 68,
            "objectClassModsProhibited": 69,
            "affectsMultipleDSAs": 71,
            "other": 80,
        }
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.LDAPResult.resultCode"
        self._asn1Type = Asn1Type.ENUMERATED

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, int],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        enum_type = LDAPResult__1()
        return enum_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: Union[str, int], tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        if not isinstance(value, int) and not isinstance(value, str):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        int_val = None
        if isinstance(value, int) and value in self._identifiers.values():
            int_val = value

        if value in self._identifiers:
            int_val = self._identifiers[value]

        if int_val is None and isinstance(value, int):
            int_val = value

        if int_val is None:
            raise ValueError(
                "62603: The enumeration item identifier is missing from the enumerated value!"
            )

        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag
        osspy.der.encode_integer(stream, int_val, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, int]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        enum_type = LDAPResult__1()
        return enum_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> Union[str, int]:
        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_integer(stream, used_tag)

        identifier = None
        for item in self._identifiers:
            if self._identifiers[item] == value:
                identifier = item

        if identifier is not None:
            return identifier

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        enum_type = LDAPResult__1()
        return enum_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        if isinstance(value, int) and value not in self._identifiers.keys():
            report_extra_field(
                value, type(self).__name__, value, errors, comp_path, list(self._identifiers.keys())
            )
        return errors


class LDAPResult__4:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "size constraint", "permitted": [(1, float("inf"))]},
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.LDAPResult.referral"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = LDAPResult__4()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0xA3]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = LDAPResult__4()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0xA3]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                if is_indefinite and osspy.der.is_eoc(stream):
                    osspy.der.skip_eoc(stream, 1)
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = LDAPResult__4()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                AssertionValue.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class Referral:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "size constraint", "permitted": [(1, float("inf"))]},
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Referral"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = Referral()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = Referral()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                if is_indefinite and osspy.der.is_eoc(stream):
                    osspy.der.skip_eoc(stream, 1)
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = Referral()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                AssertionValue.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class Controls:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Controls"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = Controls()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    Control.encode(encoding_rule, val, value_tracker, [[0x30]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    Control.encode(encoding_rule, val, value_tracker, [[0x30]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = Controls()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(Control.decode(encoding_rule, stream, value_tracker, [[0x30]]))
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(Control.decode(encoding_rule, stream, value_tracker, [[0x30]]))
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = Controls()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                Control.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class Control:
    def __init__(self):
        self._comp_types = {
            "controlType": AssertionValue,
            "criticality": Control__2,
            "controlValue": AssertionValue,
        }
        self._constraints = []
        self._def_vals = {"criticality": False}
        self._frag_components = ["controlType", "controlValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Control"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Control()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "controlType" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["controlType"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "criticality" in value and "criticality" in self._def_vals:
            if not value_tracker.are_def_eq(
                value["criticality"], self._def_vals["criticality"], self._comp_types["criticality"]
            ):
                tmpstream.append(
                    Control__2.encode(
                        encoding_rule, value["criticality"], value_tracker, [[0x01]]
                    ).get_buffer()
                )
        if "controlValue" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["controlValue"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Control()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["controlType"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["controlType"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "controlType" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["controlType"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x01]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["criticality"] = Control__2.decode(encoding_rule, stream, value_tracker, [[0x01]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x21], [0x01]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["criticality"] = Control__2.decode(
                encoding_rule, stream, value_tracker, [[0x21], [0x01]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "criticality" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x21]])[0]
        ):
            value["criticality"] = Control__2.decode(encoding_rule, stream, value_tracker, [[0x01]])
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["controlValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["controlValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "controlValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["controlValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Control()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "controlType" in value:
            AssertionValue.validate(
                value["controlType"], errors, "{}/{}".format(comp_path, "controlType")
            )
        elif "controlType" not in value:
            report_missing_field(type(self).__name__, "controlType", errors, comp_path)
        if "criticality" in value:
            Control__2.validate(
                value["criticality"], errors, "{}/{}".format(comp_path, "criticality")
            )
        if "controlValue" in value:
            AssertionValue.validate(
                value["controlValue"], errors, "{}/{}".format(comp_path, "controlValue")
            )

        return errors


class BindRequest:
    def __init__(self):
        self._comp_types = {
            "version": BindRequest__1,
            "name": AssertionValue,
            "authentication": AuthenticationChoice,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["name"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.BindRequest"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = BindRequest()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "version" in value:
            tmpstream.append(
                BindRequest__1.encode(
                    encoding_rule, value["version"], value_tracker, [[0x02]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "name" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["name"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "authentication" in value:
            tmpstream.append(
                AuthenticationChoice.encode(
                    encoding_rule, value["authentication"], value_tracker, []
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x60]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = BindRequest()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x60]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["version"] = BindRequest__1.decode(encoding_rule, stream, value_tracker, [[0x02]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x22], [0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["version"] = BindRequest__1.decode(
                encoding_rule, stream, value_tracker, [[0x22], [0x02]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "version" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x22]])[0]
        ):
            value["version"] = BindRequest__1.decode(encoding_rule, stream, value_tracker, [[0x02]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["name"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["name"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "name" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["name"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_discriminating_tags(stream, [[[0x80]], [[0xA3]]])[0]:
            value["authentication"] = AuthenticationChoice.decode(
                encoding_rule, stream, value_tracker, []
            )
        elif stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            value["authentication"] = AuthenticationChoice.decode(
                encoding_rule, stream, value_tracker, []
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = BindRequest()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "version" in value:
            BindRequest__1.validate(value["version"], errors, "{}/{}".format(comp_path, "version"))
        elif "version" not in value:
            report_missing_field(type(self).__name__, "version", errors, comp_path)
        if "name" in value:
            AssertionValue.validate(value["name"], errors, "{}/{}".format(comp_path, "name"))
        elif "name" not in value:
            report_missing_field(type(self).__name__, "name", errors, comp_path)
        if "authentication" in value:
            AuthenticationChoice.validate(
                value["authentication"], errors, "{}/{}".format(comp_path, "authentication")
            )
        elif "authentication" not in value:
            report_missing_field(type(self).__name__, "authentication", errors, comp_path)

        return errors


class BindRequest__1:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {
                    "type": "value range",
                    "definition": "1 ..  127",
                    "permitted": [(1, 127)],
                },
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.BindRequest.version"
        self._asn1Type = Asn1Type.INTEGER

    @staticmethod
    def encode(
        encoding_rule: str,
        value: int,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = BindRequest__1()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: int, tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x02]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_integer(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> int:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = BindRequest__1()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> int:
        used_tag = [[0x02]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_integer(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = BindRequest__1()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class AuthenticationChoice:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AuthenticationChoice"
        self._asn1Type = Asn1Type.CHOICE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        choice_type = AuthenticationChoice()
        return choice_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        is_encoded = False

        if not isinstance(value, dict) or len(value.keys()) != 1:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value)

        for identifier, alternative in value.items():
            if identifier == "simple":
                tmpstream.append(
                    AuthenticationChoice__1.encode(
                        encoding_rule, alternative, value_tracker, [[0x80]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "sasl":
                tmpstream.append(
                    AuthenticationChoice__2.encode(
                        encoding_rule, alternative, value_tracker, [[0xA3]]
                    ).get_buffer()
                )
                is_encoded = True
                break

        if not is_encoded:
            if "_unknown_extension" in value:
                tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extension"]))
                is_encoded = True
            else:
                raise ValueError(
                    "62403: The choice alternative identifier is missing from the choice value!"
                )

        used_tag = []
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        choice_type = AuthenticationChoice()
        return choice_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = []
        is_decoded = False

        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, offset = osspy.der.peek_tags(stream, used_tag)
        if correct == 1:
            stream.skip_bytes(offset)

        if not is_decoded and (osspy.der.peek_tags(stream, [[0x80]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["simple"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0xA0]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["simple"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA3]])[0] or osspy.der.peek_tags(stream, [[0xA3]])[0]
        ):
            value["sasl"] = AuthenticationChoice__2.decode(
                encoding_rule, stream, value_tracker, [[0xA3]]
            )
            is_decoded = True

        if not is_decoded:
            value["_unknown_extension"] = osspy.der.decode_undecoded_type(stream).hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, len(used_tag))

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        choice_type = AuthenticationChoice()
        return choice_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        is_checked = False
        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "simple" in value:
            AuthenticationChoice__1.validate(
                value["simple"], errors, "{}/{}".format(comp_path, "simple")
            )
            is_checked = True
        if "sasl" in value:
            AuthenticationChoice__2.validate(
                value["sasl"], errors, "{}/{}".format(comp_path, "sasl")
            )
            is_checked = True

        if not is_checked and "_unknown_extension" not in value:
            report_empty_value(value, type(self).__name__, errors, comp_path)
        return errors


class AuthenticationChoice__2:
    def __init__(self):
        self._comp_types = {"mechanism": AssertionValue, "credentials": AssertionValue}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["mechanism", "credentials"]
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.AuthenticationChoice.sasl"
        )
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = AuthenticationChoice__2()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "mechanism" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["mechanism"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "credentials" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["credentials"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0xA3]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = AuthenticationChoice__2()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA3]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["mechanism"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["mechanism"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "mechanism" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["mechanism"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["credentials"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["credentials"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "credentials" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["credentials"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = AuthenticationChoice__2()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "mechanism" in value:
            AssertionValue.validate(
                value["mechanism"], errors, "{}/{}".format(comp_path, "mechanism")
            )
        elif "mechanism" not in value:
            report_missing_field(type(self).__name__, "mechanism", errors, comp_path)
        if "credentials" in value:
            AssertionValue.validate(
                value["credentials"], errors, "{}/{}".format(comp_path, "credentials")
            )

        return errors


class SaslCredentials:
    def __init__(self):
        self._comp_types = {"mechanism": AssertionValue, "credentials": AssertionValue}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["mechanism", "credentials"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.SaslCredentials"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = SaslCredentials()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "mechanism" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["mechanism"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "credentials" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["credentials"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = SaslCredentials()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["mechanism"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["mechanism"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "mechanism" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["mechanism"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["credentials"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["credentials"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "credentials" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["credentials"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = SaslCredentials()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "mechanism" in value:
            AssertionValue.validate(
                value["mechanism"], errors, "{}/{}".format(comp_path, "mechanism")
            )
        elif "mechanism" not in value:
            report_missing_field(type(self).__name__, "mechanism", errors, comp_path)
        if "credentials" in value:
            AssertionValue.validate(
                value["credentials"], errors, "{}/{}".format(comp_path, "credentials")
            )

        return errors


class AssertionValue:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AssertionValue"
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = AssertionValue()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x04]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = AssertionValue()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x04]]
        c_tag = [[0x24]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = AssertionValue()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


AttributeDescription = AssertionValue
AttributeValue = AssertionValue
LDAPDN = AssertionValue
LDAPOID = AssertionValue
LDAPString = AssertionValue
MatchingRuleId = AssertionValue
RelativeLDAPDN = AssertionValue
URI = AssertionValue
Control__4 = AssertionValue
SaslCredentials__2 = AssertionValue


class BindResponse:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
            "serverSaslCreds": Filter__14,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage", "serverSaslCreds"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.BindResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = BindResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "serverSaslCreds" in value:
            tmpstream.append(
                Filter__14.encode(
                    encoding_rule, value["serverSaslCreds"], value_tracker, [[0x87]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x61]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = BindResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x61]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x87]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["serverSaslCreds"] = Filter__14.decode(
                encoding_rule, stream, value_tracker, [[0x87]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA7], [0x87]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["serverSaslCreds"] = Filter__14.decode(
                encoding_rule, stream, value_tracker, [[0xA7], [0x87]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "serverSaslCreds" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA7]])[0]
        ):
            value["serverSaslCreds"] = Filter__14.decode(
                encoding_rule, stream, value_tracker, [[0x87]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = BindResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))
        if "serverSaslCreds" in value:
            Filter__14.validate(
                value["serverSaslCreds"], errors, "{}/{}".format(comp_path, "serverSaslCreds")
            )

        return errors


class UnbindRequest:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.UnbindRequest"
        self._asn1Type = Asn1Type.NULL

    @staticmethod
    def encode(
        encoding_rule: str,
        value: None,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = UnbindRequest()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: None, tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x42]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_null(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> None:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = UnbindRequest()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> None:
        used_tag = [[0x42]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_null(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = UnbindRequest()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class SearchRequest:
    def __init__(self):
        self._comp_types = {
            "baseObject": AssertionValue,
            "scope": SearchRequest__2,
            "derefAliases": SearchRequest__3,
            "sizeLimit": MessageID,
            "timeLimit": MessageID,
            "typesOnly": Control__2,
            "filter": Filter,
            "attributes": AttributeSelection,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["baseObject"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.SearchRequest"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = SearchRequest()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "baseObject" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["baseObject"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "scope" in value:
            tmpstream.append(
                SearchRequest__2.encode(
                    encoding_rule, value["scope"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "derefAliases" in value:
            tmpstream.append(
                SearchRequest__3.encode(
                    encoding_rule, value["derefAliases"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "sizeLimit" in value:
            tmpstream.append(
                MessageID.encode(
                    encoding_rule, value["sizeLimit"], value_tracker, [[0x02]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "timeLimit" in value:
            tmpstream.append(
                MessageID.encode(
                    encoding_rule, value["timeLimit"], value_tracker, [[0x02]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "typesOnly" in value:
            tmpstream.append(
                Control__2.encode(
                    encoding_rule, value["typesOnly"], value_tracker, [[0x01]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "filter" in value:
            tmpstream.append(
                Filter.encode(encoding_rule, value["filter"], value_tracker, []).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "attributes" in value:
            tmpstream.append(
                AttributeSelection.encode(
                    encoding_rule, value["attributes"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x63]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = SearchRequest()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x63]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["baseObject"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["baseObject"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "baseObject" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["baseObject"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["scope"] = SearchRequest__2.decode(encoding_rule, stream, value_tracker, [[0x0A]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["scope"] = SearchRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "scope" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["scope"] = SearchRequest__2.decode(encoding_rule, stream, value_tracker, [[0x0A]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["derefAliases"] = SearchRequest__3.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["derefAliases"] = SearchRequest__3.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "derefAliases" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["derefAliases"] = SearchRequest__3.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["sizeLimit"] = MessageID.decode(encoding_rule, stream, value_tracker, [[0x02]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x22], [0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["sizeLimit"] = MessageID.decode(
                encoding_rule, stream, value_tracker, [[0x22], [0x02]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "sizeLimit" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x22]])[0]
        ):
            value["sizeLimit"] = MessageID.decode(encoding_rule, stream, value_tracker, [[0x02]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["timeLimit"] = MessageID.decode(encoding_rule, stream, value_tracker, [[0x02]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x22], [0x02]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["timeLimit"] = MessageID.decode(
                encoding_rule, stream, value_tracker, [[0x22], [0x02]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "timeLimit" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x22]])[0]
        ):
            value["timeLimit"] = MessageID.decode(encoding_rule, stream, value_tracker, [[0x02]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x01]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["typesOnly"] = Control__2.decode(encoding_rule, stream, value_tracker, [[0x01]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x21], [0x01]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["typesOnly"] = Control__2.decode(
                encoding_rule, stream, value_tracker, [[0x21], [0x01]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "typesOnly" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x21]])[0]
        ):
            value["typesOnly"] = Control__2.decode(encoding_rule, stream, value_tracker, [[0x01]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_discriminating_tags(
            stream,
            [
                [[0xA0]],
                [[0xA1]],
                [[0xA2]],
                [[0xA3]],
                [[0xA4]],
                [[0xA5]],
                [[0xA6]],
                [[0x87]],
                [[0xA8]],
                [[0xA9]],
            ],
        )[
            0
        ]:
            value["filter"] = Filter.decode(encoding_rule, stream, value_tracker, [])
        elif stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            value["filter"] = Filter.decode(encoding_rule, stream, value_tracker, [])
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["attributes"] = AttributeSelection.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = SearchRequest()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "baseObject" in value:
            AssertionValue.validate(
                value["baseObject"], errors, "{}/{}".format(comp_path, "baseObject")
            )
        elif "baseObject" not in value:
            report_missing_field(type(self).__name__, "baseObject", errors, comp_path)
        if "scope" in value:
            SearchRequest__2.validate(value["scope"], errors, "{}/{}".format(comp_path, "scope"))
        elif "scope" not in value:
            report_missing_field(type(self).__name__, "scope", errors, comp_path)
        if "derefAliases" in value:
            SearchRequest__3.validate(
                value["derefAliases"], errors, "{}/{}".format(comp_path, "derefAliases")
            )
        elif "derefAliases" not in value:
            report_missing_field(type(self).__name__, "derefAliases", errors, comp_path)
        if "sizeLimit" in value:
            MessageID.validate(value["sizeLimit"], errors, "{}/{}".format(comp_path, "sizeLimit"))
        elif "sizeLimit" not in value:
            report_missing_field(type(self).__name__, "sizeLimit", errors, comp_path)
        if "timeLimit" in value:
            MessageID.validate(value["timeLimit"], errors, "{}/{}".format(comp_path, "timeLimit"))
        elif "timeLimit" not in value:
            report_missing_field(type(self).__name__, "timeLimit", errors, comp_path)
        if "typesOnly" in value:
            Control__2.validate(value["typesOnly"], errors, "{}/{}".format(comp_path, "typesOnly"))
        elif "typesOnly" not in value:
            report_missing_field(type(self).__name__, "typesOnly", errors, comp_path)
        if "filter" in value:
            Filter.validate(value["filter"], errors, "{}/{}".format(comp_path, "filter"))
        elif "filter" not in value:
            report_missing_field(type(self).__name__, "filter", errors, comp_path)
        if "attributes" in value:
            AttributeSelection.validate(
                value["attributes"], errors, "{}/{}".format(comp_path, "attributes")
            )
        elif "attributes" not in value:
            report_missing_field(type(self).__name__, "attributes", errors, comp_path)

        return errors


class SearchRequest__2:
    def __init__(self):
        self._constraints = []
        self._identifiers = {"baseObject": 0, "singleLevel": 1, "wholeSubtree": 2}
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.SearchRequest.scope"
        self._asn1Type = Asn1Type.ENUMERATED

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, int],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        enum_type = SearchRequest__2()
        return enum_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: Union[str, int], tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        if not isinstance(value, int) and not isinstance(value, str):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        int_val = None
        if isinstance(value, int) and value in self._identifiers.values():
            int_val = value

        if value in self._identifiers:
            int_val = self._identifiers[value]

        if int_val is None and isinstance(value, int):
            int_val = value

        if int_val is None:
            raise ValueError(
                "62603: The enumeration item identifier is missing from the enumerated value!"
            )

        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag
        osspy.der.encode_integer(stream, int_val, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, int]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        enum_type = SearchRequest__2()
        return enum_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> Union[str, int]:
        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_integer(stream, used_tag)

        identifier = None
        for item in self._identifiers:
            if self._identifiers[item] == value:
                identifier = item

        if identifier is not None:
            return identifier

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        enum_type = SearchRequest__2()
        return enum_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        if isinstance(value, int) and value not in self._identifiers.keys():
            report_extra_field(
                value, type(self).__name__, value, errors, comp_path, list(self._identifiers.keys())
            )
        return errors


class SearchRequest__3:
    def __init__(self):
        self._constraints = []
        self._identifiers = {
            "neverDerefAliases": 0,
            "derefInSearching": 1,
            "derefFindingBaseObj": 2,
            "derefAlways": 3,
        }
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.SearchRequest.derefAliases"
        )
        self._asn1Type = Asn1Type.ENUMERATED

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, int],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        enum_type = SearchRequest__3()
        return enum_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: Union[str, int], tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        if not isinstance(value, int) and not isinstance(value, str):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        int_val = None
        if isinstance(value, int) and value in self._identifiers.values():
            int_val = value

        if value in self._identifiers:
            int_val = self._identifiers[value]

        if int_val is None and isinstance(value, int):
            int_val = value

        if int_val is None:
            raise ValueError(
                "62603: The enumeration item identifier is missing from the enumerated value!"
            )

        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag
        osspy.der.encode_integer(stream, int_val, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, int]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        enum_type = SearchRequest__3()
        return enum_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> Union[str, int]:
        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_integer(stream, used_tag)

        identifier = None
        for item in self._identifiers:
            if self._identifiers[item] == value:
                identifier = item

        if identifier is not None:
            return identifier

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        enum_type = SearchRequest__3()
        return enum_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        if isinstance(value, int) and value not in self._identifiers.keys():
            report_extra_field(
                value, type(self).__name__, value, errors, comp_path, list(self._identifiers.keys())
            )
        return errors


class MessageID:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {
                    "type": "value range",
                    "definition": "0 ..  maxInt",
                    "permitted": [(0, 2147483647)],
                },
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.MessageID"
        self._asn1Type = Asn1Type.INTEGER

    @staticmethod
    def encode(
        encoding_rule: str,
        value: int,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = MessageID()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: int, tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x02]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_integer(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> int:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = MessageID()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> int:
        used_tag = [[0x02]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_integer(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = MessageID()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


SearchRequest__4 = MessageID
SearchRequest__6 = MessageID


class AttributeSelection:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AttributeSelection"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = AttributeSelection()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = AttributeSelection()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                if is_indefinite and osspy.der.is_eoc(stream):
                    osspy.der.skip_eoc(stream, 1)
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = AttributeSelection()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                AssertionValue.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class Filter:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter"
        self._asn1Type = Asn1Type.CHOICE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        choice_type = Filter()
        return choice_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        is_encoded = False

        if not isinstance(value, dict) or len(value.keys()) != 1:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value)

        for identifier, alternative in value.items():
            if identifier == "and":
                tmpstream.append(
                    Filter__2.encode(
                        encoding_rule, alternative, value_tracker, [[0xA0]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "or":
                tmpstream.append(
                    Filter__5.encode(
                        encoding_rule, alternative, value_tracker, [[0xA1]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "not":
                tmpstream.append(
                    Filter__9.encode(
                        encoding_rule, alternative, value_tracker, [[0xA2]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "equalityMatch":
                tmpstream.append(
                    Filter__10.encode(
                        encoding_rule, alternative, value_tracker, [[0xA3]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "substrings":
                tmpstream.append(
                    Filter__11.encode(
                        encoding_rule, alternative, value_tracker, [[0xA4]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "greaterOrEqual":
                tmpstream.append(
                    Filter__12.encode(
                        encoding_rule, alternative, value_tracker, [[0xA5]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "lessOrEqual":
                tmpstream.append(
                    Filter__13.encode(
                        encoding_rule, alternative, value_tracker, [[0xA6]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "present":
                tmpstream.append(
                    Filter__14.encode(
                        encoding_rule, alternative, value_tracker, [[0x87]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "approxMatch":
                tmpstream.append(
                    Filter__15.encode(
                        encoding_rule, alternative, value_tracker, [[0xA8]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "extensibleMatch":
                tmpstream.append(
                    Filter__16.encode(
                        encoding_rule, alternative, value_tracker, [[0xA9]]
                    ).get_buffer()
                )
                is_encoded = True
                break

        if not is_encoded:
            if "_unknown_extension" in value:
                tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extension"]))
                is_encoded = True
            else:
                raise ValueError(
                    "62403: The choice alternative identifier is missing from the choice value!"
                )

        used_tag = []
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        choice_type = Filter()
        return choice_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = []
        is_decoded = False

        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, offset = osspy.der.peek_tags(stream, used_tag)
        if correct == 1:
            stream.skip_bytes(offset)

        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA0]])[0] or osspy.der.peek_tags(stream, [[0xA0]])[0]
        ):
            value["and"] = Filter__2.decode(encoding_rule, stream, value_tracker, [[0xA0]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA1]])[0] or osspy.der.peek_tags(stream, [[0xA1]])[0]
        ):
            value["or"] = Filter__5.decode(encoding_rule, stream, value_tracker, [[0xA1]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA2]])[0] or osspy.der.peek_tags(stream, [[0xA2]])[0]
        ):
            value["not"] = Filter__9.decode(encoding_rule, stream, value_tracker, [[0xA2]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA3]])[0] or osspy.der.peek_tags(stream, [[0xA3]])[0]
        ):
            value["equalityMatch"] = Filter__10.decode(
                encoding_rule, stream, value_tracker, [[0xA3]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA4]])[0] or osspy.der.peek_tags(stream, [[0xA4]])[0]
        ):
            value["substrings"] = Filter__11.decode(encoding_rule, stream, value_tracker, [[0xA4]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA5]])[0] or osspy.der.peek_tags(stream, [[0xA5]])[0]
        ):
            value["greaterOrEqual"] = Filter__12.decode(
                encoding_rule, stream, value_tracker, [[0xA5]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA6]])[0] or osspy.der.peek_tags(stream, [[0xA6]])[0]
        ):
            value["lessOrEqual"] = Filter__13.decode(encoding_rule, stream, value_tracker, [[0xA6]])
            is_decoded = True
        if not is_decoded and (osspy.der.peek_tags(stream, [[0x87]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["present"] = Filter__14.decode(encoding_rule, stream, value_tracker, [[0x87]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0xA7]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["present"] = Filter__14.decode(encoding_rule, stream, value_tracker, [[0x87]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA8]])[0] or osspy.der.peek_tags(stream, [[0xA8]])[0]
        ):
            value["approxMatch"] = Filter__15.decode(encoding_rule, stream, value_tracker, [[0xA8]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA9]])[0] or osspy.der.peek_tags(stream, [[0xA9]])[0]
        ):
            value["extensibleMatch"] = Filter__16.decode(
                encoding_rule, stream, value_tracker, [[0xA9]]
            )
            is_decoded = True

        if not is_decoded:
            value["_unknown_extension"] = osspy.der.decode_undecoded_type(stream).hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, len(used_tag))

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        choice_type = Filter()
        return choice_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        is_checked = False
        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "and" in value:
            Filter__2.validate(value["and"], errors, "{}/{}".format(comp_path, "and"))
            is_checked = True
        if "or" in value:
            Filter__5.validate(value["or"], errors, "{}/{}".format(comp_path, "or"))
            is_checked = True
        if "not" in value:
            Filter__9.validate(value["not"], errors, "{}/{}".format(comp_path, "not"))
            is_checked = True
        if "equalityMatch" in value:
            Filter__10.validate(
                value["equalityMatch"], errors, "{}/{}".format(comp_path, "equalityMatch")
            )
            is_checked = True
        if "substrings" in value:
            Filter__11.validate(
                value["substrings"], errors, "{}/{}".format(comp_path, "substrings")
            )
            is_checked = True
        if "greaterOrEqual" in value:
            Filter__12.validate(
                value["greaterOrEqual"], errors, "{}/{}".format(comp_path, "greaterOrEqual")
            )
            is_checked = True
        if "lessOrEqual" in value:
            Filter__13.validate(
                value["lessOrEqual"], errors, "{}/{}".format(comp_path, "lessOrEqual")
            )
            is_checked = True
        if "present" in value:
            Filter__14.validate(value["present"], errors, "{}/{}".format(comp_path, "present"))
            is_checked = True
        if "approxMatch" in value:
            Filter__15.validate(
                value["approxMatch"], errors, "{}/{}".format(comp_path, "approxMatch")
            )
            is_checked = True
        if "extensibleMatch" in value:
            Filter__16.validate(
                value["extensibleMatch"], errors, "{}/{}".format(comp_path, "extensibleMatch")
            )
            is_checked = True

        if not is_checked and "_unknown_extension" not in value:
            report_empty_value(value, type(self).__name__, errors, comp_path)
        return errors


class Filter__2:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "size constraint", "permitted": [(1, float("inf"))]},
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.and"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = Filter__2()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = True
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(Filter.encode(encoding_rule, val, value_tracker, []).get_buffer())
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(Filter.encode(encoding_rule, val, value_tracker, []).get_buffer())
                value_tracker.remove_ancestor()

        used_tag = [[0xA0]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = Filter__2()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0xA0]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(Filter.decode(encoding_rule, stream, value_tracker, []))
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(Filter.decode(encoding_rule, stream, value_tracker, []))
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = Filter__2()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                Filter.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class Filter__5:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "size constraint", "permitted": [(1, float("inf"))]},
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.or"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = Filter__5()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = True
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(Filter.encode(encoding_rule, val, value_tracker, []).get_buffer())
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(Filter.encode(encoding_rule, val, value_tracker, []).get_buffer())
                value_tracker.remove_ancestor()

        used_tag = [[0xA1]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = Filter__5()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0xA1]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(Filter.decode(encoding_rule, stream, value_tracker, []))
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(Filter.decode(encoding_rule, stream, value_tracker, []))
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = Filter__5()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                Filter.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class Filter__9:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.not"
        self._asn1Type = Asn1Type.CHOICE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        choice_type = Filter__9()
        return choice_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        is_encoded = False

        if not isinstance(value, dict) or len(value.keys()) != 1:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value)

        for identifier, alternative in value.items():
            if identifier == "and":
                tmpstream.append(
                    Filter__2.encode(
                        encoding_rule, alternative, value_tracker, [[0xA0]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "or":
                tmpstream.append(
                    Filter__5.encode(
                        encoding_rule, alternative, value_tracker, [[0xA1]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "not":
                tmpstream.append(
                    Filter__9.encode(
                        encoding_rule, alternative, value_tracker, [[0xA2]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "equalityMatch":
                tmpstream.append(
                    Filter__10.encode(
                        encoding_rule, alternative, value_tracker, [[0xA3]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "substrings":
                tmpstream.append(
                    Filter__11.encode(
                        encoding_rule, alternative, value_tracker, [[0xA4]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "greaterOrEqual":
                tmpstream.append(
                    Filter__12.encode(
                        encoding_rule, alternative, value_tracker, [[0xA5]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "lessOrEqual":
                tmpstream.append(
                    Filter__13.encode(
                        encoding_rule, alternative, value_tracker, [[0xA6]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "present":
                tmpstream.append(
                    Filter__14.encode(
                        encoding_rule, alternative, value_tracker, [[0x87]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "approxMatch":
                tmpstream.append(
                    Filter__15.encode(
                        encoding_rule, alternative, value_tracker, [[0xA8]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "extensibleMatch":
                tmpstream.append(
                    Filter__16.encode(
                        encoding_rule, alternative, value_tracker, [[0xA9]]
                    ).get_buffer()
                )
                is_encoded = True
                break

        if not is_encoded:
            if "_unknown_extension" in value:
                tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extension"]))
                is_encoded = True
            else:
                raise ValueError(
                    "62403: The choice alternative identifier is missing from the choice value!"
                )

        used_tag = [[0xA2]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        choice_type = Filter__9()
        return choice_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA2]]
        is_decoded = False

        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, offset = osspy.der.peek_tags(stream, used_tag)
        if correct == 1:
            stream.skip_bytes(offset)

        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA0]])[0] or osspy.der.peek_tags(stream, [[0xA0]])[0]
        ):
            value["and"] = Filter__2.decode(encoding_rule, stream, value_tracker, [[0xA0]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA1]])[0] or osspy.der.peek_tags(stream, [[0xA1]])[0]
        ):
            value["or"] = Filter__5.decode(encoding_rule, stream, value_tracker, [[0xA1]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA2]])[0] or osspy.der.peek_tags(stream, [[0xA2]])[0]
        ):
            value["not"] = Filter__9.decode(encoding_rule, stream, value_tracker, [[0xA2]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA3]])[0] or osspy.der.peek_tags(stream, [[0xA3]])[0]
        ):
            value["equalityMatch"] = Filter__10.decode(
                encoding_rule, stream, value_tracker, [[0xA3]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA4]])[0] or osspy.der.peek_tags(stream, [[0xA4]])[0]
        ):
            value["substrings"] = Filter__11.decode(encoding_rule, stream, value_tracker, [[0xA4]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA5]])[0] or osspy.der.peek_tags(stream, [[0xA5]])[0]
        ):
            value["greaterOrEqual"] = Filter__12.decode(
                encoding_rule, stream, value_tracker, [[0xA5]]
            )
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA6]])[0] or osspy.der.peek_tags(stream, [[0xA6]])[0]
        ):
            value["lessOrEqual"] = Filter__13.decode(encoding_rule, stream, value_tracker, [[0xA6]])
            is_decoded = True
        if not is_decoded and (osspy.der.peek_tags(stream, [[0x87]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["present"] = Filter__14.decode(encoding_rule, stream, value_tracker, [[0x87]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0xA7]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["present"] = Filter__14.decode(encoding_rule, stream, value_tracker, [[0x87]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA8]])[0] or osspy.der.peek_tags(stream, [[0xA8]])[0]
        ):
            value["approxMatch"] = Filter__15.decode(encoding_rule, stream, value_tracker, [[0xA8]])
            is_decoded = True
        if not is_decoded and (
            osspy.der.peek_tags(stream, [[0xA9]])[0] or osspy.der.peek_tags(stream, [[0xA9]])[0]
        ):
            value["extensibleMatch"] = Filter__16.decode(
                encoding_rule, stream, value_tracker, [[0xA9]]
            )
            is_decoded = True

        if not is_decoded:
            value["_unknown_extension"] = osspy.der.decode_undecoded_type(stream).hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, len(used_tag))

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        choice_type = Filter__9()
        return choice_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        is_checked = False
        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "and" in value:
            Filter__2.validate(value["and"], errors, "{}/{}".format(comp_path, "and"))
            is_checked = True
        if "or" in value:
            Filter__5.validate(value["or"], errors, "{}/{}".format(comp_path, "or"))
            is_checked = True
        if "not" in value:
            Filter__9.validate(value["not"], errors, "{}/{}".format(comp_path, "not"))
            is_checked = True
        if "equalityMatch" in value:
            Filter__10.validate(
                value["equalityMatch"], errors, "{}/{}".format(comp_path, "equalityMatch")
            )
            is_checked = True
        if "substrings" in value:
            Filter__11.validate(
                value["substrings"], errors, "{}/{}".format(comp_path, "substrings")
            )
            is_checked = True
        if "greaterOrEqual" in value:
            Filter__12.validate(
                value["greaterOrEqual"], errors, "{}/{}".format(comp_path, "greaterOrEqual")
            )
            is_checked = True
        if "lessOrEqual" in value:
            Filter__13.validate(
                value["lessOrEqual"], errors, "{}/{}".format(comp_path, "lessOrEqual")
            )
            is_checked = True
        if "present" in value:
            Filter__14.validate(value["present"], errors, "{}/{}".format(comp_path, "present"))
            is_checked = True
        if "approxMatch" in value:
            Filter__15.validate(
                value["approxMatch"], errors, "{}/{}".format(comp_path, "approxMatch")
            )
            is_checked = True
        if "extensibleMatch" in value:
            Filter__16.validate(
                value["extensibleMatch"], errors, "{}/{}".format(comp_path, "extensibleMatch")
            )
            is_checked = True

        if not is_checked and "_unknown_extension" not in value:
            report_empty_value(value, type(self).__name__, errors, comp_path)
        return errors


class Filter__10:
    def __init__(self):
        self._comp_types = {"attributeDesc": AssertionValue, "assertionValue": AssertionValue}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["attributeDesc", "assertionValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.equalityMatch"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Filter__10()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "attributeDesc" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["attributeDesc"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "assertionValue" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["assertionValue"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0xA3]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Filter__10()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA3]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "attributeDesc" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "assertionValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Filter__10()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "attributeDesc" in value:
            AssertionValue.validate(
                value["attributeDesc"], errors, "{}/{}".format(comp_path, "attributeDesc")
            )
        elif "attributeDesc" not in value:
            report_missing_field(type(self).__name__, "attributeDesc", errors, comp_path)
        if "assertionValue" in value:
            AssertionValue.validate(
                value["assertionValue"], errors, "{}/{}".format(comp_path, "assertionValue")
            )
        elif "assertionValue" not in value:
            report_missing_field(type(self).__name__, "assertionValue", errors, comp_path)

        return errors


class Filter__11:
    def __init__(self):
        self._comp_types = {"type": AssertionValue, "substrings": SubstringFilter__6}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["type"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.substrings"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Filter__11()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "type" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["type"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "substrings" in value:
            tmpstream.append(
                SubstringFilter__6.encode(
                    encoding_rule, value["substrings"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0xA4]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Filter__11()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA4]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "type" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["substrings"] = SubstringFilter__6.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Filter__11()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "type" in value:
            AssertionValue.validate(value["type"], errors, "{}/{}".format(comp_path, "type"))
        elif "type" not in value:
            report_missing_field(type(self).__name__, "type", errors, comp_path)
        if "substrings" in value:
            SubstringFilter__6.validate(
                value["substrings"], errors, "{}/{}".format(comp_path, "substrings")
            )
        elif "substrings" not in value:
            report_missing_field(type(self).__name__, "substrings", errors, comp_path)

        return errors


class Filter__12:
    def __init__(self):
        self._comp_types = {"attributeDesc": AssertionValue, "assertionValue": AssertionValue}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["attributeDesc", "assertionValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.greaterOrEqual"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Filter__12()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "attributeDesc" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["attributeDesc"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "assertionValue" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["assertionValue"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0xA5]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Filter__12()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA5]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "attributeDesc" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "assertionValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Filter__12()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "attributeDesc" in value:
            AssertionValue.validate(
                value["attributeDesc"], errors, "{}/{}".format(comp_path, "attributeDesc")
            )
        elif "attributeDesc" not in value:
            report_missing_field(type(self).__name__, "attributeDesc", errors, comp_path)
        if "assertionValue" in value:
            AssertionValue.validate(
                value["assertionValue"], errors, "{}/{}".format(comp_path, "assertionValue")
            )
        elif "assertionValue" not in value:
            report_missing_field(type(self).__name__, "assertionValue", errors, comp_path)

        return errors


class Filter__13:
    def __init__(self):
        self._comp_types = {"attributeDesc": AssertionValue, "assertionValue": AssertionValue}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["attributeDesc", "assertionValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.lessOrEqual"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Filter__13()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "attributeDesc" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["attributeDesc"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "assertionValue" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["assertionValue"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0xA6]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Filter__13()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA6]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "attributeDesc" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "assertionValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Filter__13()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "attributeDesc" in value:
            AssertionValue.validate(
                value["attributeDesc"], errors, "{}/{}".format(comp_path, "attributeDesc")
            )
        elif "attributeDesc" not in value:
            report_missing_field(type(self).__name__, "attributeDesc", errors, comp_path)
        if "assertionValue" in value:
            AssertionValue.validate(
                value["assertionValue"], errors, "{}/{}".format(comp_path, "assertionValue")
            )
        elif "assertionValue" not in value:
            report_missing_field(type(self).__name__, "assertionValue", errors, comp_path)

        return errors


class Filter__14:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.present"
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = Filter__14()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x87]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = Filter__14()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x87]]
        c_tag = [[0xA7]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = Filter__14()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


BindResponse_1__5 = Filter__14


class Filter__15:
    def __init__(self):
        self._comp_types = {"attributeDesc": AssertionValue, "assertionValue": AssertionValue}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["attributeDesc", "assertionValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.approxMatch"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Filter__15()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "attributeDesc" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["attributeDesc"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "assertionValue" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["assertionValue"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0xA8]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Filter__15()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA8]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "attributeDesc" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["attributeDesc"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "assertionValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["assertionValue"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Filter__15()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "attributeDesc" in value:
            AssertionValue.validate(
                value["attributeDesc"], errors, "{}/{}".format(comp_path, "attributeDesc")
            )
        elif "attributeDesc" not in value:
            report_missing_field(type(self).__name__, "attributeDesc", errors, comp_path)
        if "assertionValue" in value:
            AssertionValue.validate(
                value["assertionValue"], errors, "{}/{}".format(comp_path, "assertionValue")
            )
        elif "assertionValue" not in value:
            report_missing_field(type(self).__name__, "assertionValue", errors, comp_path)

        return errors


class Filter__16:
    def __init__(self):
        self._comp_types = {
            "matchingRule": ExtendedRequest__2,
            "type": MatchingRuleAssertion__2,
            "matchValue": MatchingRuleAssertion__3,
            "dnAttributes": MatchingRuleAssertion__4,
        }
        self._constraints = []
        self._def_vals = {"dnAttributes": False}
        self._frag_components = ["matchingRule", "type", "matchValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Filter.extensibleMatch"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = Filter__16()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "matchingRule" in value:
            tmpstream.append(
                ExtendedRequest__2.encode(
                    encoding_rule, value["matchingRule"], value_tracker, [[0x81]]
                ).get_buffer()
            )
        if "type" in value:
            tmpstream.append(
                MatchingRuleAssertion__2.encode(
                    encoding_rule, value["type"], value_tracker, [[0x82]]
                ).get_buffer()
            )
        if "matchValue" in value:
            tmpstream.append(
                MatchingRuleAssertion__3.encode(
                    encoding_rule, value["matchValue"], value_tracker, [[0x83]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "dnAttributes" in value and "dnAttributes" in self._def_vals:
            if not value_tracker.are_def_eq(
                value["dnAttributes"],
                self._def_vals["dnAttributes"],
                self._comp_types["dnAttributes"],
            ):
                tmpstream.append(
                    MatchingRuleAssertion__4.encode(
                        encoding_rule, value["dnAttributes"], value_tracker, [[0x84]]
                    ).get_buffer()
                )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0xA9]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = Filter__16()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0xA9]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchingRule"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA1], [0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchingRule"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0xA1], [0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchingRule" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA1]])[0]
        ):
            value["matchingRule"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x82]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0x82]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA2], [0x82]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0xA2], [0x82]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "type" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA2]])[0]
        ):
            value["type"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0x82]]
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x83]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchValue"] = MatchingRuleAssertion__3.decode(
                encoding_rule, stream, value_tracker, [[0x83]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3], [0x83]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchValue"] = MatchingRuleAssertion__3.decode(
                encoding_rule, stream, value_tracker, [[0xA3], [0x83]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA3]])[0]
        ):
            value["matchValue"] = MatchingRuleAssertion__3.decode(
                encoding_rule, stream, value_tracker, [[0x83]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x84]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["dnAttributes"] = MatchingRuleAssertion__4.decode(
                encoding_rule, stream, value_tracker, [[0x84]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA4], [0x84]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["dnAttributes"] = MatchingRuleAssertion__4.decode(
                encoding_rule, stream, value_tracker, [[0xA4], [0x84]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "dnAttributes" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA4]])[0]
        ):
            value["dnAttributes"] = MatchingRuleAssertion__4.decode(
                encoding_rule, stream, value_tracker, [[0x84]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = Filter__16()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "matchingRule" in value:
            ExtendedRequest__2.validate(
                value["matchingRule"], errors, "{}/{}".format(comp_path, "matchingRule")
            )
        if "type" in value:
            MatchingRuleAssertion__2.validate(
                value["type"], errors, "{}/{}".format(comp_path, "type")
            )
        if "matchValue" in value:
            MatchingRuleAssertion__3.validate(
                value["matchValue"], errors, "{}/{}".format(comp_path, "matchValue")
            )
        elif "matchValue" not in value:
            report_missing_field(type(self).__name__, "matchValue", errors, comp_path)
        if "dnAttributes" in value:
            MatchingRuleAssertion__4.validate(
                value["dnAttributes"], errors, "{}/{}".format(comp_path, "dnAttributes")
            )

        return errors


class SubstringFilter:
    def __init__(self):
        self._comp_types = {"type": AssertionValue, "substrings": SubstringFilter__6}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["type"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.SubstringFilter"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = SubstringFilter()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "type" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["type"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "substrings" in value:
            tmpstream.append(
                SubstringFilter__6.encode(
                    encoding_rule, value["substrings"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = SubstringFilter()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "type" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["type"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["substrings"] = SubstringFilter__6.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = SubstringFilter()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "type" in value:
            AssertionValue.validate(value["type"], errors, "{}/{}".format(comp_path, "type"))
        elif "type" not in value:
            report_missing_field(type(self).__name__, "type", errors, comp_path)
        if "substrings" in value:
            SubstringFilter__6.validate(
                value["substrings"], errors, "{}/{}".format(comp_path, "substrings")
            )
        elif "substrings" not in value:
            report_missing_field(type(self).__name__, "substrings", errors, comp_path)

        return errors


class SubstringFilter__6:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "size constraint", "permitted": [(1, float("inf"))]},
            }
        ]
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.SubstringFilter.substrings"
        )
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = SubstringFilter__6()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    SubstringFilter__5.encode(encoding_rule, val, value_tracker, []).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    SubstringFilter__5.encode(encoding_rule, val, value_tracker, []).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = SubstringFilter__6()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(
                    SubstringFilter__5.decode(encoding_rule, stream, value_tracker, [])
                )
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    SubstringFilter__5.decode(encoding_rule, stream, value_tracker, [])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = SubstringFilter__6()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                SubstringFilter__5.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class SubstringFilter__5:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.SubstringFilter.substrings.c"
        )
        self._asn1Type = Asn1Type.CHOICE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        choice_type = SubstringFilter__5()
        return choice_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        is_encoded = False

        if not isinstance(value, dict) or len(value.keys()) != 1:
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value)

        for identifier, alternative in value.items():
            if identifier == "initial":
                tmpstream.append(
                    AuthenticationChoice__1.encode(
                        encoding_rule, alternative, value_tracker, [[0x80]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "any":
                tmpstream.append(
                    ExtendedRequest__2.encode(
                        encoding_rule, alternative, value_tracker, [[0x81]]
                    ).get_buffer()
                )
                is_encoded = True
                break
            if identifier == "final":
                tmpstream.append(
                    MatchingRuleAssertion__2.encode(
                        encoding_rule, alternative, value_tracker, [[0x82]]
                    ).get_buffer()
                )
                is_encoded = True
                break

        if not is_encoded:
            if "_unknown_extension" in value:
                tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extension"]))
                is_encoded = True
            else:
                raise ValueError(
                    "62403: The choice alternative identifier is missing from the choice value!"
                )

        used_tag = []
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        choice_type = SubstringFilter__5()
        return choice_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = []
        is_decoded = False

        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, offset = osspy.der.peek_tags(stream, used_tag)
        if correct == 1:
            stream.skip_bytes(offset)

        if not is_decoded and (osspy.der.peek_tags(stream, [[0x80]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["initial"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0xA0]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["initial"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (osspy.der.peek_tags(stream, [[0x81]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["any"] = ExtendedRequest__2.decode(encoding_rule, stream, value_tracker, [[0x81]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0xA1]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["any"] = ExtendedRequest__2.decode(encoding_rule, stream, value_tracker, [[0x81]])
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        if not is_decoded and (osspy.der.peek_tags(stream, [[0x82]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["final"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0x82]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif not is_decoded and (osspy.der.peek_tags(stream, [[0xA2]])[0]):
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["final"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0x82]]
            )
            is_decoded = True
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)

        if not is_decoded:
            value["_unknown_extension"] = osspy.der.decode_undecoded_type(stream).hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, len(used_tag))

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        choice_type = SubstringFilter__5()
        return choice_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        is_checked = False
        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "initial" in value:
            AuthenticationChoice__1.validate(
                value["initial"], errors, "{}/{}".format(comp_path, "initial")
            )
            is_checked = True
        if "any" in value:
            ExtendedRequest__2.validate(value["any"], errors, "{}/{}".format(comp_path, "any"))
            is_checked = True
        if "final" in value:
            MatchingRuleAssertion__2.validate(
                value["final"], errors, "{}/{}".format(comp_path, "final")
            )
            is_checked = True

        if not is_checked and "_unknown_extension" not in value:
            report_empty_value(value, type(self).__name__, errors, comp_path)
        return errors


class MatchingRuleAssertion:
    def __init__(self):
        self._comp_types = {
            "matchingRule": ExtendedRequest__2,
            "type": MatchingRuleAssertion__2,
            "matchValue": MatchingRuleAssertion__3,
            "dnAttributes": MatchingRuleAssertion__4,
        }
        self._constraints = []
        self._def_vals = {"dnAttributes": False}
        self._frag_components = ["matchingRule", "type", "matchValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.MatchingRuleAssertion"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = MatchingRuleAssertion()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "matchingRule" in value:
            tmpstream.append(
                ExtendedRequest__2.encode(
                    encoding_rule, value["matchingRule"], value_tracker, [[0x81]]
                ).get_buffer()
            )
        if "type" in value:
            tmpstream.append(
                MatchingRuleAssertion__2.encode(
                    encoding_rule, value["type"], value_tracker, [[0x82]]
                ).get_buffer()
            )
        if "matchValue" in value:
            tmpstream.append(
                MatchingRuleAssertion__3.encode(
                    encoding_rule, value["matchValue"], value_tracker, [[0x83]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "dnAttributes" in value and "dnAttributes" in self._def_vals:
            if not value_tracker.are_def_eq(
                value["dnAttributes"],
                self._def_vals["dnAttributes"],
                self._comp_types["dnAttributes"],
            ):
                tmpstream.append(
                    MatchingRuleAssertion__4.encode(
                        encoding_rule, value["dnAttributes"], value_tracker, [[0x84]]
                    ).get_buffer()
                )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = MatchingRuleAssertion()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchingRule"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA1], [0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchingRule"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0xA1], [0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchingRule" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA1]])[0]
        ):
            value["matchingRule"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x82]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0x82]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA2], [0x82]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["type"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0xA2], [0x82]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "type" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA2]])[0]
        ):
            value["type"] = MatchingRuleAssertion__2.decode(
                encoding_rule, stream, value_tracker, [[0x82]]
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x83]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchValue"] = MatchingRuleAssertion__3.decode(
                encoding_rule, stream, value_tracker, [[0x83]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3], [0x83]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchValue"] = MatchingRuleAssertion__3.decode(
                encoding_rule, stream, value_tracker, [[0xA3], [0x83]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA3]])[0]
        ):
            value["matchValue"] = MatchingRuleAssertion__3.decode(
                encoding_rule, stream, value_tracker, [[0x83]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x84]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["dnAttributes"] = MatchingRuleAssertion__4.decode(
                encoding_rule, stream, value_tracker, [[0x84]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA4], [0x84]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["dnAttributes"] = MatchingRuleAssertion__4.decode(
                encoding_rule, stream, value_tracker, [[0xA4], [0x84]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "dnAttributes" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA4]])[0]
        ):
            value["dnAttributes"] = MatchingRuleAssertion__4.decode(
                encoding_rule, stream, value_tracker, [[0x84]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = MatchingRuleAssertion()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "matchingRule" in value:
            ExtendedRequest__2.validate(
                value["matchingRule"], errors, "{}/{}".format(comp_path, "matchingRule")
            )
        if "type" in value:
            MatchingRuleAssertion__2.validate(
                value["type"], errors, "{}/{}".format(comp_path, "type")
            )
        if "matchValue" in value:
            MatchingRuleAssertion__3.validate(
                value["matchValue"], errors, "{}/{}".format(comp_path, "matchValue")
            )
        elif "matchValue" not in value:
            report_missing_field(type(self).__name__, "matchValue", errors, comp_path)
        if "dnAttributes" in value:
            MatchingRuleAssertion__4.validate(
                value["dnAttributes"], errors, "{}/{}".format(comp_path, "dnAttributes")
            )

        return errors


class ExtendedRequest__2:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.ExtendedRequest.requestValue"
        )
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = ExtendedRequest__2()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x81]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = ExtendedRequest__2()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x81]]
        c_tag = [[0xA1]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = ExtendedRequest__2()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


IntermediateResponse__2 = ExtendedRequest__2
MatchingRuleAssertion__1 = ExtendedRequest__2
SubstringFilter__3 = ExtendedRequest__2


class MatchingRuleAssertion__2:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.MatchingRuleAssertion.type"
        )
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = MatchingRuleAssertion__2()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x82]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = MatchingRuleAssertion__2()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x82]]
        c_tag = [[0xA2]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = MatchingRuleAssertion__2()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


SubstringFilter__4 = MatchingRuleAssertion__2


class MatchingRuleAssertion__3:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.MatchingRuleAssertion.matchValue"
        )
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = MatchingRuleAssertion__3()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x83]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = MatchingRuleAssertion__3()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x83]]
        c_tag = [[0xA3]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = MatchingRuleAssertion__3()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class MatchingRuleAssertion__4:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.MatchingRuleAssertion.dnAttributes"
        )
        self._asn1Type = Asn1Type.BOOLEAN

    @staticmethod
    def encode(
        encoding_rule: str,
        value: bool,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = MatchingRuleAssertion__4()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: bool, tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x84]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_boolean(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> bool:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = MatchingRuleAssertion__4()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> bool:
        used_tag = [[0x84]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_boolean(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = MatchingRuleAssertion__4()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class SearchResultEntry:
    def __init__(self):
        self._comp_types = {"objectName": AssertionValue, "attributes": PartialAttributeList}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["objectName"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.SearchResultEntry"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = SearchResultEntry()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "objectName" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["objectName"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "attributes" in value:
            tmpstream.append(
                PartialAttributeList.encode(
                    encoding_rule, value["attributes"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x64]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = SearchResultEntry()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x64]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["objectName"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["objectName"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "objectName" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["objectName"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["attributes"] = PartialAttributeList.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = SearchResultEntry()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "objectName" in value:
            AssertionValue.validate(
                value["objectName"], errors, "{}/{}".format(comp_path, "objectName")
            )
        elif "objectName" not in value:
            report_missing_field(type(self).__name__, "objectName", errors, comp_path)
        if "attributes" in value:
            PartialAttributeList.validate(
                value["attributes"], errors, "{}/{}".format(comp_path, "attributes")
            )
        elif "attributes" not in value:
            report_missing_field(type(self).__name__, "attributes", errors, comp_path)

        return errors


class PartialAttributeList:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.PartialAttributeList"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = PartialAttributeList()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    PartialAttribute.encode(
                        encoding_rule, val, value_tracker, [[0x30]]
                    ).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    PartialAttribute.encode(
                        encoding_rule, val, value_tracker, [[0x30]]
                    ).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = PartialAttributeList()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(
                    PartialAttribute.decode(encoding_rule, stream, value_tracker, [[0x30]])
                )
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    PartialAttribute.decode(encoding_rule, stream, value_tracker, [[0x30]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = PartialAttributeList()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                PartialAttribute.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class SearchResultReference:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "size constraint", "permitted": [(1, float("inf"))]},
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.SearchResultReference"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = SearchResultReference()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x73]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = SearchResultReference()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x73]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                if is_indefinite and osspy.der.is_eoc(stream):
                    osspy.der.skip_eoc(stream, 1)
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = SearchResultReference()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                AssertionValue.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class SearchResultDone:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.SearchResultDone"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = SearchResultDone()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x65]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = SearchResultDone()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x65]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = SearchResultDone()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))

        return errors


class ModifyRequest:
    def __init__(self):
        self._comp_types = {"object": AssertionValue, "changes": ModifyRequest__5}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["object"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ModifyRequest"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = ModifyRequest()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "object" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["object"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "changes" in value:
            tmpstream.append(
                ModifyRequest__5.encode(
                    encoding_rule, value["changes"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x66]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = ModifyRequest()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x66]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["object"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["object"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "object" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["object"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["changes"] = ModifyRequest__5.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = ModifyRequest()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "object" in value:
            AssertionValue.validate(value["object"], errors, "{}/{}".format(comp_path, "object"))
        elif "object" not in value:
            report_missing_field(type(self).__name__, "object", errors, comp_path)
        if "changes" in value:
            ModifyRequest__5.validate(
                value["changes"], errors, "{}/{}".format(comp_path, "changes")
            )
        elif "changes" not in value:
            report_missing_field(type(self).__name__, "changes", errors, comp_path)

        return errors


class ModifyRequest__5:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ModifyRequest.changes"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = ModifyRequest__5()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    ModifyRequest__4.encode(
                        encoding_rule, val, value_tracker, [[0x30]]
                    ).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    ModifyRequest__4.encode(
                        encoding_rule, val, value_tracker, [[0x30]]
                    ).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = ModifyRequest__5()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(
                    ModifyRequest__4.decode(encoding_rule, stream, value_tracker, [[0x30]])
                )
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    ModifyRequest__4.decode(encoding_rule, stream, value_tracker, [[0x30]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = ModifyRequest__5()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                ModifyRequest__4.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class ModifyRequest__4:
    def __init__(self):
        self._comp_types = {"operation": ModifyRequest__2, "modification": PartialAttribute}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ModifyRequest.changes.c"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = ModifyRequest__4()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "operation" in value:
            tmpstream.append(
                ModifyRequest__2.encode(
                    encoding_rule, value["operation"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "modification" in value:
            tmpstream.append(
                PartialAttribute.encode(
                    encoding_rule, value["modification"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = ModifyRequest__4()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["operation"] = ModifyRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["operation"] = ModifyRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "operation" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["operation"] = ModifyRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["modification"] = PartialAttribute.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = ModifyRequest__4()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "operation" in value:
            ModifyRequest__2.validate(
                value["operation"], errors, "{}/{}".format(comp_path, "operation")
            )
        elif "operation" not in value:
            report_missing_field(type(self).__name__, "operation", errors, comp_path)
        if "modification" in value:
            PartialAttribute.validate(
                value["modification"], errors, "{}/{}".format(comp_path, "modification")
            )
        elif "modification" not in value:
            report_missing_field(type(self).__name__, "modification", errors, comp_path)

        return errors


class ModifyRequest__2:
    def __init__(self):
        self._constraints = []
        self._identifiers = {"add": 0, "delete": 1, "replace": 2}
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.ModifyRequest.changes.c.operation"
        )
        self._asn1Type = Asn1Type.ENUMERATED

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, int],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        enum_type = ModifyRequest__2()
        return enum_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: Union[str, int], tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        if not isinstance(value, int) and not isinstance(value, str):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        int_val = None
        if isinstance(value, int) and value in self._identifiers.values():
            int_val = value

        if value in self._identifiers:
            int_val = self._identifiers[value]

        if int_val is None and isinstance(value, int):
            int_val = value

        if int_val is None:
            raise ValueError(
                "62603: The enumeration item identifier is missing from the enumerated value!"
            )

        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag
        osspy.der.encode_integer(stream, int_val, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, int]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        enum_type = ModifyRequest__2()
        return enum_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> Union[str, int]:
        used_tag = [[0x0A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_integer(stream, used_tag)

        identifier = None
        for item in self._identifiers:
            if self._identifiers[item] == value:
                identifier = item

        if identifier is not None:
            return identifier

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        enum_type = ModifyRequest__2()
        return enum_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        if isinstance(value, int) and value not in self._identifiers.keys():
            report_extra_field(
                value, type(self).__name__, value, errors, comp_path, list(self._identifiers.keys())
            )
        return errors


class ModifyResponse:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ModifyResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = ModifyResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x67]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = ModifyResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x67]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = ModifyResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))

        return errors


class AddRequest:
    def __init__(self):
        self._comp_types = {"entry": AssertionValue, "attributes": AttributeList}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["entry"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AddRequest"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = AddRequest()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "entry" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["entry"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "attributes" in value:
            tmpstream.append(
                AttributeList.encode(
                    encoding_rule, value["attributes"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x68]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = AddRequest()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x68]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["entry"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["entry"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "entry" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["entry"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["attributes"] = AttributeList.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = AddRequest()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "entry" in value:
            AssertionValue.validate(value["entry"], errors, "{}/{}".format(comp_path, "entry"))
        elif "entry" not in value:
            report_missing_field(type(self).__name__, "entry", errors, comp_path)
        if "attributes" in value:
            AttributeList.validate(
                value["attributes"], errors, "{}/{}".format(comp_path, "attributes")
            )
        elif "attributes" not in value:
            report_missing_field(type(self).__name__, "attributes", errors, comp_path)

        return errors


class AttributeList:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AttributeList"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = AttributeList()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = False
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    Attribute.encode(encoding_rule, val, value_tracker, [[0x30]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    Attribute.encode(encoding_rule, val, value_tracker, [[0x30]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x30]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = AttributeList()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x30]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                components.append(Attribute.decode(encoding_rule, stream, value_tracker, [[0x30]]))
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(Attribute.decode(encoding_rule, stream, value_tracker, [[0x30]]))
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = AttributeList()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                Attribute.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors


class AddResponse:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AddResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = AddResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x69]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = AddResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x69]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = AddResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))

        return errors


class DelRequest:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.DelRequest"
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = DelRequest()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x4A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = DelRequest()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x4A]]
        c_tag = [[0x6A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = DelRequest()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class DelResponse:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.DelResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = DelResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x6B]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = DelResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x6B]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = DelResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))

        return errors


class ModifyDNRequest:
    def __init__(self):
        self._comp_types = {
            "entry": AssertionValue,
            "newrdn": AssertionValue,
            "deleteoldrdn": Control__2,
            "newSuperior": AuthenticationChoice__1,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["entry", "newrdn", "newSuperior"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ModifyDNRequest"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = ModifyDNRequest()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "entry" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["entry"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "newrdn" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["newrdn"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "deleteoldrdn" in value:
            tmpstream.append(
                Control__2.encode(
                    encoding_rule, value["deleteoldrdn"], value_tracker, [[0x01]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "newSuperior" in value:
            tmpstream.append(
                AuthenticationChoice__1.encode(
                    encoding_rule, value["newSuperior"], value_tracker, [[0x80]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x6C]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = ModifyDNRequest()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x6C]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["entry"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["entry"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "entry" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["entry"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["newrdn"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["newrdn"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "newrdn" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["newrdn"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x01]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["deleteoldrdn"] = Control__2.decode(
                encoding_rule, stream, value_tracker, [[0x01]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x21], [0x01]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["deleteoldrdn"] = Control__2.decode(
                encoding_rule, stream, value_tracker, [[0x21], [0x01]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "deleteoldrdn" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x21]])[0]
        ):
            value["deleteoldrdn"] = Control__2.decode(
                encoding_rule, stream, value_tracker, [[0x01]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x80]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["newSuperior"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA0], [0x80]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["newSuperior"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0xA0], [0x80]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "newSuperior" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA0]])[0]
        ):
            value["newSuperior"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = ModifyDNRequest()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "entry" in value:
            AssertionValue.validate(value["entry"], errors, "{}/{}".format(comp_path, "entry"))
        elif "entry" not in value:
            report_missing_field(type(self).__name__, "entry", errors, comp_path)
        if "newrdn" in value:
            AssertionValue.validate(value["newrdn"], errors, "{}/{}".format(comp_path, "newrdn"))
        elif "newrdn" not in value:
            report_missing_field(type(self).__name__, "newrdn", errors, comp_path)
        if "deleteoldrdn" in value:
            Control__2.validate(
                value["deleteoldrdn"], errors, "{}/{}".format(comp_path, "deleteoldrdn")
            )
        elif "deleteoldrdn" not in value:
            report_missing_field(type(self).__name__, "deleteoldrdn", errors, comp_path)
        if "newSuperior" in value:
            AuthenticationChoice__1.validate(
                value["newSuperior"], errors, "{}/{}".format(comp_path, "newSuperior")
            )

        return errors


class Control__2:
    def __init__(self):
        self._constraints = []
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.Control.criticality"
        self._asn1Type = Asn1Type.BOOLEAN

    @staticmethod
    def encode(
        encoding_rule: str,
        value: bool,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = Control__2()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: bool, tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x01]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_boolean(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> bool:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = Control__2()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> bool:
        used_tag = [[0x01]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_boolean(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = Control__2()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


ModifyDNRequest__3 = Control__2
SearchRequest__8 = Control__2


class AuthenticationChoice__1:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.AuthenticationChoice.simple"
        )
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = AuthenticationChoice__1()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x80]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = AuthenticationChoice__1()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x80]]
        c_tag = [[0xA0]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = AuthenticationChoice__1()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


ExtendedRequest__1 = AuthenticationChoice__1
IntermediateResponse__1 = AuthenticationChoice__1
ModifyDNRequest__4 = AuthenticationChoice__1
SubstringFilter__2 = AuthenticationChoice__1


class ModifyDNResponse:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ModifyDNResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = ModifyDNResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x6D]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = ModifyDNResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x6D]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = ModifyDNResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))

        return errors


class CompareRequest:
    def __init__(self):
        self._comp_types = {"entry": AssertionValue, "ava": AttributeValueAssertion}
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["entry"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.CompareRequest"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = CompareRequest()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "entry" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["entry"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "ava" in value:
            tmpstream.append(
                AttributeValueAssertion.encode(
                    encoding_rule, value["ava"], value_tracker, [[0x30]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x6E]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = CompareRequest()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x6E]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["entry"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["entry"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "entry" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["entry"] = AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x30]])[0]:
            value["ava"] = AttributeValueAssertion.decode(
                encoding_rule, stream, value_tracker, [[0x30]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = CompareRequest()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "entry" in value:
            AssertionValue.validate(value["entry"], errors, "{}/{}".format(comp_path, "entry"))
        elif "entry" not in value:
            report_missing_field(type(self).__name__, "entry", errors, comp_path)
        if "ava" in value:
            AttributeValueAssertion.validate(value["ava"], errors, "{}/{}".format(comp_path, "ava"))
        elif "ava" not in value:
            report_missing_field(type(self).__name__, "ava", errors, comp_path)

        return errors


class CompareResponse:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.CompareResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = CompareResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x6F]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = CompareResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x6F]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = CompareResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))

        return errors


class AbandonRequest:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {
                    "type": "value range",
                    "definition": "0 ..  maxInt",
                    "permitted": [(0, 2147483647)],
                },
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.AbandonRequest"
        self._asn1Type = Asn1Type.INTEGER

    @staticmethod
    def encode(
        encoding_rule: str,
        value: int,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        simple_type = AbandonRequest()
        return simple_type.encode_value(value, tag, stream)

    def encode_value(
        self, value: int, tag: list, stream: osspy.der.encodingstream
    ) -> osspy.der.encodingstream:
        used_tag = [[0x50]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_integer(stream, value, used_tag)
        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker_: dict, tag: list = None
    ) -> int:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        simple_type = AbandonRequest()
        return simple_type.decode_value(stream, tag)

    def decode_value(self, stream: osspy.der.decodingstream, tag: list) -> int:
        used_tag = [[0x50]]
        c_tag = None
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        return osspy.der.decode_integer(stream, used_tag, c_tag)

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        simple_type = AbandonRequest()
        return simple_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class ExtendedRequest:
    def __init__(self):
        self._comp_types = {
            "requestName": AuthenticationChoice__1,
            "requestValue": ExtendedRequest__2,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["requestName", "requestValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ExtendedRequest"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = ExtendedRequest()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "requestName" in value:
            tmpstream.append(
                AuthenticationChoice__1.encode(
                    encoding_rule, value["requestName"], value_tracker, [[0x80]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "requestValue" in value:
            tmpstream.append(
                ExtendedRequest__2.encode(
                    encoding_rule, value["requestValue"], value_tracker, [[0x81]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x77]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = ExtendedRequest()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x77]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x80]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["requestName"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA0], [0x80]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["requestName"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0xA0], [0x80]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "requestName" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA0]])[0]
        ):
            value["requestName"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["requestValue"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA1], [0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["requestValue"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0xA1], [0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "requestValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA1]])[0]
        ):
            value["requestValue"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = ExtendedRequest()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "requestName" in value:
            AuthenticationChoice__1.validate(
                value["requestName"], errors, "{}/{}".format(comp_path, "requestName")
            )
        elif "requestName" not in value:
            report_missing_field(type(self).__name__, "requestName", errors, comp_path)
        if "requestValue" in value:
            ExtendedRequest__2.validate(
                value["requestValue"], errors, "{}/{}".format(comp_path, "requestValue")
            )

        return errors


class ExtendedResponse:
    def __init__(self):
        self._comp_types = {
            "resultCode": LDAPResult__1,
            "matchedDN": AssertionValue,
            "diagnosticMessage": AssertionValue,
            "referral": LDAPResult__4,
            "responseName": ExtendedResponse_1__5,
            "responseValue": ExtendedResponse_1__6,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["matchedDN", "diagnosticMessage", "responseName", "responseValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.ExtendedResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = ExtendedResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "resultCode" in value:
            tmpstream.append(
                LDAPResult__1.encode(
                    encoding_rule, value["resultCode"], value_tracker, [[0x0A]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "matchedDN" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["matchedDN"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "diagnosticMessage" in value:
            tmpstream.append(
                AssertionValue.encode(
                    encoding_rule, value["diagnosticMessage"], value_tracker, [[0x04]]
                ).get_buffer()
            )
        else:
            raise ValueError(
                "63803: A mandatory component is missing from the sequence or set value!"
            )
        if "referral" in value:
            tmpstream.append(
                LDAPResult__4.encode(
                    encoding_rule, value["referral"], value_tracker, [[0xA3]]
                ).get_buffer()
            )
        if "responseName" in value:
            tmpstream.append(
                ExtendedResponse_1__5.encode(
                    encoding_rule, value["responseName"], value_tracker, [[0x8A]]
                ).get_buffer()
            )
        if "responseValue" in value:
            tmpstream.append(
                ExtendedResponse_1__6.encode(
                    encoding_rule, value["responseValue"], value_tracker, [[0x8B]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x78]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = ExtendedResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x78]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x2A], [0x0A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x2A], [0x0A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "resultCode" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x2A]])[0]
        ):
            value["resultCode"] = LDAPResult__1.decode(
                encoding_rule, stream, value_tracker, [[0x0A]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "matchedDN" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["matchedDN"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x24], [0x04]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x24], [0x04]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "diagnosticMessage" in self._frag_components
            and osspy.der.peek_tags(stream, [[0x24]])[0]
        ):
            value["diagnosticMessage"] = AssertionValue.decode(
                encoding_rule, stream, value_tracker, [[0x04]]
            )
        else:
            value_tracker.remove_ancestor()
            raise ValueError(
                "63805: A mandatory component of the sequence or set type is missing from the encoded data!"
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA3]])[0]:
            value["referral"] = LDAPResult__4.decode(encoding_rule, stream, value_tracker, [[0xA3]])
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x8A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseName"] = ExtendedResponse_1__5.decode(
                encoding_rule, stream, value_tracker, [[0x8A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xAA], [0x8A]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseName"] = ExtendedResponse_1__5.decode(
                encoding_rule, stream, value_tracker, [[0xAA], [0x8A]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "responseName" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xAA]])[0]
        ):
            value["responseName"] = ExtendedResponse_1__5.decode(
                encoding_rule, stream, value_tracker, [[0x8A]]
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x8B]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseValue"] = ExtendedResponse_1__6.decode(
                encoding_rule, stream, value_tracker, [[0x8B]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xAB], [0x8B]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseValue"] = ExtendedResponse_1__6.decode(
                encoding_rule, stream, value_tracker, [[0xAB], [0x8B]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "responseValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xAB]])[0]
        ):
            value["responseValue"] = ExtendedResponse_1__6.decode(
                encoding_rule, stream, value_tracker, [[0x8B]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = ExtendedResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "resultCode" in value:
            LDAPResult__1.validate(
                value["resultCode"], errors, "{}/{}".format(comp_path, "resultCode")
            )
        elif "resultCode" not in value:
            report_missing_field(type(self).__name__, "resultCode", errors, comp_path)
        if "matchedDN" in value:
            AssertionValue.validate(
                value["matchedDN"], errors, "{}/{}".format(comp_path, "matchedDN")
            )
        elif "matchedDN" not in value:
            report_missing_field(type(self).__name__, "matchedDN", errors, comp_path)
        if "diagnosticMessage" in value:
            AssertionValue.validate(
                value["diagnosticMessage"], errors, "{}/{}".format(comp_path, "diagnosticMessage")
            )
        elif "diagnosticMessage" not in value:
            report_missing_field(type(self).__name__, "diagnosticMessage", errors, comp_path)
        if "referral" in value:
            LDAPResult__4.validate(value["referral"], errors, "{}/{}".format(comp_path, "referral"))
        if "responseName" in value:
            ExtendedResponse_1__5.validate(
                value["responseName"], errors, "{}/{}".format(comp_path, "responseName")
            )
        if "responseValue" in value:
            ExtendedResponse_1__6.validate(
                value["responseValue"], errors, "{}/{}".format(comp_path, "responseValue")
            )

        return errors


class ExtendedResponse_1__5:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.ExtendedResponse-1.responseName"
        )
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = ExtendedResponse_1__5()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x8A]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = ExtendedResponse_1__5()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x8A]]
        c_tag = [[0xAA]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = ExtendedResponse_1__5()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class ExtendedResponse_1__6:
    def __init__(self):
        self._constraints = []
        self._contents_constrait = None
        self._unique_indetifier = (
            "Lightweight-Directory-Access-Protocol-V3.ExtendedResponse-1.responseValue"
        )
        self._asn1Type = Asn1Type.OCTET_STRING

    def get_containing_constraint(self):
        for constraint in self._constraints:
            if constraint.get("type") == "contents constraint":
                return constraint
        return None

    @staticmethod
    def encode(
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        octetstring_type = ExtendedResponse_1__6()
        return octetstring_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: Union[str, dict],
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        if not isinstance(value, str) and not isinstance(value, dict):
            raise ValueError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        constraint = self._contents_constrait
        bin_val = None
        if constraint is not None and isinstance(value, dict) and "containing" in value:
            func = getattr(constraint, "encode")
            bin_val = func(encoding_rule, value["containing"], value_tracker, []).get_buffer()
        else:
            try:
                bin_val = bytearray.fromhex(value)
            except Exception as exc:
                raise TypeError(
                    "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
                ) from exc

        if bin_val is None:
            raise TypeError("63305: The 'plain octets' are missing from the octet string value!")

        used_tag = [[0x8B]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        osspy.der.encode_octet_string(stream, bin_val, used_tag)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> Union[str, dict]:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        octetstring_type = ExtendedResponse_1__6()
        return octetstring_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> Union[str, dict]:
        used_tag = [[0x8B]]
        c_tag = [[0xAB]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value = osspy.der.decode_octet_string(stream, used_tag, c_tag)

        constraint = self._contents_constrait
        if constraint is not None:
            func = getattr(constraint, "decode")
            bin_val = bytearray.fromhex(value)
            tmpstream = osspy.der.decodingstream(bin_val, encoding_rule)
            try:
                valcontaining = {}
                current_depth = value_tracker.depth
                valcontaining["containing"] = func(encoding_rule, tmpstream, value_tracker, [])
                if tmpstream.is_eof():
                    value = valcontaining
            except Exception as _exc:  # pylint: disable=broad-except
                warn("63302: The value contained in the octet string value could not be decoded!")
                value_tracker.depth = current_depth

        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        octetstring_type = ExtendedResponse_1__6()
        return octetstring_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)

        return errors


class IntermediateResponse:
    def __init__(self):
        self._comp_types = {
            "responseName": AuthenticationChoice__1,
            "responseValue": ExtendedRequest__2,
        }
        self._constraints = []
        self._def_vals = {}
        self._frag_components = ["responseName", "responseValue"]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.IntermediateResponse"
        self._asn1Type = Asn1Type.SEQUENCE

    @staticmethod
    def encode(
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seq_type = IntermediateResponse()
        return seq_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: object,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)

        if not isinstance(value, object):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map = {}
        data_map["encoding_form"] = "constructed"

        value_tracker.add_ancestor(value, self._def_vals)

        if "responseName" in value:
            tmpstream.append(
                AuthenticationChoice__1.encode(
                    encoding_rule, value["responseName"], value_tracker, [[0x80]]
                ).get_buffer()
            )
        if "responseValue" in value:
            tmpstream.append(
                ExtendedRequest__2.encode(
                    encoding_rule, value["responseValue"], value_tracker, [[0x81]]
                ).get_buffer()
            )
        if "_unknown_extensions" in value:
            tmpstream.append(osspy.der.encode_unknown_extensions(value["_unknown_extensions"]))

        used_tag = [[0x79]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        value_tracker.remove_ancestor()

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> dict:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seq_type = IntermediateResponse()
        return seq_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> dict:
        value = {}
        used_tag = [[0x79]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        value_tracker.add_ancestor(value)

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            value_tracker.remove_ancestor()
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )
        start_pos = stream.get_pos()

        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x80]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseName"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA0], [0x80]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseName"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0xA0], [0x80]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "responseName" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA0]])[0]
        ):
            value["responseName"] = AuthenticationChoice__1.decode(
                encoding_rule, stream, value_tracker, [[0x80]]
            )
        if (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseValue"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            stream.get_pos() < start_pos + length
            or (length < 0 and not osspy.der.is_eoc(stream, length))
        ) and osspy.der.peek_tags(stream, [[0xA1], [0x81]])[0]:
            is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
            value["responseValue"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0xA1], [0x81]]
            )
            if is_indefinite and osspy.der.is_eoc(stream):
                osspy.der.skip_eoc(stream, 1)
        elif (
            (
                stream.get_pos() < start_pos + length
                or (length < 0 and not osspy.der.is_eoc(stream, length))
            )
            and "responseValue" in self._frag_components
            and osspy.der.peek_tags(stream, [[0xA1]])[0]
        ):
            value["responseValue"] = ExtendedRequest__2.decode(
                encoding_rule, stream, value_tracker, [[0x81]]
            )
        if stream.get_pos() < start_pos + length or (
            length < 0 and not osspy.der.is_eoc(stream, length)
        ):
            position = stream.get_pos()
            while position < (start_pos + length) or (
                length < 0 and not osspy.der.is_eoc(stream, length)
            ):
                octets = osspy.der.decode_undecoded_type(stream)
                position = position + len(octets)

                if len(octets) > 0:
                    if "_unknown_extensions" not in value:
                        value["_unknown_extensions"] = ""
                    value["_unknown_extensions"] += octets.hex().upper()

        if length < 0 and osspy.der.is_eoc(stream):
            osspy.der.skip_eoc(stream, num_indefs)

        if len(self._def_vals) > 0:
            for key, val in self._def_vals.items():
                if key not in value:
                    value[key] = val

        value = value_tracker.execute_deferred(value)
        return value

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seq_type = IntermediateResponse()
        return seq_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value: dict, errors: list, comp_path: str) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if not isinstance(value, dict):
            report_empty_value(value, type(self).__name__, errors, comp_path)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if "responseName" in value:
            AuthenticationChoice__1.validate(
                value["responseName"], errors, "{}/{}".format(comp_path, "responseName")
            )
        if "responseValue" in value:
            ExtendedRequest__2.validate(
                value["responseValue"], errors, "{}/{}".format(comp_path, "responseValue")
            )

        return errors


class PartialAttribute_1__2:
    def __init__(self):
        self._constraints = [
            {
                "type": "subtype constraint",
                "root expression": {"type": "size constraint", "permitted": [(1, float("inf"))]},
            }
        ]
        self._unique_indetifier = "Lightweight-Directory-Access-Protocol-V3.PartialAttribute-1.vals"
        self._asn1Type = Asn1Type.SEQUENCE_OF

    @staticmethod
    def encode(
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list = None,
        stream: osspy.der.encodingstream = None,
    ) -> osspy.der.encodingstream:
        if not isinstance(stream, osspy.der.encodingstream):
            stream = osspy.der.encodingstream(encoding_rule)

        seqof_type = PartialAttribute_1__2()
        return seqof_type.encode_value(encoding_rule, value, value_tracker, tag, stream)

    def encode_value(
        self,
        encoding_rule: str,
        value: list,
        value_tracker: dict,
        tag: list,
        stream: osspy.der.encodingstream,
    ) -> osspy.der.encodingstream:
        tmpstream = osspy.der.encodingstream(encoding_rule)
        data_map = {}

        if not isinstance(value, list):
            raise TypeError(
                "65201: The value class containing the value to be encoded does not match the type specified in the schema!"
            )

        data_map["is_setof_type"] = True
        data_map["encoding_form"] = "constructed"

        if data_map["is_setof_type"] and stream.canonical:
            enc_list = []
            for val in value:
                value_tracker.add_ancestor(val)
                enc_list.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()
            enc_list = sorted(enc_list)
            for enc_item in enc_list:
                tmpstream.append(enc_item)
        else:
            for val in value:
                value_tracker.add_ancestor(val)
                tmpstream.append(
                    AssertionValue.encode(encoding_rule, val, value_tracker, [[0x04]]).get_buffer()
                )
                value_tracker.remove_ancestor()

        used_tag = [[0x31]]
        if tag is None:
            tag = []
        elif len(tag) > 0:
            used_tag = tag

        buffer = tmpstream.get_buffer()
        if stream.canonical:
            osspy.der.encode_tags_lens(stream.buffer, used_tag, len(buffer))
        else:
            osspy.der.encode_tags_lens_ber(
                stream.buffer, used_tag, buffer, data_map["encoding_form"]
            )
        stream.append(buffer)

        return stream

    @staticmethod
    def decode(
        encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list = None
    ) -> list:
        if not isinstance(stream, osspy.der.decodingstream):
            stream = osspy.der.decodingstream(stream, encoding_rule)

        seqof_type = PartialAttribute_1__2()
        return seqof_type.decode_value(encoding_rule, stream, value_tracker, tag)

    def decode_value(
        self, encoding_rule: str, stream: osspy.der.decodingstream, value_tracker: dict, tag: list
    ) -> list:
        components = []
        used_tag = [[0x31]]
        if tag is None:
            tag = []
        if len(tag) > 0:
            used_tag = tag
        idx = 0

        correct, length, num_indefs = osspy.der.decode_tags(stream, used_tag)
        if correct == 0:
            raise ValueError(
                "70003: The next tag present in the encoding does not match the tag of the type to be decoded!"
            )

        position = stream.get_pos()
        if length == -1:
            while not osspy.der.is_eoc(stream) and not stream.is_eof():
                value_tracker.add_ancestor(idx)
                is_indefinite = osspy.der.is_indefinite(stream, stream.get_pos())
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                if is_indefinite and osspy.der.is_eoc(stream):
                    osspy.der.skip_eoc(stream, 1)
                value_tracker.remove_ancestor()
                idx += 1
            osspy.der.skip_eoc(stream, num_indefs)
        else:
            while stream.get_pos() < position + length:
                value_tracker.add_ancestor(idx)
                components.append(
                    AssertionValue.decode(encoding_rule, stream, value_tracker, [[0x04]])
                )
                value_tracker.remove_ancestor()
                idx += 1

        return components

    @staticmethod
    def validate(value, errors: list, comp_path: str = "") -> list:
        seqof_type = PartialAttribute_1__2()
        return seqof_type.validate_instance(value, errors, comp_path)

    def validate_instance(self, value, errors: list, comp_path) -> list:
        validate_value_type(value, comp_path, errors, self._asn1Type)

        if len(self._constraints) > 0:
            validate_value(value, self._constraints, comp_path, errors)
        if isinstance(value, list):
            for idx, val in enumerate(value):
                AssertionValue.validate(val, errors, "{}/{}".format(comp_path, idx))

        return errors
