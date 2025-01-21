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

from __future__ import annotations
from typing import Union, Optional

from .private.osspy_bindings import (
    InvalidTypeParameter,
    OSS_Boolean,
    OSS_Integer,
    OSS_OctetString,
    OSS_Sequence,
    OSS_SequenceOf,
    OSS_Choice,
    OSS_Enum,
    OSS_NullType,
    OSS_Null,
)


class LDAPMessage(OSS_Sequence):
    class ProtocolOp(OSS_Choice):
        @classmethod
        def _field_map(cls):
            return {
                "bindRequest": BindRequest,
                "bindResponse": BindResponse,
                "unbindRequest": OSS_NullType,
                "searchRequest": SearchRequest,
                "searchResEntry": SearchResultEntry,
                "searchResDone": SearchResultDone,
                "searchResRef": SearchResultReference,
                "modifyRequest": ModifyRequest,
                "modifyResponse": ModifyResponse,
                "addRequest": AddRequest,
                "addResponse": AddResponse,
                "delRequest": DelRequest,
                "delResponse": DelResponse,
                "modDNRequest": ModifyDNRequest,
                "modDNResponse": ModifyDNResponse,
                "compareRequest": CompareRequest,
                "compareResponse": CompareResponse,
                "abandonRequest": AbandonRequest,
                "extendedReq": ExtendedRequest,
                "extendedResp": ExtendedResponse,
                "intermediateResponse": IntermediateResponse,
            }

        @property
        def bindRequest(self) -> Union[BindRequest, None]:
            """Get the value of the 'bindRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.bindRequest
            """
            return self._value.get("bindRequest")

        @bindRequest.setter
        def bindRequest(self, val: BindRequest):
            """Set the value of the 'bindRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.bindRequest = BindRequest()
            """
            if not isinstance(val, (self._fields["bindRequest"],)):
                raise InvalidTypeParameter((self._fields["bindRequest"],))
            self._value.clear()
            self._value["bindRequest"] = val

        @property
        def bindResponse(self) -> Union[BindResponse, None]:
            """Get the value of the 'bindResponse' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.bindResponse
            """
            return self._value.get("bindResponse")

        @bindResponse.setter
        def bindResponse(self, val: BindResponse):
            """Set the value of the 'bindResponse' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.bindResponse = BindResponse()
            """
            if not isinstance(val, (self._fields["bindResponse"],)):
                raise InvalidTypeParameter((self._fields["bindResponse"],))
            self._value.clear()
            self._value["bindResponse"] = val

        @property
        def unbindRequest(self) -> Union[UnbindRequest, None]:
            """Get the value of the 'unbindRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.unbindRequest
            """
            return self._value.get("unbindRequest")

        @unbindRequest.setter
        def unbindRequest(self, val: UnbindRequest):
            """Set the value of the 'unbindRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.unbindRequest = UnbindRequest()
            """
            if not isinstance(val, (self._fields["unbindRequest"],)):
                raise InvalidTypeParameter((self._fields["unbindRequest"],))
            self._value.clear()
            self._value["unbindRequest"] = val

        @property
        def searchRequest(self) -> Union[SearchRequest, None]:
            """Get the value of the 'searchRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.searchRequest
            """
            return self._value.get("searchRequest")

        @searchRequest.setter
        def searchRequest(self, val: SearchRequest):
            """Set the value of the 'searchRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.searchRequest = SearchRequest()
            """
            if not isinstance(val, (self._fields["searchRequest"],)):
                raise InvalidTypeParameter((self._fields["searchRequest"],))
            self._value.clear()
            self._value["searchRequest"] = val

        @property
        def searchResEntry(self) -> Union[SearchResultEntry, None]:
            """Get the value of the 'searchResEntry' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.searchResEntry
            """
            return self._value.get("searchResEntry")

        @searchResEntry.setter
        def searchResEntry(self, val: SearchResultEntry):
            """Set the value of the 'searchResEntry' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.searchResEntry = SearchResultEntry()
            """
            if not isinstance(val, (self._fields["searchResEntry"],)):
                raise InvalidTypeParameter((self._fields["searchResEntry"],))
            self._value.clear()
            self._value["searchResEntry"] = val

        @property
        def searchResDone(self) -> Union[SearchResultDone, None]:
            """Get the value of the 'searchResDone' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.searchResDone
            """
            return self._value.get("searchResDone")

        @searchResDone.setter
        def searchResDone(self, val: SearchResultDone):
            """Set the value of the 'searchResDone' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.searchResDone = SearchResultDone()
            """
            if not isinstance(val, (self._fields["searchResDone"],)):
                raise InvalidTypeParameter((self._fields["searchResDone"],))
            self._value.clear()
            self._value["searchResDone"] = val

        @property
        def searchResRef(self) -> Union[SearchResultReference, None]:
            """Get the value of the 'searchResRef' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.searchResRef
            """
            return self._value.get("searchResRef")

        @searchResRef.setter
        def searchResRef(self, val: SearchResultReference):
            """Set the value of the 'searchResRef' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.searchResRef = SearchResultReference()
            """
            if not isinstance(val, (self._fields["searchResRef"],)):
                raise InvalidTypeParameter((self._fields["searchResRef"],))
            self._value.clear()
            self._value["searchResRef"] = val

        @property
        def modifyRequest(self) -> Union[ModifyRequest, None]:
            """Get the value of the 'modifyRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.modifyRequest
            """
            return self._value.get("modifyRequest")

        @modifyRequest.setter
        def modifyRequest(self, val: ModifyRequest):
            """Set the value of the 'modifyRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.modifyRequest = ModifyRequest()
            """
            if not isinstance(val, (self._fields["modifyRequest"],)):
                raise InvalidTypeParameter((self._fields["modifyRequest"],))
            self._value.clear()
            self._value["modifyRequest"] = val

        @property
        def modifyResponse(self) -> Union[ModifyResponse, None]:
            """Get the value of the 'modifyResponse' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.modifyResponse
            """
            return self._value.get("modifyResponse")

        @modifyResponse.setter
        def modifyResponse(self, val: ModifyResponse):
            """Set the value of the 'modifyResponse' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.modifyResponse = ModifyResponse()
            """
            if not isinstance(val, (self._fields["modifyResponse"],)):
                raise InvalidTypeParameter((self._fields["modifyResponse"],))
            self._value.clear()
            self._value["modifyResponse"] = val

        @property
        def addRequest(self) -> Union[AddRequest, None]:
            """Get the value of the 'addRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.addRequest
            """
            return self._value.get("addRequest")

        @addRequest.setter
        def addRequest(self, val: AddRequest):
            """Set the value of the 'addRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.addRequest = AddRequest()
            """
            if not isinstance(val, (self._fields["addRequest"],)):
                raise InvalidTypeParameter((self._fields["addRequest"],))
            self._value.clear()
            self._value["addRequest"] = val

        @property
        def addResponse(self) -> Union[AddResponse, None]:
            """Get the value of the 'addResponse' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.addResponse
            """
            return self._value.get("addResponse")

        @addResponse.setter
        def addResponse(self, val: AddResponse):
            """Set the value of the 'addResponse' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.addResponse = AddResponse()
            """
            if not isinstance(val, (self._fields["addResponse"],)):
                raise InvalidTypeParameter((self._fields["addResponse"],))
            self._value.clear()
            self._value["addResponse"] = val

        @property
        def delRequest(self) -> Union[DelRequest, None]:
            """Get the value of the 'delRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.delRequest
            """
            return self._value.get("delRequest")

        @delRequest.setter
        def delRequest(self, val: DelRequest):
            """Set the value of the 'delRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.delRequest = DelRequest()
            """
            if not isinstance(val, (self._fields["delRequest"],)):
                raise InvalidTypeParameter((self._fields["delRequest"],))
            self._value.clear()
            self._value["delRequest"] = val

        @property
        def delResponse(self) -> Union[DelResponse, None]:
            """Get the value of the 'delResponse' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.delResponse
            """
            return self._value.get("delResponse")

        @delResponse.setter
        def delResponse(self, val: DelResponse):
            """Set the value of the 'delResponse' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.delResponse = DelResponse()
            """
            if not isinstance(val, (self._fields["delResponse"],)):
                raise InvalidTypeParameter((self._fields["delResponse"],))
            self._value.clear()
            self._value["delResponse"] = val

        @property
        def modDNRequest(self) -> Union[ModifyDNRequest, None]:
            """Get the value of the 'modDNRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.modDNRequest
            """
            return self._value.get("modDNRequest")

        @modDNRequest.setter
        def modDNRequest(self, val: ModifyDNRequest):
            """Set the value of the 'modDNRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.modDNRequest = ModifyDNRequest()
            """
            if not isinstance(val, (self._fields["modDNRequest"],)):
                raise InvalidTypeParameter((self._fields["modDNRequest"],))
            self._value.clear()
            self._value["modDNRequest"] = val

        @property
        def modDNResponse(self) -> Union[ModifyDNResponse, None]:
            """Get the value of the 'modDNResponse' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.modDNResponse
            """
            return self._value.get("modDNResponse")

        @modDNResponse.setter
        def modDNResponse(self, val: ModifyDNResponse):
            """Set the value of the 'modDNResponse' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.modDNResponse = ModifyDNResponse()
            """
            if not isinstance(val, (self._fields["modDNResponse"],)):
                raise InvalidTypeParameter((self._fields["modDNResponse"],))
            self._value.clear()
            self._value["modDNResponse"] = val

        @property
        def compareRequest(self) -> Union[CompareRequest, None]:
            """Get the value of the 'compareRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.compareRequest
            """
            return self._value.get("compareRequest")

        @compareRequest.setter
        def compareRequest(self, val: CompareRequest):
            """Set the value of the 'compareRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.compareRequest = CompareRequest()
            """
            if not isinstance(val, (self._fields["compareRequest"],)):
                raise InvalidTypeParameter((self._fields["compareRequest"],))
            self._value.clear()
            self._value["compareRequest"] = val

        @property
        def compareResponse(self) -> Union[CompareResponse, None]:
            """Get the value of the 'compareResponse' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.compareResponse
            """
            return self._value.get("compareResponse")

        @compareResponse.setter
        def compareResponse(self, val: CompareResponse):
            """Set the value of the 'compareResponse' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.compareResponse = CompareResponse()
            """
            if not isinstance(val, (self._fields["compareResponse"],)):
                raise InvalidTypeParameter((self._fields["compareResponse"],))
            self._value.clear()
            self._value["compareResponse"] = val

        @property
        def abandonRequest(self) -> Union[AbandonRequest, None]:
            """Get the value of the 'abandonRequest' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.abandonRequest
            """
            return self._value.get("abandonRequest")

        @abandonRequest.setter
        def abandonRequest(self, val: AbandonRequest):
            """Set the value of the 'abandonRequest' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.abandonRequest = AbandonRequest()
            """
            if not isinstance(val, (self._fields["abandonRequest"],)):
                raise InvalidTypeParameter((self._fields["abandonRequest"],))
            self._value.clear()
            self._value["abandonRequest"] = val

        @property
        def extendedReq(self) -> Union[ExtendedRequest, None]:
            """Get the value of the 'extendedReq' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.extendedReq
            """
            return self._value.get("extendedReq")

        @extendedReq.setter
        def extendedReq(self, val: ExtendedRequest):
            """Set the value of the 'extendedReq' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.extendedReq = ExtendedRequest()
            """
            if not isinstance(val, (self._fields["extendedReq"],)):
                raise InvalidTypeParameter((self._fields["extendedReq"],))
            self._value.clear()
            self._value["extendedReq"] = val

        @property
        def extendedResp(self) -> Union[ExtendedResponse, None]:
            """Get the value of the 'extendedResp' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.extendedResp
            """
            return self._value.get("extendedResp")

        @extendedResp.setter
        def extendedResp(self, val: ExtendedResponse):
            """Set the value of the 'extendedResp' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.extendedResp = ExtendedResponse()
            """
            if not isinstance(val, (self._fields["extendedResp"],)):
                raise InvalidTypeParameter((self._fields["extendedResp"],))
            self._value.clear()
            self._value["extendedResp"] = val

        @property
        def intermediateResponse(self) -> Union[IntermediateResponse, None]:
            """Get the value of the 'intermediateResponse' alternative.
            Will return ``None`` if other alternative is chosen.
            Use as:
                >>> myAlternative = myObject.intermediateResponse
            """
            return self._value.get("intermediateResponse")

        @intermediateResponse.setter
        def intermediateResponse(self, val: IntermediateResponse):
            """Set the value of the 'intermediateResponse' alternative.
            Any previously chosen alternative will be overwritten.
            Use as:
                >>> myObject.intermediateResponse = IntermediateResponse()
            """
            if not isinstance(val, (self._fields["intermediateResponse"],)):
                raise InvalidTypeParameter((self._fields["intermediateResponse"],))
            self._value.clear()
            self._value["intermediateResponse"] = val

        def has_BindRequest(self) -> bool:
            """Return True if the 'bindRequest' alternative is chosen."""
            return [*self._value][0] == "bindRequest"

        def has_BindResponse(self) -> bool:
            """Return True if the 'bindResponse' alternative is chosen."""
            return [*self._value][0] == "bindResponse"

        def has_UnbindRequest(self) -> bool:
            """Return True if the 'unbindRequest' alternative is chosen."""
            return [*self._value][0] == "unbindRequest"

        def has_SearchRequest(self) -> bool:
            """Return True if the 'searchRequest' alternative is chosen."""
            return [*self._value][0] == "searchRequest"

        def has_SearchResEntry(self) -> bool:
            """Return True if the 'searchResEntry' alternative is chosen."""
            return [*self._value][0] == "searchResEntry"

        def has_SearchResDone(self) -> bool:
            """Return True if the 'searchResDone' alternative is chosen."""
            return [*self._value][0] == "searchResDone"

        def has_SearchResRef(self) -> bool:
            """Return True if the 'searchResRef' alternative is chosen."""
            return [*self._value][0] == "searchResRef"

        def has_ModifyRequest(self) -> bool:
            """Return True if the 'modifyRequest' alternative is chosen."""
            return [*self._value][0] == "modifyRequest"

        def has_ModifyResponse(self) -> bool:
            """Return True if the 'modifyResponse' alternative is chosen."""
            return [*self._value][0] == "modifyResponse"

        def has_AddRequest(self) -> bool:
            """Return True if the 'addRequest' alternative is chosen."""
            return [*self._value][0] == "addRequest"

        def has_AddResponse(self) -> bool:
            """Return True if the 'addResponse' alternative is chosen."""
            return [*self._value][0] == "addResponse"

        def has_DelRequest(self) -> bool:
            """Return True if the 'delRequest' alternative is chosen."""
            return [*self._value][0] == "delRequest"

        def has_DelResponse(self) -> bool:
            """Return True if the 'delResponse' alternative is chosen."""
            return [*self._value][0] == "delResponse"

        def has_ModDNRequest(self) -> bool:
            """Return True if the 'modDNRequest' alternative is chosen."""
            return [*self._value][0] == "modDNRequest"

        def has_ModDNResponse(self) -> bool:
            """Return True if the 'modDNResponse' alternative is chosen."""
            return [*self._value][0] == "modDNResponse"

        def has_CompareRequest(self) -> bool:
            """Return True if the 'compareRequest' alternative is chosen."""
            return [*self._value][0] == "compareRequest"

        def has_CompareResponse(self) -> bool:
            """Return True if the 'compareResponse' alternative is chosen."""
            return [*self._value][0] == "compareResponse"

        def has_AbandonRequest(self) -> bool:
            """Return True if the 'abandonRequest' alternative is chosen."""
            return [*self._value][0] == "abandonRequest"

        def has_ExtendedReq(self) -> bool:
            """Return True if the 'extendedReq' alternative is chosen."""
            return [*self._value][0] == "extendedReq"

        def has_ExtendedResp(self) -> bool:
            """Return True if the 'extendedResp' alternative is chosen."""
            return [*self._value][0] == "extendedResp"

        def has_IntermediateResponse(self) -> bool:
            """Return True if the 'intermediateResponse' alternative is chosen."""
            return [*self._value][0] == "intermediateResponse"

        def get_selected(self) -> bool:
            """Return the alternative identifier of the chosen alternative."""
            return [*self._value][0]

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ProtocolOp from it's Python json dict representation."""
            obj = LDAPMessage.ProtocolOp()
            if "bindRequest" in jsond.keys():
                vald = jsond["bindRequest"]
                valo = BindRequest.from_native_type(vald)
                obj.bindRequest = valo
            elif "bindResponse" in jsond.keys():
                vald = jsond["bindResponse"]
                valo = BindResponse.from_native_type(vald)
                obj.bindResponse = valo
            elif "unbindRequest" in jsond.keys():
                obj.unbindRequest = OSS_Null
            elif "searchRequest" in jsond.keys():
                vald = jsond["searchRequest"]
                valo = SearchRequest.from_native_type(vald)
                obj.searchRequest = valo
            elif "searchResEntry" in jsond.keys():
                vald = jsond["searchResEntry"]
                valo = SearchResultEntry.from_native_type(vald)
                obj.searchResEntry = valo
            elif "searchResDone" in jsond.keys():
                vald = jsond["searchResDone"]
                valo = SearchResultDone.from_native_type(vald)
                obj.searchResDone = valo
            elif "searchResRef" in jsond.keys():
                vald = jsond["searchResRef"]
                valo = SearchResultReference.from_native_type(vald)
                obj.searchResRef = valo
            elif "modifyRequest" in jsond.keys():
                vald = jsond["modifyRequest"]
                valo = ModifyRequest.from_native_type(vald)
                obj.modifyRequest = valo
            elif "modifyResponse" in jsond.keys():
                vald = jsond["modifyResponse"]
                valo = ModifyResponse.from_native_type(vald)
                obj.modifyResponse = valo
            elif "addRequest" in jsond.keys():
                vald = jsond["addRequest"]
                valo = AddRequest.from_native_type(vald)
                obj.addRequest = valo
            elif "addResponse" in jsond.keys():
                vald = jsond["addResponse"]
                valo = AddResponse.from_native_type(vald)
                obj.addResponse = valo
            elif "delRequest" in jsond.keys():
                vald = jsond["delRequest"]
                valo = DelRequest.from_native_type(vald)
                obj.delRequest = valo
            elif "delResponse" in jsond.keys():
                vald = jsond["delResponse"]
                valo = DelResponse.from_native_type(vald)
                obj.delResponse = valo
            elif "modDNRequest" in jsond.keys():
                vald = jsond["modDNRequest"]
                valo = ModifyDNRequest.from_native_type(vald)
                obj.modDNRequest = valo
            elif "modDNResponse" in jsond.keys():
                vald = jsond["modDNResponse"]
                valo = ModifyDNResponse.from_native_type(vald)
                obj.modDNResponse = valo
            elif "compareRequest" in jsond.keys():
                vald = jsond["compareRequest"]
                valo = CompareRequest.from_native_type(vald)
                obj.compareRequest = valo
            elif "compareResponse" in jsond.keys():
                vald = jsond["compareResponse"]
                valo = CompareResponse.from_native_type(vald)
                obj.compareResponse = valo
            elif "abandonRequest" in jsond.keys():
                vald = jsond["abandonRequest"]
                valo = AbandonRequest.from_native_type(vald)
                obj.abandonRequest = valo
            elif "extendedReq" in jsond.keys():
                vald = jsond["extendedReq"]
                valo = ExtendedRequest.from_native_type(vald)
                obj.extendedReq = valo
            elif "extendedResp" in jsond.keys():
                vald = jsond["extendedResp"]
                valo = ExtendedResponse.from_native_type(vald)
                obj.extendedResp = valo
            elif "intermediateResponse" in jsond.keys():
                vald = jsond["intermediateResponse"]
                valo = IntermediateResponse.from_native_type(vald)
                obj.intermediateResponse = valo

            return obj

    @classmethod
    def _field_map(cls):
        return {
            "messageID": MessageID,
            "protocolOp": LDAPMessage.ProtocolOp,
            "controls": Controls,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a LDAPMessage SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def messageID(self) -> MessageID:
        """Get the value of the mandatory 'messageID' field
        Use as:
            >>> myField = myObject.messageID
        """
        return self._value.get("messageID")

    @messageID.setter
    def messageID(self, val: MessageID):
        """Set the value of the mandatory  'messageID' field
        Use as:
            >>> myObject.messageID = MessageID()
        """
        if not isinstance(val, (self._fields["messageID"],)):
            raise InvalidTypeParameter((self._fields["messageID"],))
        self._value["messageID"] = val

    @property
    def protocolOp(self) -> ProtocolOp:
        """Get the value of the mandatory 'protocolOp' field
        Use as:
            >>> myField = myObject.protocolOp
        """
        return self._value.get("protocolOp")

    @protocolOp.setter
    def protocolOp(self, val: ProtocolOp):
        """Set the value of the mandatory  'protocolOp' field
        Use as:
            >>> myObject.protocolOp = ProtocolOp()
        """
        if not isinstance(val, (self._fields["protocolOp"],)):
            raise InvalidTypeParameter((self._fields["protocolOp"],))
        self._value["protocolOp"] = val

    @property
    def controls(self) -> Union[Controls, None]:
        """Get the value of the optional 'controls' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.controls
        """
        return self._value.get("controls")

    @controls.setter
    def controls(self, val: Controls):
        """Set the value of the optional 'controls' field
        Use as:
            >>> myObject.controls = Controls()
        """
        if not isinstance(val, (self._fields["controls"],)):
            raise InvalidTypeParameter((self._fields["controls"],))
        self._value["controls"] = val

    @controls.deleter
    def controls(self):
        """Delete the optional 'controls' field
        Use as:
            >>> del myObject.controls
        """
        if "controls" in self._value:
            del self._value["controls"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of LDAPMessage from it's Python json dict representation."""
        obj = LDAPMessage()
        vald = jsond["messageID"]
        valo = MessageID.from_native_type(vald)
        obj.messageID = valo
        vald = jsond["protocolOp"]
        valo = LDAPMessage.ProtocolOp.from_native_type(vald)
        obj.protocolOp = valo
        if "controls" in jsond.keys():
            vald = jsond["controls"]
            valo = Controls.from_native_type(vald)
            obj.controls = valo

        return obj


class MessageID(OSS_Integer):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of MessageID from it's Python json dict representation."""
        return MessageID(jsond)


class AttributeDescription(OSS_OctetString):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AttributeDescription from it's Python json dict representation."""
        return AttributeDescription(jsond)


LDAPDN = AttributeDescription
LDAPString = AttributeDescription
MatchingRuleId = AttributeDescription
RelativeLDAPDN = AttributeDescription
URI = AttributeDescription


class LDAPOID(OSS_OctetString):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of LDAPOID from it's Python json dict representation."""
        return LDAPOID(jsond)


class AttributeValue(OSS_OctetString):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AttributeValue from it's Python json dict representation."""
        return AttributeValue(jsond)


class AttributeValueAssertion(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "attributeDesc": AttributeDescription,
            "assertionValue": AssertionValue,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a AttributeValueAssertion SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def attributeDesc(self) -> AttributeDescription:
        """Get the value of the mandatory 'attributeDesc' field
        Use as:
            >>> myField = myObject.attributeDesc
        """
        return self._value.get("attributeDesc")

    @attributeDesc.setter
    def attributeDesc(self, val: AttributeDescription):
        """Set the value of the mandatory  'attributeDesc' field
        Use as:
            >>> myObject.attributeDesc = AttributeDescription()
        """
        if not isinstance(val, (self._fields["attributeDesc"],)):
            raise InvalidTypeParameter((self._fields["attributeDesc"],))
        self._value["attributeDesc"] = val

    @property
    def assertionValue(self) -> AssertionValue:
        """Get the value of the mandatory 'assertionValue' field
        Use as:
            >>> myField = myObject.assertionValue
        """
        return self._value.get("assertionValue")

    @assertionValue.setter
    def assertionValue(self, val: AssertionValue):
        """Set the value of the mandatory  'assertionValue' field
        Use as:
            >>> myObject.assertionValue = AssertionValue()
        """
        if not isinstance(val, (self._fields["assertionValue"],)):
            raise InvalidTypeParameter((self._fields["assertionValue"],))
        self._value["assertionValue"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AttributeValueAssertion from it's Python json dict representation."""
        obj = AttributeValueAssertion()
        vald = jsond["attributeDesc"]
        valo = AttributeDescription.from_native_type(vald)
        obj.attributeDesc = valo
        vald = jsond["assertionValue"]
        valo = AssertionValue.from_native_type(vald)
        obj.assertionValue = valo

        return obj


class AssertionValue(OSS_OctetString):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AssertionValue from it's Python json dict representation."""
        return AssertionValue(jsond)


class PartialAttribute(OSS_Sequence):
    class Vals(OSS_SequenceOf):
        @classmethod
        def _field_map(cls):
            return AttributeValue

        def __init__(self, value: Optional[list] = None) -> None:
            """Instanciates a Vals SEQUENCE OF type object.
            By default, the object will contain one component only.
            """
            super().__init__()
            self._value = []
            if value is None:
                value = [AttributeValue()]
            self._value = value

        def append(self, value: AttributeValue):
            """Appends an element at the end of the list"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.append(value)

        def insert(self, idx, value: AttributeValue):
            """Inserts an element at the specified index"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.insert(idx, value)

        def __setitem__(self, idx, value: AttributeValue):
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value[idx] = value

        def __getitem__(self, idx) -> AttributeValue:
            return self._value[idx]

        def __delitem__(self, idx):
            del self._value[idx]

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of Vals from it's Python json dict representation."""
            lst = PartialAttribute.Vals([])
            for itemd in jsond:
                obj = AttributeValue.from_native_type(itemd)
                lst.append(obj)

            return lst

    @classmethod
    def _field_map(cls):
        return {
            "type": AttributeDescription,
            "vals": PartialAttribute.Vals,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a PartialAttribute SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def type(self) -> AttributeDescription:
        """Get the value of the mandatory 'type' field
        Use as:
            >>> myField = myObject.type
        """
        return self._value.get("type")

    @type.setter
    def type(self, val: AttributeDescription):
        """Set the value of the mandatory  'type' field
        Use as:
            >>> myObject.type = AttributeDescription()
        """
        if not isinstance(val, (self._fields["type"],)):
            raise InvalidTypeParameter((self._fields["type"],))
        self._value["type"] = val

    @property
    def vals(self) -> Vals:
        """Get the value of the mandatory 'vals' field
        Use as:
            >>> myField = myObject.vals
        """
        return self._value.get("vals")

    @vals.setter
    def vals(self, val: Vals):
        """Set the value of the mandatory  'vals' field
        Use as:
            >>> myObject.vals = Vals()
        """
        if not isinstance(val, (self._fields["vals"],)):
            raise InvalidTypeParameter((self._fields["vals"],))
        self._value["vals"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of PartialAttribute from it's Python json dict representation."""
        obj = PartialAttribute()
        vald = jsond["type"]
        valo = AttributeDescription.from_native_type(vald)
        obj.type = valo
        vald = jsond["vals"]
        valo = PartialAttribute.Vals.from_native_type(vald)
        obj.vals = valo

        return obj


class Attribute(OSS_Sequence):
    class Vals(OSS_SequenceOf):
        @classmethod
        def _field_map(cls):
            return AttributeValue

        def __init__(self, value: Optional[list] = None) -> None:
            """Instanciates a Vals SEQUENCE OF type object.
            By default, the object will contain one component only.
            """
            super().__init__()
            self._value = []
            if value is None:
                value = [AttributeValue()]
            self._value = value

        def append(self, value: AttributeValue):
            """Appends an element at the end of the list"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.append(value)

        def insert(self, idx, value: AttributeValue):
            """Inserts an element at the specified index"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.insert(idx, value)

        def __setitem__(self, idx, value: AttributeValue):
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value[idx] = value

        def __getitem__(self, idx) -> AttributeValue:
            return self._value[idx]

        def __delitem__(self, idx):
            del self._value[idx]

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of Vals from it's Python json dict representation."""
            lst = Attribute.Vals([])
            for itemd in jsond:
                obj = AttributeValue.from_native_type(itemd)
                lst.append(obj)

            return lst

    @classmethod
    def _field_map(cls):
        return {
            "type": AttributeDescription,
            "vals": Attribute.Vals,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a Attribute SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def type(self) -> AttributeDescription:
        """Get the value of the mandatory 'type' field
        Use as:
            >>> myField = myObject.type
        """
        return self._value.get("type")

    @type.setter
    def type(self, val: AttributeDescription):
        """Set the value of the mandatory  'type' field
        Use as:
            >>> myObject.type = AttributeDescription()
        """
        if not isinstance(val, (self._fields["type"],)):
            raise InvalidTypeParameter((self._fields["type"],))
        self._value["type"] = val

    @property
    def vals(self) -> Vals:
        """Get the value of the mandatory 'vals' field
        Use as:
            >>> myField = myObject.vals
        """
        return self._value.get("vals")

    @vals.setter
    def vals(self, val: Vals):
        """Set the value of the mandatory  'vals' field
        Use as:
            >>> myObject.vals = Vals()
        """
        if not isinstance(val, (self._fields["vals"],)):
            raise InvalidTypeParameter((self._fields["vals"],))
        self._value["vals"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of Attribute from it's Python json dict representation."""
        obj = Attribute()
        vald = jsond["type"]
        valo = AttributeDescription.from_native_type(vald)
        obj.type = valo
        vald = jsond["vals"]
        valo = Attribute.Vals.from_native_type(vald)
        obj.vals = valo

        return obj


class LDAPResult(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return LDAPResult.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a LDAPResult SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of LDAPResult from it's Python json dict representation."""
        obj = LDAPResult()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo

        return obj


class Referral(OSS_SequenceOf):
    @classmethod
    def _field_map(cls):
        return AttributeDescription

    def __init__(self, value: Optional[list] = None) -> None:
        """Instanciates a Referral SEQUENCE OF type object.
        By default, the object will contain one component only.
        """
        super().__init__()
        self._value = []
        if value is None:
            value = [AttributeDescription()]
        self._value = value

    def append(self, value: AttributeDescription):
        """Appends an element at the end of the list"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.append(value)

    def insert(self, idx, value: AttributeDescription):
        """Inserts an element at the specified index"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.insert(idx, value)

    def __setitem__(self, idx, value: AttributeDescription):
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value[idx] = value

    def __getitem__(self, idx) -> AttributeDescription:
        return self._value[idx]

    def __delitem__(self, idx):
        del self._value[idx]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of Referral from it's Python json dict representation."""
        lst = Referral([])
        for itemd in jsond:
            obj = AttributeDescription.from_native_type(itemd)
            lst.append(obj)

        return lst


class Controls(OSS_SequenceOf):
    @classmethod
    def _field_map(cls):
        return Control

    def __init__(self, value: Optional[list] = None) -> None:
        """Instanciates a Controls SEQUENCE OF type object.
        By default, the object will contain one component only.
        """
        super().__init__()
        self._value = []
        if value is None:
            value = [Control()]
        self._value = value

    def append(self, value: Control):
        """Appends an element at the end of the list"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.append(value)

    def insert(self, idx, value: Control):
        """Inserts an element at the specified index"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.insert(idx, value)

    def __setitem__(self, idx, value: Control):
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value[idx] = value

    def __getitem__(self, idx) -> Control:
        return self._value[idx]

    def __delitem__(self, idx):
        del self._value[idx]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of Controls from it's Python json dict representation."""
        lst = Controls([])
        for itemd in jsond:
            obj = Control.from_native_type(itemd)
            lst.append(obj)

        return lst


class Control(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "controlType": LDAPOID,
            "criticality": OSS_Boolean,
            "controlValue": OSS_OctetString,
        }

    _defaults = {"criticality": False}

    def __init__(self) -> None:
        """Instanciates a Control SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def controlType(self) -> LDAPOID:
        """Get the value of the mandatory 'controlType' field
        Use as:
            >>> myField = myObject.controlType
        """
        return self._value.get("controlType")

    @controlType.setter
    def controlType(self, val: LDAPOID):
        """Set the value of the mandatory  'controlType' field
        Use as:
            >>> myObject.controlType = LDAPOID()
        """
        if not isinstance(val, (self._fields["controlType"],)):
            raise InvalidTypeParameter((self._fields["controlType"],))
        self._value["controlType"] = val

    @property
    def criticality(self) -> OSS_Boolean:
        """Get the value of the mandatory 'criticality' field
        Use as:
            >>> myField = myObject.criticality
        """
        return self._value.get("criticality")

    @criticality.setter
    def criticality(self, val: OSS_Boolean):
        """Set the value of the mandatory  'criticality' field
        Use as:
            >>> myObject.criticality = OSS_Boolean()
        """
        if not isinstance(val, (self._fields["criticality"], bool)):
            raise InvalidTypeParameter((self._fields["criticality"],))
        self._value["criticality"] = val

    @property
    def controlValue(self) -> Union[OSS_OctetString, None]:
        """Get the value of the optional 'controlValue' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.controlValue
        """
        return self._value.get("controlValue")

    @controlValue.setter
    def controlValue(self, val: OSS_OctetString):
        """Set the value of the optional 'controlValue' field
        Use as:
            >>> myObject.controlValue = OSS_OctetString()
        """
        if not isinstance(val, (self._fields["controlValue"],)):
            raise InvalidTypeParameter((self._fields["controlValue"],))
        self._value["controlValue"] = val

    @controlValue.deleter
    def controlValue(self):
        """Delete the optional 'controlValue' field
        Use as:
            >>> del myObject.controlValue
        """
        if "controlValue" in self._value:
            del self._value["controlValue"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of Control from it's Python json dict representation."""
        obj = Control()
        vald = jsond["controlType"]
        valo = LDAPOID.from_native_type(vald)
        obj.controlType = valo
        if "criticality" in jsond.keys():
            vald = jsond["criticality"]
        else:
            vald = Control._defaults["criticality"]
        obj.criticality = vald
        if "controlValue" in jsond.keys():
            vald = jsond["controlValue"]
            valo = OSS_OctetString.from_native_type(vald)
            obj.controlValue = valo

        return obj


class BindRequest(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "version": OSS_Integer,
            "name": AttributeDescription,
            "authentication": AuthenticationChoice,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a BindRequest SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def version(self) -> OSS_Integer:
        """Get the value of the mandatory 'version' field
        Use as:
            >>> myField = myObject.version
        """
        return self._value.get("version")

    @version.setter
    def version(self, val: OSS_Integer):
        """Set the value of the mandatory  'version' field
        Use as:
            >>> myObject.version = OSS_Integer()
        """
        if not isinstance(val, (self._fields["version"], int)):
            raise InvalidTypeParameter((self._fields["version"],))
        self._value["version"] = val

    @property
    def name(self) -> AttributeDescription:
        """Get the value of the mandatory 'name' field
        Use as:
            >>> myField = myObject.name
        """
        return self._value.get("name")

    @name.setter
    def name(self, val: AttributeDescription):
        """Set the value of the mandatory  'name' field
        Use as:
            >>> myObject.name = AttributeDescription()
        """
        if not isinstance(val, (self._fields["name"],)):
            raise InvalidTypeParameter((self._fields["name"],))
        self._value["name"] = val

    @property
    def authentication(self) -> AuthenticationChoice:
        """Get the value of the mandatory 'authentication' field
        Use as:
            >>> myField = myObject.authentication
        """
        return self._value.get("authentication")

    @authentication.setter
    def authentication(self, val: AuthenticationChoice):
        """Set the value of the mandatory  'authentication' field
        Use as:
            >>> myObject.authentication = AuthenticationChoice()
        """
        if not isinstance(val, (self._fields["authentication"],)):
            raise InvalidTypeParameter((self._fields["authentication"],))
        self._value["authentication"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of BindRequest from it's Python json dict representation."""
        obj = BindRequest()
        vald = jsond["version"]
        obj.version = vald
        vald = jsond["name"]
        valo = AttributeDescription.from_native_type(vald)
        obj.name = valo
        vald = jsond["authentication"]
        valo = AuthenticationChoice.from_native_type(vald)
        obj.authentication = valo

        return obj


class AuthenticationChoice(OSS_Choice):
    @classmethod
    def _field_map(cls):
        return {
            "simple": OSS_OctetString,
            "sasl": SaslCredentials,
        }

    @property
    def simple(self) -> Union[OSS_OctetString, None]:
        """Get the value of the 'simple' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.simple
        """
        return self._value.get("simple")

    @simple.setter
    def simple(self, val: OSS_OctetString):
        """Set the value of the 'simple' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.simple = OSS_OctetString()
        """
        if not isinstance(val, (self._fields["simple"],)):
            raise InvalidTypeParameter((self._fields["simple"],))
        self._value.clear()
        self._value["simple"] = val

    @property
    def sasl(self) -> Union[SaslCredentials, None]:
        """Get the value of the 'sasl' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.sasl
        """
        return self._value.get("sasl")

    @sasl.setter
    def sasl(self, val: SaslCredentials):
        """Set the value of the 'sasl' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.sasl = SaslCredentials()
        """
        if not isinstance(val, (self._fields["sasl"],)):
            raise InvalidTypeParameter((self._fields["sasl"],))
        self._value.clear()
        self._value["sasl"] = val

    def has_Simple(self) -> bool:
        """Return True if the 'simple' alternative is chosen."""
        return [*self._value][0] == "simple"

    def has_Sasl(self) -> bool:
        """Return True if the 'sasl' alternative is chosen."""
        return [*self._value][0] == "sasl"

    def get_selected(self) -> bool:
        """Return the alternative identifier of the chosen alternative."""
        return [*self._value][0]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AuthenticationChoice from it's Python json dict representation."""
        obj = AuthenticationChoice()
        if "simple" in jsond.keys():
            vald = jsond["simple"]
            valo = OSS_OctetString.from_native_type(vald)
            obj.simple = valo
        elif "sasl" in jsond.keys():
            vald = jsond["sasl"]
            valo = SaslCredentials.from_native_type(vald)
            obj.sasl = valo

        return obj


class SaslCredentials(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "mechanism": AttributeDescription,
            "credentials": OSS_OctetString,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a SaslCredentials SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()

    @property
    def mechanism(self) -> AttributeDescription:
        """Get the value of the mandatory 'mechanism' field
        Use as:
            >>> myField = myObject.mechanism
        """
        return self._value.get("mechanism")

    @mechanism.setter
    def mechanism(self, val: AttributeDescription):
        """Set the value of the mandatory  'mechanism' field
        Use as:
            >>> myObject.mechanism = AttributeDescription()
        """
        if not isinstance(val, (self._fields["mechanism"],)):
            raise InvalidTypeParameter((self._fields["mechanism"],))
        self._value["mechanism"] = val

    @property
    def credentials(self) -> Union[OSS_OctetString, None]:
        """Get the value of the optional 'credentials' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.credentials
        """
        return self._value.get("credentials")

    @credentials.setter
    def credentials(self, val: OSS_OctetString):
        """Set the value of the optional 'credentials' field
        Use as:
            >>> myObject.credentials = OSS_OctetString()
        """
        if not isinstance(val, (self._fields["credentials"],)):
            raise InvalidTypeParameter((self._fields["credentials"],))
        self._value["credentials"] = val

    @credentials.deleter
    def credentials(self):
        """Delete the optional 'credentials' field
        Use as:
            >>> del myObject.credentials
        """
        if "credentials" in self._value:
            del self._value["credentials"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of SaslCredentials from it's Python json dict representation."""
        obj = SaslCredentials()
        vald = jsond["mechanism"]
        valo = AttributeDescription.from_native_type(vald)
        obj.mechanism = valo
        if "credentials" in jsond.keys():
            vald = jsond["credentials"]
            valo = OSS_OctetString.from_native_type(vald)
            obj.credentials = valo

        return obj


class BindResponse(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return BindResponse.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
            "serverSaslCreds": OSS_OctetString,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a BindResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @property
    def serverSaslCreds(self) -> Union[OSS_OctetString, None]:
        """Get the value of the optional 'serverSaslCreds' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.serverSaslCreds
        """
        return self._value.get("serverSaslCreds")

    @serverSaslCreds.setter
    def serverSaslCreds(self, val: OSS_OctetString):
        """Set the value of the optional 'serverSaslCreds' field
        Use as:
            >>> myObject.serverSaslCreds = OSS_OctetString()
        """
        if not isinstance(val, (self._fields["serverSaslCreds"],)):
            raise InvalidTypeParameter((self._fields["serverSaslCreds"],))
        self._value["serverSaslCreds"] = val

    @serverSaslCreds.deleter
    def serverSaslCreds(self):
        """Delete the optional 'serverSaslCreds' field
        Use as:
            >>> del myObject.serverSaslCreds
        """
        if "serverSaslCreds" in self._value:
            del self._value["serverSaslCreds"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of BindResponse from it's Python json dict representation."""
        obj = BindResponse()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo
        if "serverSaslCreds" in jsond.keys():
            vald = jsond["serverSaslCreds"]
            valo = OSS_OctetString.from_native_type(vald)
            obj.serverSaslCreds = valo

        return obj


class UnbindRequest(OSS_NullType):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of UnbindRequest from it's Python json dict representation."""
        return UnbindRequest(jsond)


class SearchRequest(OSS_Sequence):
    class Scope(OSS_Enum):

        _fields = {"baseObject": 1, "singleLevel": 2, "wholeSubtree": 3}

        baseObject = "baseObject"
        singleLevel = "singleLevel"
        wholeSubtree = "wholeSubtree"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a Scope ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.baseObject
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of Scope from it's Python json dict representation."""
            return SearchRequest.Scope(jsond)

    class DerefAliases(OSS_Enum):

        _fields = {
            "neverDerefAliases": 1,
            "derefInSearching": 2,
            "derefFindingBaseObj": 3,
            "derefAlways": 4,
        }

        neverDerefAliases = "neverDerefAliases"
        derefInSearching = "derefInSearching"
        derefFindingBaseObj = "derefFindingBaseObj"
        derefAlways = "derefAlways"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a DerefAliases ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.neverDerefAliases
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of DerefAliases from it's Python json dict representation."""
            return SearchRequest.DerefAliases(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "baseObject": AttributeDescription,
            "scope": SearchRequest.Scope,
            "derefAliases": SearchRequest.DerefAliases,
            "sizeLimit": OSS_Integer,
            "timeLimit": OSS_Integer,
            "typesOnly": OSS_Boolean,
            "filter": Filter,
            "attributes": AttributeSelection,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a SearchRequest SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[3]] = (list(self._fields.values())[3])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[4]] = (list(self._fields.values())[4])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[5]] = (list(self._fields.values())[5])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[6]] = (list(self._fields.values())[6])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[7]] = (list(self._fields.values())[7])()

    @property
    def baseObject(self) -> AttributeDescription:
        """Get the value of the mandatory 'baseObject' field
        Use as:
            >>> myField = myObject.baseObject
        """
        return self._value.get("baseObject")

    @baseObject.setter
    def baseObject(self, val: AttributeDescription):
        """Set the value of the mandatory  'baseObject' field
        Use as:
            >>> myObject.baseObject = AttributeDescription()
        """
        if not isinstance(val, (self._fields["baseObject"],)):
            raise InvalidTypeParameter((self._fields["baseObject"],))
        self._value["baseObject"] = val

    @property
    def scope(self) -> Scope:
        """Get the value of the mandatory 'scope' field
        Use as:
            >>> myField = myObject.scope
        """
        return self._value.get("scope")

    @scope.setter
    def scope(self, val: Scope):
        """Set the value of the mandatory  'scope' field
        Use as:
            >>> myObject.scope = Scope()
        """
        if not isinstance(val, (self._fields["scope"],)):
            raise InvalidTypeParameter((self._fields["scope"],))
        self._value["scope"] = val

    @property
    def derefAliases(self) -> DerefAliases:
        """Get the value of the mandatory 'derefAliases' field
        Use as:
            >>> myField = myObject.derefAliases
        """
        return self._value.get("derefAliases")

    @derefAliases.setter
    def derefAliases(self, val: DerefAliases):
        """Set the value of the mandatory  'derefAliases' field
        Use as:
            >>> myObject.derefAliases = DerefAliases()
        """
        if not isinstance(val, (self._fields["derefAliases"],)):
            raise InvalidTypeParameter((self._fields["derefAliases"],))
        self._value["derefAliases"] = val

    @property
    def sizeLimit(self) -> OSS_Integer:
        """Get the value of the mandatory 'sizeLimit' field
        Use as:
            >>> myField = myObject.sizeLimit
        """
        return self._value.get("sizeLimit")

    @sizeLimit.setter
    def sizeLimit(self, val: OSS_Integer):
        """Set the value of the mandatory  'sizeLimit' field
        Use as:
            >>> myObject.sizeLimit = OSS_Integer()
        """
        if not isinstance(val, (self._fields["sizeLimit"], int)):
            raise InvalidTypeParameter((self._fields["sizeLimit"],))
        self._value["sizeLimit"] = val

    @property
    def timeLimit(self) -> OSS_Integer:
        """Get the value of the mandatory 'timeLimit' field
        Use as:
            >>> myField = myObject.timeLimit
        """
        return self._value.get("timeLimit")

    @timeLimit.setter
    def timeLimit(self, val: OSS_Integer):
        """Set the value of the mandatory  'timeLimit' field
        Use as:
            >>> myObject.timeLimit = OSS_Integer()
        """
        if not isinstance(val, (self._fields["timeLimit"], int)):
            raise InvalidTypeParameter((self._fields["timeLimit"],))
        self._value["timeLimit"] = val

    @property
    def typesOnly(self) -> OSS_Boolean:
        """Get the value of the mandatory 'typesOnly' field
        Use as:
            >>> myField = myObject.typesOnly
        """
        return self._value.get("typesOnly")

    @typesOnly.setter
    def typesOnly(self, val: OSS_Boolean):
        """Set the value of the mandatory  'typesOnly' field
        Use as:
            >>> myObject.typesOnly = OSS_Boolean()
        """
        if not isinstance(val, (self._fields["typesOnly"], bool)):
            raise InvalidTypeParameter((self._fields["typesOnly"],))
        self._value["typesOnly"] = val

    @property
    def filter(self) -> Filter:
        """Get the value of the mandatory 'filter' field
        Use as:
            >>> myField = myObject.filter
        """
        return self._value.get("filter")

    @filter.setter
    def filter(self, val: Filter):
        """Set the value of the mandatory  'filter' field
        Use as:
            >>> myObject.filter = Filter()
        """
        if not isinstance(val, (self._fields["filter"],)):
            raise InvalidTypeParameter((self._fields["filter"],))
        self._value["filter"] = val

    @property
    def attributes(self) -> AttributeSelection:
        """Get the value of the mandatory 'attributes' field
        Use as:
            >>> myField = myObject.attributes
        """
        return self._value.get("attributes")

    @attributes.setter
    def attributes(self, val: AttributeSelection):
        """Set the value of the mandatory  'attributes' field
        Use as:
            >>> myObject.attributes = AttributeSelection()
        """
        if not isinstance(val, (self._fields["attributes"],)):
            raise InvalidTypeParameter((self._fields["attributes"],))
        self._value["attributes"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of SearchRequest from it's Python json dict representation."""
        obj = SearchRequest()
        vald = jsond["baseObject"]
        valo = AttributeDescription.from_native_type(vald)
        obj.baseObject = valo
        vald = jsond["scope"]
        valo = SearchRequest.Scope.from_native_type(vald)
        obj.scope = valo
        vald = jsond["derefAliases"]
        valo = SearchRequest.DerefAliases.from_native_type(vald)
        obj.derefAliases = valo
        vald = jsond["sizeLimit"]
        obj.sizeLimit = vald
        vald = jsond["timeLimit"]
        obj.timeLimit = vald
        vald = jsond["typesOnly"]
        obj.typesOnly = vald
        vald = jsond["filter"]
        valo = Filter.from_native_type(vald)
        obj.filter = valo
        vald = jsond["attributes"]
        valo = AttributeSelection.from_native_type(vald)
        obj.attributes = valo

        return obj


class AttributeSelection(OSS_SequenceOf):
    @classmethod
    def _field_map(cls):
        return AttributeDescription

    def __init__(self, value: Optional[list] = None) -> None:
        """Instanciates a AttributeSelection SEQUENCE OF type object.
        By default, the object will contain one component only.
        """
        super().__init__()
        self._value = []
        if value is None:
            value = [AttributeDescription()]
        self._value = value

    def append(self, value: AttributeDescription):
        """Appends an element at the end of the list"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.append(value)

    def insert(self, idx, value: AttributeDescription):
        """Inserts an element at the specified index"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.insert(idx, value)

    def __setitem__(self, idx, value: AttributeDescription):
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value[idx] = value

    def __getitem__(self, idx) -> AttributeDescription:
        return self._value[idx]

    def __delitem__(self, idx):
        del self._value[idx]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AttributeSelection from it's Python json dict representation."""
        lst = AttributeSelection([])
        for itemd in jsond:
            obj = AttributeDescription.from_native_type(itemd)
            lst.append(obj)

        return lst


class Filter(OSS_Choice):
    class And_1(OSS_SequenceOf):
        @classmethod
        def _field_map(cls):
            return Filter

        def __init__(self, value: Optional[list] = None) -> None:
            """Instanciates a And_1 SEQUENCE OF type object.
            By default, the object will contain one component only.
            """
            super().__init__()
            self._value = []
            if value is None:
                value = [Filter()]
            self._value = value

        def append(self, value: Filter):
            """Appends an element at the end of the list"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.append(value)

        def insert(self, idx, value: Filter):
            """Inserts an element at the specified index"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.insert(idx, value)

        def __setitem__(self, idx, value: Filter):
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value[idx] = value

        def __getitem__(self, idx) -> Filter:
            return self._value[idx]

        def __delitem__(self, idx):
            del self._value[idx]

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of And_1 from it's Python json dict representation."""
            lst = Filter.And_1([])
            for itemd in jsond:
                obj = Filter.from_native_type(itemd)
                lst.append(obj)

            return lst

    class Or_1(OSS_SequenceOf):
        @classmethod
        def _field_map(cls):
            return Filter

        def __init__(self, value: Optional[list] = None) -> None:
            """Instanciates a Or_1 SEQUENCE OF type object.
            By default, the object will contain one component only.
            """
            super().__init__()
            self._value = []
            if value is None:
                value = [Filter()]
            self._value = value

        def append(self, value: Filter):
            """Appends an element at the end of the list"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.append(value)

        def insert(self, idx, value: Filter):
            """Inserts an element at the specified index"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.insert(idx, value)

        def __setitem__(self, idx, value: Filter):
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value[idx] = value

        def __getitem__(self, idx) -> Filter:
            return self._value[idx]

        def __delitem__(self, idx):
            del self._value[idx]

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of Or_1 from it's Python json dict representation."""
            lst = Filter.Or_1([])
            for itemd in jsond:
                obj = Filter.from_native_type(itemd)
                lst.append(obj)

            return lst

    @classmethod
    def _field_map(cls):
        return {
            "and": Filter.And_1,
            "or": Filter.Or_1,
            "not": Filter,
            "equalityMatch": AttributeValueAssertion,
            "substrings": SubstringFilter,
            "greaterOrEqual": AttributeValueAssertion,
            "lessOrEqual": AttributeValueAssertion,
            "present": AttributeDescription,
            "approxMatch": AttributeValueAssertion,
            "extensibleMatch": MatchingRuleAssertion,
        }

    @property
    def and_1(self) -> Union[And_1, None]:
        """Get the value of the 'and' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.and_1
        """
        return self._value.get("and")

    @and_1.setter
    def and_1(self, val: And_1):
        """Set the value of the 'and' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.and_1 = And_1()
        """
        if not isinstance(val, (self._fields["and"],)):
            raise InvalidTypeParameter((self._fields["and"],))
        self._value.clear()
        self._value["and"] = val

    @property
    def or_1(self) -> Union[Or_1, None]:
        """Get the value of the 'or' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.or_1
        """
        return self._value.get("or")

    @or_1.setter
    def or_1(self, val: Or_1):
        """Set the value of the 'or' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.or_1 = Or_1()
        """
        if not isinstance(val, (self._fields["or"],)):
            raise InvalidTypeParameter((self._fields["or"],))
        self._value.clear()
        self._value["or"] = val

    @property
    def not_1(self) -> Union[Filter, None]:
        """Get the value of the 'not' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.not_1
        """
        return self._value.get("not")

    @not_1.setter
    def not_1(self, val: Filter):
        """Set the value of the 'not' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.not_1 = Filter()
        """
        if not isinstance(val, (self._fields["not"],)):
            raise InvalidTypeParameter((self._fields["not"],))
        self._value.clear()
        self._value["not"] = val

    @property
    def equalityMatch(self) -> Union[AttributeValueAssertion, None]:
        """Get the value of the 'equalityMatch' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.equalityMatch
        """
        return self._value.get("equalityMatch")

    @equalityMatch.setter
    def equalityMatch(self, val: AttributeValueAssertion):
        """Set the value of the 'equalityMatch' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.equalityMatch = AttributeValueAssertion()
        """
        if not isinstance(val, (self._fields["equalityMatch"],)):
            raise InvalidTypeParameter((self._fields["equalityMatch"],))
        self._value.clear()
        self._value["equalityMatch"] = val

    @property
    def substrings(self) -> Union[SubstringFilter, None]:
        """Get the value of the 'substrings' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.substrings
        """
        return self._value.get("substrings")

    @substrings.setter
    def substrings(self, val: SubstringFilter):
        """Set the value of the 'substrings' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.substrings = SubstringFilter()
        """
        if not isinstance(val, (self._fields["substrings"],)):
            raise InvalidTypeParameter((self._fields["substrings"],))
        self._value.clear()
        self._value["substrings"] = val

    @property
    def greaterOrEqual(self) -> Union[AttributeValueAssertion, None]:
        """Get the value of the 'greaterOrEqual' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.greaterOrEqual
        """
        return self._value.get("greaterOrEqual")

    @greaterOrEqual.setter
    def greaterOrEqual(self, val: AttributeValueAssertion):
        """Set the value of the 'greaterOrEqual' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.greaterOrEqual = AttributeValueAssertion()
        """
        if not isinstance(val, (self._fields["greaterOrEqual"],)):
            raise InvalidTypeParameter((self._fields["greaterOrEqual"],))
        self._value.clear()
        self._value["greaterOrEqual"] = val

    @property
    def lessOrEqual(self) -> Union[AttributeValueAssertion, None]:
        """Get the value of the 'lessOrEqual' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.lessOrEqual
        """
        return self._value.get("lessOrEqual")

    @lessOrEqual.setter
    def lessOrEqual(self, val: AttributeValueAssertion):
        """Set the value of the 'lessOrEqual' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.lessOrEqual = AttributeValueAssertion()
        """
        if not isinstance(val, (self._fields["lessOrEqual"],)):
            raise InvalidTypeParameter((self._fields["lessOrEqual"],))
        self._value.clear()
        self._value["lessOrEqual"] = val

    @property
    def present(self) -> Union[AttributeDescription, None]:
        """Get the value of the 'present' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.present
        """
        return self._value.get("present")

    @present.setter
    def present(self, val: AttributeDescription):
        """Set the value of the 'present' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.present = AttributeDescription()
        """
        if not isinstance(val, (self._fields["present"],)):
            raise InvalidTypeParameter((self._fields["present"],))
        self._value.clear()
        self._value["present"] = val

    @property
    def approxMatch(self) -> Union[AttributeValueAssertion, None]:
        """Get the value of the 'approxMatch' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.approxMatch
        """
        return self._value.get("approxMatch")

    @approxMatch.setter
    def approxMatch(self, val: AttributeValueAssertion):
        """Set the value of the 'approxMatch' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.approxMatch = AttributeValueAssertion()
        """
        if not isinstance(val, (self._fields["approxMatch"],)):
            raise InvalidTypeParameter((self._fields["approxMatch"],))
        self._value.clear()
        self._value["approxMatch"] = val

    @property
    def extensibleMatch(self) -> Union[MatchingRuleAssertion, None]:
        """Get the value of the 'extensibleMatch' alternative.
        Will return ``None`` if other alternative is chosen.
        Use as:
            >>> myAlternative = myObject.extensibleMatch
        """
        return self._value.get("extensibleMatch")

    @extensibleMatch.setter
    def extensibleMatch(self, val: MatchingRuleAssertion):
        """Set the value of the 'extensibleMatch' alternative.
        Any previously chosen alternative will be overwritten.
        Use as:
            >>> myObject.extensibleMatch = MatchingRuleAssertion()
        """
        if not isinstance(val, (self._fields["extensibleMatch"],)):
            raise InvalidTypeParameter((self._fields["extensibleMatch"],))
        self._value.clear()
        self._value["extensibleMatch"] = val

    def has_And_1(self) -> bool:
        """Return True if the 'and' alternative is chosen."""
        return [*self._value][0] == "and"

    def has_Or_1(self) -> bool:
        """Return True if the 'or' alternative is chosen."""
        return [*self._value][0] == "or"

    def has_Not_1(self) -> bool:
        """Return True if the 'not' alternative is chosen."""
        return [*self._value][0] == "not"

    def has_EqualityMatch(self) -> bool:
        """Return True if the 'equalityMatch' alternative is chosen."""
        return [*self._value][0] == "equalityMatch"

    def has_Substrings(self) -> bool:
        """Return True if the 'substrings' alternative is chosen."""
        return [*self._value][0] == "substrings"

    def has_GreaterOrEqual(self) -> bool:
        """Return True if the 'greaterOrEqual' alternative is chosen."""
        return [*self._value][0] == "greaterOrEqual"

    def has_LessOrEqual(self) -> bool:
        """Return True if the 'lessOrEqual' alternative is chosen."""
        return [*self._value][0] == "lessOrEqual"

    def has_Present(self) -> bool:
        """Return True if the 'present' alternative is chosen."""
        return [*self._value][0] == "present"

    def has_ApproxMatch(self) -> bool:
        """Return True if the 'approxMatch' alternative is chosen."""
        return [*self._value][0] == "approxMatch"

    def has_ExtensibleMatch(self) -> bool:
        """Return True if the 'extensibleMatch' alternative is chosen."""
        return [*self._value][0] == "extensibleMatch"

    def get_selected(self) -> bool:
        """Return the alternative identifier of the chosen alternative."""
        return [*self._value][0]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of Filter from it's Python json dict representation."""
        obj = Filter()
        if "and" in jsond.keys():
            vald = jsond["and"]
            valo = Filter.And_1.from_native_type(vald)
            obj.and_1 = valo
        elif "or" in jsond.keys():
            vald = jsond["or"]
            valo = Filter.Or_1.from_native_type(vald)
            obj.or_1 = valo
        elif "not" in jsond.keys():
            vald = jsond["not"]
            valo = Filter.from_native_type(vald)
            obj.not_1 = valo
        elif "equalityMatch" in jsond.keys():
            vald = jsond["equalityMatch"]
            valo = AttributeValueAssertion.from_native_type(vald)
            obj.equalityMatch = valo
        elif "substrings" in jsond.keys():
            vald = jsond["substrings"]
            valo = SubstringFilter.from_native_type(vald)
            obj.substrings = valo
        elif "greaterOrEqual" in jsond.keys():
            vald = jsond["greaterOrEqual"]
            valo = AttributeValueAssertion.from_native_type(vald)
            obj.greaterOrEqual = valo
        elif "lessOrEqual" in jsond.keys():
            vald = jsond["lessOrEqual"]
            valo = AttributeValueAssertion.from_native_type(vald)
            obj.lessOrEqual = valo
        elif "present" in jsond.keys():
            vald = jsond["present"]
            valo = AttributeDescription.from_native_type(vald)
            obj.present = valo
        elif "approxMatch" in jsond.keys():
            vald = jsond["approxMatch"]
            valo = AttributeValueAssertion.from_native_type(vald)
            obj.approxMatch = valo
        elif "extensibleMatch" in jsond.keys():
            vald = jsond["extensibleMatch"]
            valo = MatchingRuleAssertion.from_native_type(vald)
            obj.extensibleMatch = valo

        return obj


class SubstringFilter(OSS_Sequence):
    class Substrings(OSS_SequenceOf):
        class C(OSS_Choice):
            @classmethod
            def _field_map(cls):
                return {
                    "initial": AssertionValue,
                    "any": AssertionValue,
                    "final": AssertionValue,
                }

            @property
            def initial(self) -> Union[AssertionValue, None]:
                """Get the value of the 'initial' alternative.
                Will return ``None`` if other alternative is chosen.
                Use as:
                    >>> myAlternative = myObject.initial
                """
                return self._value.get("initial")

            @initial.setter
            def initial(self, val: AssertionValue):
                """Set the value of the 'initial' alternative.
                Any previously chosen alternative will be overwritten.
                Use as:
                    >>> myObject.initial = AssertionValue()
                """
                if not isinstance(val, (self._fields["initial"],)):
                    raise InvalidTypeParameter((self._fields["initial"],))
                self._value.clear()
                self._value["initial"] = val

            @property
            def any(self) -> Union[AssertionValue, None]:
                """Get the value of the 'any' alternative.
                Will return ``None`` if other alternative is chosen.
                Use as:
                    >>> myAlternative = myObject.any
                """
                return self._value.get("any")

            @any.setter
            def any(self, val: AssertionValue):
                """Set the value of the 'any' alternative.
                Any previously chosen alternative will be overwritten.
                Use as:
                    >>> myObject.any = AssertionValue()
                """
                if not isinstance(val, (self._fields["any"],)):
                    raise InvalidTypeParameter((self._fields["any"],))
                self._value.clear()
                self._value["any"] = val

            @property
            def final(self) -> Union[AssertionValue, None]:
                """Get the value of the 'final' alternative.
                Will return ``None`` if other alternative is chosen.
                Use as:
                    >>> myAlternative = myObject.final
                """
                return self._value.get("final")

            @final.setter
            def final(self, val: AssertionValue):
                """Set the value of the 'final' alternative.
                Any previously chosen alternative will be overwritten.
                Use as:
                    >>> myObject.final = AssertionValue()
                """
                if not isinstance(val, (self._fields["final"],)):
                    raise InvalidTypeParameter((self._fields["final"],))
                self._value.clear()
                self._value["final"] = val

            def has_Initial(self) -> bool:
                """Return True if the 'initial' alternative is chosen."""
                return [*self._value][0] == "initial"

            def has_Any(self) -> bool:
                """Return True if the 'any' alternative is chosen."""
                return [*self._value][0] == "any"

            def has_Final(self) -> bool:
                """Return True if the 'final' alternative is chosen."""
                return [*self._value][0] == "final"

            def get_selected(self) -> bool:
                """Return the alternative identifier of the chosen alternative."""
                return [*self._value][0]

            @staticmethod
            def from_native_type(jsond: dict):
                """Obtain an instance of C from it's Python json dict representation."""
                obj = SubstringFilter.Substrings.C()
                if "initial" in jsond.keys():
                    vald = jsond["initial"]
                    valo = AssertionValue.from_native_type(vald)
                    obj.initial = valo
                elif "any" in jsond.keys():
                    vald = jsond["any"]
                    valo = AssertionValue.from_native_type(vald)
                    obj.any = valo
                elif "final" in jsond.keys():
                    vald = jsond["final"]
                    valo = AssertionValue.from_native_type(vald)
                    obj.final = valo

                return obj

        @classmethod
        def _field_map(cls):
            return SubstringFilter.Substrings.C

        def __init__(self, value: Optional[list] = None) -> None:
            """Instanciates a Substrings SEQUENCE OF type object.
            By default, the object will contain one component only.
            """
            super().__init__()
            self._value = []
            if value is None:
                value = [SubstringFilter.Substrings.C()]
            self._value = value

        def append(self, value: C):
            """Appends an element at the end of the list"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.append(value)

        def insert(self, idx, value: C):
            """Inserts an element at the specified index"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.insert(idx, value)

        def __setitem__(self, idx, value: C):
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value[idx] = value

        def __getitem__(self, idx) -> C:
            return self._value[idx]

        def __delitem__(self, idx):
            del self._value[idx]

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of Substrings from it's Python json dict representation."""
            lst = SubstringFilter.Substrings([])
            for itemd in jsond:
                obj = SubstringFilter.Substrings.C.from_native_type(itemd)
                lst.append(obj)

            return lst

    @classmethod
    def _field_map(cls):
        return {
            "type": AttributeDescription,
            "substrings": SubstringFilter.Substrings,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a SubstringFilter SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def type(self) -> AttributeDescription:
        """Get the value of the mandatory 'type' field
        Use as:
            >>> myField = myObject.type
        """
        return self._value.get("type")

    @type.setter
    def type(self, val: AttributeDescription):
        """Set the value of the mandatory  'type' field
        Use as:
            >>> myObject.type = AttributeDescription()
        """
        if not isinstance(val, (self._fields["type"],)):
            raise InvalidTypeParameter((self._fields["type"],))
        self._value["type"] = val

    @property
    def substrings(self) -> Substrings:
        """Get the value of the mandatory 'substrings' field
        Use as:
            >>> myField = myObject.substrings
        """
        return self._value.get("substrings")

    @substrings.setter
    def substrings(self, val: Substrings):
        """Set the value of the mandatory  'substrings' field
        Use as:
            >>> myObject.substrings = Substrings()
        """
        if not isinstance(val, (self._fields["substrings"],)):
            raise InvalidTypeParameter((self._fields["substrings"],))
        self._value["substrings"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of SubstringFilter from it's Python json dict representation."""
        obj = SubstringFilter()
        vald = jsond["type"]
        valo = AttributeDescription.from_native_type(vald)
        obj.type = valo
        vald = jsond["substrings"]
        valo = SubstringFilter.Substrings.from_native_type(vald)
        obj.substrings = valo

        return obj


class MatchingRuleAssertion(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "matchingRule": AttributeDescription,
            "type": AttributeDescription,
            "matchValue": AssertionValue,
            "dnAttributes": OSS_Boolean,
        }

    _defaults = {"dnAttributes": False}

    def __init__(self) -> None:
        """Instanciates a MatchingRuleAssertion SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[3]] = (list(self._fields.values())[3])()

    @property
    def matchingRule(self) -> Union[AttributeDescription, None]:
        """Get the value of the optional 'matchingRule' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.matchingRule
        """
        return self._value.get("matchingRule")

    @matchingRule.setter
    def matchingRule(self, val: AttributeDescription):
        """Set the value of the optional 'matchingRule' field
        Use as:
            >>> myObject.matchingRule = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchingRule"],)):
            raise InvalidTypeParameter((self._fields["matchingRule"],))
        self._value["matchingRule"] = val

    @matchingRule.deleter
    def matchingRule(self):
        """Delete the optional 'matchingRule' field
        Use as:
            >>> del myObject.matchingRule
        """
        if "matchingRule" in self._value:
            del self._value["matchingRule"]

    @property
    def type(self) -> Union[AttributeDescription, None]:
        """Get the value of the optional 'type' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.type
        """
        return self._value.get("type")

    @type.setter
    def type(self, val: AttributeDescription):
        """Set the value of the optional 'type' field
        Use as:
            >>> myObject.type = AttributeDescription()
        """
        if not isinstance(val, (self._fields["type"],)):
            raise InvalidTypeParameter((self._fields["type"],))
        self._value["type"] = val

    @type.deleter
    def type(self):
        """Delete the optional 'type' field
        Use as:
            >>> del myObject.type
        """
        if "type" in self._value:
            del self._value["type"]

    @property
    def matchValue(self) -> AssertionValue:
        """Get the value of the mandatory 'matchValue' field
        Use as:
            >>> myField = myObject.matchValue
        """
        return self._value.get("matchValue")

    @matchValue.setter
    def matchValue(self, val: AssertionValue):
        """Set the value of the mandatory  'matchValue' field
        Use as:
            >>> myObject.matchValue = AssertionValue()
        """
        if not isinstance(val, (self._fields["matchValue"],)):
            raise InvalidTypeParameter((self._fields["matchValue"],))
        self._value["matchValue"] = val

    @property
    def dnAttributes(self) -> OSS_Boolean:
        """Get the value of the mandatory 'dnAttributes' field
        Use as:
            >>> myField = myObject.dnAttributes
        """
        return self._value.get("dnAttributes")

    @dnAttributes.setter
    def dnAttributes(self, val: OSS_Boolean):
        """Set the value of the mandatory  'dnAttributes' field
        Use as:
            >>> myObject.dnAttributes = OSS_Boolean()
        """
        if not isinstance(val, (self._fields["dnAttributes"], bool)):
            raise InvalidTypeParameter((self._fields["dnAttributes"],))
        self._value["dnAttributes"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of MatchingRuleAssertion from it's Python json dict representation."""
        obj = MatchingRuleAssertion()
        if "matchingRule" in jsond.keys():
            vald = jsond["matchingRule"]
            valo = AttributeDescription.from_native_type(vald)
            obj.matchingRule = valo
        if "type" in jsond.keys():
            vald = jsond["type"]
            valo = AttributeDescription.from_native_type(vald)
            obj.type = valo
        vald = jsond["matchValue"]
        valo = AssertionValue.from_native_type(vald)
        obj.matchValue = valo
        if "dnAttributes" in jsond.keys():
            vald = jsond["dnAttributes"]
        else:
            vald = MatchingRuleAssertion._defaults["dnAttributes"]
        obj.dnAttributes = vald

        return obj


class SearchResultEntry(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "objectName": AttributeDescription,
            "attributes": PartialAttributeList,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a SearchResultEntry SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def objectName(self) -> AttributeDescription:
        """Get the value of the mandatory 'objectName' field
        Use as:
            >>> myField = myObject.objectName
        """
        return self._value.get("objectName")

    @objectName.setter
    def objectName(self, val: AttributeDescription):
        """Set the value of the mandatory  'objectName' field
        Use as:
            >>> myObject.objectName = AttributeDescription()
        """
        if not isinstance(val, (self._fields["objectName"],)):
            raise InvalidTypeParameter((self._fields["objectName"],))
        self._value["objectName"] = val

    @property
    def attributes(self) -> PartialAttributeList:
        """Get the value of the mandatory 'attributes' field
        Use as:
            >>> myField = myObject.attributes
        """
        return self._value.get("attributes")

    @attributes.setter
    def attributes(self, val: PartialAttributeList):
        """Set the value of the mandatory  'attributes' field
        Use as:
            >>> myObject.attributes = PartialAttributeList()
        """
        if not isinstance(val, (self._fields["attributes"],)):
            raise InvalidTypeParameter((self._fields["attributes"],))
        self._value["attributes"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of SearchResultEntry from it's Python json dict representation."""
        obj = SearchResultEntry()
        vald = jsond["objectName"]
        valo = AttributeDescription.from_native_type(vald)
        obj.objectName = valo
        vald = jsond["attributes"]
        valo = PartialAttributeList.from_native_type(vald)
        obj.attributes = valo

        return obj


class PartialAttributeList(OSS_SequenceOf):
    @classmethod
    def _field_map(cls):
        return PartialAttribute

    def __init__(self, value: Optional[list] = None) -> None:
        """Instanciates a PartialAttributeList SEQUENCE OF type object.
        By default, the object will contain one component only.
        """
        super().__init__()
        self._value = []
        if value is None:
            value = [PartialAttribute()]
        self._value = value

    def append(self, value: PartialAttribute):
        """Appends an element at the end of the list"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.append(value)

    def insert(self, idx, value: PartialAttribute):
        """Inserts an element at the specified index"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.insert(idx, value)

    def __setitem__(self, idx, value: PartialAttribute):
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value[idx] = value

    def __getitem__(self, idx) -> PartialAttribute:
        return self._value[idx]

    def __delitem__(self, idx):
        del self._value[idx]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of PartialAttributeList from it's Python json dict representation."""
        lst = PartialAttributeList([])
        for itemd in jsond:
            obj = PartialAttribute.from_native_type(itemd)
            lst.append(obj)

        return lst


class SearchResultReference(OSS_SequenceOf):
    @classmethod
    def _field_map(cls):
        return AttributeDescription

    def __init__(self, value: Optional[list] = None) -> None:
        """Instanciates a SearchResultReference SEQUENCE OF type object.
        By default, the object will contain one component only.
        """
        super().__init__()
        self._value = []
        if value is None:
            value = [AttributeDescription()]
        self._value = value

    def append(self, value: AttributeDescription):
        """Appends an element at the end of the list"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.append(value)

    def insert(self, idx, value: AttributeDescription):
        """Inserts an element at the specified index"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.insert(idx, value)

    def __setitem__(self, idx, value: AttributeDescription):
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value[idx] = value

    def __getitem__(self, idx) -> AttributeDescription:
        return self._value[idx]

    def __delitem__(self, idx):
        del self._value[idx]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of SearchResultReference from it's Python json dict representation."""
        lst = SearchResultReference([])
        for itemd in jsond:
            obj = AttributeDescription.from_native_type(itemd)
            lst.append(obj)

        return lst


class SearchResultDone(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return SearchResultDone.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a SearchResultDone SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of SearchResultDone from it's Python json dict representation."""
        obj = SearchResultDone()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo

        return obj


class ModifyRequest(OSS_Sequence):
    class Changes(OSS_SequenceOf):
        class C(OSS_Sequence):
            class Operation(OSS_Enum):

                _fields = {"add": 1, "delete": 2, "replace": 3}

                add = "add"
                delete = "delete"
                replace = "replace"

                def __init__(self, value: Optional[str] = None) -> None:
                    """Instanciates a Operation ENUMERATED type object.
                    By default, the object will be initialised to the first enumerated value.
                    """
                    if value is not None:
                        if value not in self._fields.keys():
                            raise ValueError("%s not in permitted list of enumerators" % (value))
                    else:
                        value = self.add
                    self._value = value

                @staticmethod
                def from_native_type(jsond: dict):
                    """Obtain an instance of Operation from it's Python json dict representation."""
                    return ModifyRequest.Changes.C.Operation(jsond)

            @classmethod
            def _field_map(cls):
                return {
                    "operation": ModifyRequest.Changes.C.Operation,
                    "modification": PartialAttribute,
                }

            _defaults = {}

            def __init__(self) -> None:
                """Instanciates a C SEQUENCE type object.
                The object will contain all mandatory fields and no optional fields.
                """
                super().__init__()
                self._value = {}
                # Create values for non-optional fields
                self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
                # Create values for non-optional fields
                self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

            @property
            def operation(self) -> Operation:
                """Get the value of the mandatory 'operation' field
                Use as:
                    >>> myField = myObject.operation
                """
                return self._value.get("operation")

            @operation.setter
            def operation(self, val: Operation):
                """Set the value of the mandatory  'operation' field
                Use as:
                    >>> myObject.operation = Operation()
                """
                if not isinstance(val, (self._fields["operation"],)):
                    raise InvalidTypeParameter((self._fields["operation"],))
                self._value["operation"] = val

            @property
            def modification(self) -> PartialAttribute:
                """Get the value of the mandatory 'modification' field
                Use as:
                    >>> myField = myObject.modification
                """
                return self._value.get("modification")

            @modification.setter
            def modification(self, val: PartialAttribute):
                """Set the value of the mandatory  'modification' field
                Use as:
                    >>> myObject.modification = PartialAttribute()
                """
                if not isinstance(val, (self._fields["modification"],)):
                    raise InvalidTypeParameter((self._fields["modification"],))
                self._value["modification"] = val

            @staticmethod
            def from_native_type(jsond: dict):
                """Obtain an instance of C from it's Python json dict representation."""
                obj = ModifyRequest.Changes.C()
                vald = jsond["operation"]
                valo = ModifyRequest.Changes.C.Operation.from_native_type(vald)
                obj.operation = valo
                vald = jsond["modification"]
                valo = PartialAttribute.from_native_type(vald)
                obj.modification = valo

                return obj

        @classmethod
        def _field_map(cls):
            return ModifyRequest.Changes.C

        def __init__(self, value: Optional[list] = None) -> None:
            """Instanciates a Changes SEQUENCE OF type object.
            By default, the object will contain one component only.
            """
            super().__init__()
            self._value = []
            if value is None:
                value = [ModifyRequest.Changes.C()]
            self._value = value

        def append(self, value: C):
            """Appends an element at the end of the list"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.append(value)

        def insert(self, idx, value: C):
            """Inserts an element at the specified index"""
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value.insert(idx, value)

        def __setitem__(self, idx, value: C):
            if not isinstance(value, (self._fields,)):
                raise InvalidTypeParameter((self._fields,))
            self._value[idx] = value

        def __getitem__(self, idx) -> C:
            return self._value[idx]

        def __delitem__(self, idx):
            del self._value[idx]

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of Changes from it's Python json dict representation."""
            lst = ModifyRequest.Changes([])
            for itemd in jsond:
                obj = ModifyRequest.Changes.C.from_native_type(itemd)
                lst.append(obj)

            return lst

    @classmethod
    def _field_map(cls):
        return {
            "object": AttributeDescription,
            "changes": ModifyRequest.Changes,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a ModifyRequest SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def object(self) -> AttributeDescription:
        """Get the value of the mandatory 'object' field
        Use as:
            >>> myField = myObject.object
        """
        return self._value.get("object")

    @object.setter
    def object(self, val: AttributeDescription):
        """Set the value of the mandatory  'object' field
        Use as:
            >>> myObject.object = AttributeDescription()
        """
        if not isinstance(val, (self._fields["object"],)):
            raise InvalidTypeParameter((self._fields["object"],))
        self._value["object"] = val

    @property
    def changes(self) -> Changes:
        """Get the value of the mandatory 'changes' field
        Use as:
            >>> myField = myObject.changes
        """
        return self._value.get("changes")

    @changes.setter
    def changes(self, val: Changes):
        """Set the value of the mandatory  'changes' field
        Use as:
            >>> myObject.changes = Changes()
        """
        if not isinstance(val, (self._fields["changes"],)):
            raise InvalidTypeParameter((self._fields["changes"],))
        self._value["changes"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of ModifyRequest from it's Python json dict representation."""
        obj = ModifyRequest()
        vald = jsond["object"]
        valo = AttributeDescription.from_native_type(vald)
        obj.object = valo
        vald = jsond["changes"]
        valo = ModifyRequest.Changes.from_native_type(vald)
        obj.changes = valo

        return obj


class ModifyResponse(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return ModifyResponse.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a ModifyResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of ModifyResponse from it's Python json dict representation."""
        obj = ModifyResponse()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo

        return obj


class AddRequest(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "entry": AttributeDescription,
            "attributes": AttributeList,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a AddRequest SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def entry(self) -> AttributeDescription:
        """Get the value of the mandatory 'entry' field
        Use as:
            >>> myField = myObject.entry
        """
        return self._value.get("entry")

    @entry.setter
    def entry(self, val: AttributeDescription):
        """Set the value of the mandatory  'entry' field
        Use as:
            >>> myObject.entry = AttributeDescription()
        """
        if not isinstance(val, (self._fields["entry"],)):
            raise InvalidTypeParameter((self._fields["entry"],))
        self._value["entry"] = val

    @property
    def attributes(self) -> AttributeList:
        """Get the value of the mandatory 'attributes' field
        Use as:
            >>> myField = myObject.attributes
        """
        return self._value.get("attributes")

    @attributes.setter
    def attributes(self, val: AttributeList):
        """Set the value of the mandatory  'attributes' field
        Use as:
            >>> myObject.attributes = AttributeList()
        """
        if not isinstance(val, (self._fields["attributes"],)):
            raise InvalidTypeParameter((self._fields["attributes"],))
        self._value["attributes"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AddRequest from it's Python json dict representation."""
        obj = AddRequest()
        vald = jsond["entry"]
        valo = AttributeDescription.from_native_type(vald)
        obj.entry = valo
        vald = jsond["attributes"]
        valo = AttributeList.from_native_type(vald)
        obj.attributes = valo

        return obj


class AttributeList(OSS_SequenceOf):
    @classmethod
    def _field_map(cls):
        return Attribute

    def __init__(self, value: Optional[list] = None) -> None:
        """Instanciates a AttributeList SEQUENCE OF type object.
        By default, the object will contain one component only.
        """
        super().__init__()
        self._value = []
        if value is None:
            value = [Attribute()]
        self._value = value

    def append(self, value: Attribute):
        """Appends an element at the end of the list"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.append(value)

    def insert(self, idx, value: Attribute):
        """Inserts an element at the specified index"""
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value.insert(idx, value)

    def __setitem__(self, idx, value: Attribute):
        if not isinstance(value, (self._fields,)):
            raise InvalidTypeParameter((self._fields,))
        self._value[idx] = value

    def __getitem__(self, idx) -> Attribute:
        return self._value[idx]

    def __delitem__(self, idx):
        del self._value[idx]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AttributeList from it's Python json dict representation."""
        lst = AttributeList([])
        for itemd in jsond:
            obj = Attribute.from_native_type(itemd)
            lst.append(obj)

        return lst


class AddResponse(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return AddResponse.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a AddResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AddResponse from it's Python json dict representation."""
        obj = AddResponse()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo

        return obj


class DelRequest(OSS_OctetString):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of DelRequest from it's Python json dict representation."""
        return DelRequest(jsond)


class DelResponse(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return DelResponse.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a DelResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of DelResponse from it's Python json dict representation."""
        obj = DelResponse()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo

        return obj


class ModifyDNRequest(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "entry": AttributeDescription,
            "newrdn": AttributeDescription,
            "deleteoldrdn": OSS_Boolean,
            "newSuperior": AttributeDescription,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a ModifyDNRequest SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def entry(self) -> AttributeDescription:
        """Get the value of the mandatory 'entry' field
        Use as:
            >>> myField = myObject.entry
        """
        return self._value.get("entry")

    @entry.setter
    def entry(self, val: AttributeDescription):
        """Set the value of the mandatory  'entry' field
        Use as:
            >>> myObject.entry = AttributeDescription()
        """
        if not isinstance(val, (self._fields["entry"],)):
            raise InvalidTypeParameter((self._fields["entry"],))
        self._value["entry"] = val

    @property
    def newrdn(self) -> AttributeDescription:
        """Get the value of the mandatory 'newrdn' field
        Use as:
            >>> myField = myObject.newrdn
        """
        return self._value.get("newrdn")

    @newrdn.setter
    def newrdn(self, val: AttributeDescription):
        """Set the value of the mandatory  'newrdn' field
        Use as:
            >>> myObject.newrdn = AttributeDescription()
        """
        if not isinstance(val, (self._fields["newrdn"],)):
            raise InvalidTypeParameter((self._fields["newrdn"],))
        self._value["newrdn"] = val

    @property
    def deleteoldrdn(self) -> OSS_Boolean:
        """Get the value of the mandatory 'deleteoldrdn' field
        Use as:
            >>> myField = myObject.deleteoldrdn
        """
        return self._value.get("deleteoldrdn")

    @deleteoldrdn.setter
    def deleteoldrdn(self, val: OSS_Boolean):
        """Set the value of the mandatory  'deleteoldrdn' field
        Use as:
            >>> myObject.deleteoldrdn = OSS_Boolean()
        """
        if not isinstance(val, (self._fields["deleteoldrdn"], bool)):
            raise InvalidTypeParameter((self._fields["deleteoldrdn"],))
        self._value["deleteoldrdn"] = val

    @property
    def newSuperior(self) -> Union[AttributeDescription, None]:
        """Get the value of the optional 'newSuperior' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.newSuperior
        """
        return self._value.get("newSuperior")

    @newSuperior.setter
    def newSuperior(self, val: AttributeDescription):
        """Set the value of the optional 'newSuperior' field
        Use as:
            >>> myObject.newSuperior = AttributeDescription()
        """
        if not isinstance(val, (self._fields["newSuperior"],)):
            raise InvalidTypeParameter((self._fields["newSuperior"],))
        self._value["newSuperior"] = val

    @newSuperior.deleter
    def newSuperior(self):
        """Delete the optional 'newSuperior' field
        Use as:
            >>> del myObject.newSuperior
        """
        if "newSuperior" in self._value:
            del self._value["newSuperior"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of ModifyDNRequest from it's Python json dict representation."""
        obj = ModifyDNRequest()
        vald = jsond["entry"]
        valo = AttributeDescription.from_native_type(vald)
        obj.entry = valo
        vald = jsond["newrdn"]
        valo = AttributeDescription.from_native_type(vald)
        obj.newrdn = valo
        vald = jsond["deleteoldrdn"]
        obj.deleteoldrdn = vald
        if "newSuperior" in jsond.keys():
            vald = jsond["newSuperior"]
            valo = AttributeDescription.from_native_type(vald)
            obj.newSuperior = valo

        return obj


class ModifyDNResponse(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return ModifyDNResponse.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a ModifyDNResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of ModifyDNResponse from it's Python json dict representation."""
        obj = ModifyDNResponse()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo

        return obj


class CompareRequest(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "entry": AttributeDescription,
            "ava": AttributeValueAssertion,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a CompareRequest SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()

    @property
    def entry(self) -> AttributeDescription:
        """Get the value of the mandatory 'entry' field
        Use as:
            >>> myField = myObject.entry
        """
        return self._value.get("entry")

    @entry.setter
    def entry(self, val: AttributeDescription):
        """Set the value of the mandatory  'entry' field
        Use as:
            >>> myObject.entry = AttributeDescription()
        """
        if not isinstance(val, (self._fields["entry"],)):
            raise InvalidTypeParameter((self._fields["entry"],))
        self._value["entry"] = val

    @property
    def ava(self) -> AttributeValueAssertion:
        """Get the value of the mandatory 'ava' field
        Use as:
            >>> myField = myObject.ava
        """
        return self._value.get("ava")

    @ava.setter
    def ava(self, val: AttributeValueAssertion):
        """Set the value of the mandatory  'ava' field
        Use as:
            >>> myObject.ava = AttributeValueAssertion()
        """
        if not isinstance(val, (self._fields["ava"],)):
            raise InvalidTypeParameter((self._fields["ava"],))
        self._value["ava"] = val

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of CompareRequest from it's Python json dict representation."""
        obj = CompareRequest()
        vald = jsond["entry"]
        valo = AttributeDescription.from_native_type(vald)
        obj.entry = valo
        vald = jsond["ava"]
        valo = AttributeValueAssertion.from_native_type(vald)
        obj.ava = valo

        return obj


class CompareResponse(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return CompareResponse.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a CompareResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of CompareResponse from it's Python json dict representation."""
        obj = CompareResponse()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo

        return obj


class AbandonRequest(OSS_Integer):
    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of AbandonRequest from it's Python json dict representation."""
        return AbandonRequest(jsond)


class ExtendedRequest(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "requestName": LDAPOID,
            "requestValue": OSS_OctetString,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a ExtendedRequest SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()

    @property
    def requestName(self) -> LDAPOID:
        """Get the value of the mandatory 'requestName' field
        Use as:
            >>> myField = myObject.requestName
        """
        return self._value.get("requestName")

    @requestName.setter
    def requestName(self, val: LDAPOID):
        """Set the value of the mandatory  'requestName' field
        Use as:
            >>> myObject.requestName = LDAPOID()
        """
        if not isinstance(val, (self._fields["requestName"],)):
            raise InvalidTypeParameter((self._fields["requestName"],))
        self._value["requestName"] = val

    @property
    def requestValue(self) -> Union[OSS_OctetString, None]:
        """Get the value of the optional 'requestValue' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.requestValue
        """
        return self._value.get("requestValue")

    @requestValue.setter
    def requestValue(self, val: OSS_OctetString):
        """Set the value of the optional 'requestValue' field
        Use as:
            >>> myObject.requestValue = OSS_OctetString()
        """
        if not isinstance(val, (self._fields["requestValue"],)):
            raise InvalidTypeParameter((self._fields["requestValue"],))
        self._value["requestValue"] = val

    @requestValue.deleter
    def requestValue(self):
        """Delete the optional 'requestValue' field
        Use as:
            >>> del myObject.requestValue
        """
        if "requestValue" in self._value:
            del self._value["requestValue"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of ExtendedRequest from it's Python json dict representation."""
        obj = ExtendedRequest()
        vald = jsond["requestName"]
        valo = LDAPOID.from_native_type(vald)
        obj.requestName = valo
        if "requestValue" in jsond.keys():
            vald = jsond["requestValue"]
            valo = OSS_OctetString.from_native_type(vald)
            obj.requestValue = valo

        return obj


class ExtendedResponse(OSS_Sequence):
    class ResultCode(OSS_Enum):

        _fields = {
            "success": 1,
            "operationsError": 2,
            "protocolError": 3,
            "timeLimitExceeded": 4,
            "sizeLimitExceeded": 5,
            "compareFalse": 6,
            "compareTrue": 7,
            "authMethodNotSupported": 8,
            "strongerAuthRequired": 9,
            "referral": 10,
            "adminLimitExceeded": 11,
            "unavailableCriticalExtension": 12,
            "confidentialityRequired": 13,
            "saslBindInProgress": 14,
            "noSuchAttribute": 15,
            "undefinedAttributeType": 16,
            "inappropriateMatching": 17,
            "constraintViolation": 18,
            "attributeOrValueExists": 19,
            "invalidAttributeSyntax": 20,
            "noSuchObject": 21,
            "aliasProblem": 22,
            "invalidDNSyntax": 23,
            "aliasDereferencingProblem": 24,
            "inappropriateAuthentication": 25,
            "invalidCredentials": 26,
            "insufficientAccessRights": 27,
            "busy": 28,
            "unavailable": 29,
            "unwillingToPerform": 30,
            "loopDetect": 31,
            "namingViolation": 32,
            "objectClassViolation": 33,
            "notAllowedOnNonLeaf": 34,
            "notAllowedOnRDN": 35,
            "entryAlreadyExists": 36,
            "objectClassModsProhibited": 37,
            "affectsMultipleDSAs": 38,
            "other": 39,
        }

        success = "success"
        operationsError = "operationsError"
        protocolError = "protocolError"
        timeLimitExceeded = "timeLimitExceeded"
        sizeLimitExceeded = "sizeLimitExceeded"
        compareFalse = "compareFalse"
        compareTrue = "compareTrue"
        authMethodNotSupported = "authMethodNotSupported"
        strongerAuthRequired = "strongerAuthRequired"
        referral = "referral"
        adminLimitExceeded = "adminLimitExceeded"
        unavailableCriticalExtension = "unavailableCriticalExtension"
        confidentialityRequired = "confidentialityRequired"
        saslBindInProgress = "saslBindInProgress"
        noSuchAttribute = "noSuchAttribute"
        undefinedAttributeType = "undefinedAttributeType"
        inappropriateMatching = "inappropriateMatching"
        constraintViolation = "constraintViolation"
        attributeOrValueExists = "attributeOrValueExists"
        invalidAttributeSyntax = "invalidAttributeSyntax"
        noSuchObject = "noSuchObject"
        aliasProblem = "aliasProblem"
        invalidDNSyntax = "invalidDNSyntax"
        aliasDereferencingProblem = "aliasDereferencingProblem"
        inappropriateAuthentication = "inappropriateAuthentication"
        invalidCredentials = "invalidCredentials"
        insufficientAccessRights = "insufficientAccessRights"
        busy = "busy"
        unavailable = "unavailable"
        unwillingToPerform = "unwillingToPerform"
        loopDetect = "loopDetect"
        namingViolation = "namingViolation"
        objectClassViolation = "objectClassViolation"
        notAllowedOnNonLeaf = "notAllowedOnNonLeaf"
        notAllowedOnRDN = "notAllowedOnRDN"
        entryAlreadyExists = "entryAlreadyExists"
        objectClassModsProhibited = "objectClassModsProhibited"
        affectsMultipleDSAs = "affectsMultipleDSAs"
        other = "other"

        def __init__(self, value: Optional[str] = None) -> None:
            """Instanciates a ResultCode ENUMERATED type object.
            By default, the object will be initialised to the first enumerated value.
            """
            if value is not None:
                if value not in self._fields.keys():
                    raise ValueError("%s not in permitted list of enumerators" % (value))
            else:
                value = self.success
            self._value = value

        @staticmethod
        def from_native_type(jsond: dict):
            """Obtain an instance of ResultCode from it's Python json dict representation."""
            return ExtendedResponse.ResultCode(jsond)

    @classmethod
    def _field_map(cls):
        return {
            "resultCode": LDAPResult.ResultCode,
            "matchedDN": AttributeDescription,
            "diagnosticMessage": AttributeDescription,
            "referral": Referral,
            "responseName": LDAPOID,
            "responseValue": OSS_OctetString,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a ExtendedResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[0]] = (list(self._fields.values())[0])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[1]] = (list(self._fields.values())[1])()
        # Create values for non-optional fields
        self._value[list(self._fields.keys())[2]] = (list(self._fields.values())[2])()

    @property
    def resultCode(self) -> ResultCode:
        """Get the value of the mandatory 'resultCode' field
        Use as:
            >>> myField = myObject.resultCode
        """
        return self._value.get("resultCode")

    @resultCode.setter
    def resultCode(self, val: ResultCode):
        """Set the value of the mandatory  'resultCode' field
        Use as:
            >>> myObject.resultCode = ResultCode()
        """
        if not isinstance(val, (self._fields["resultCode"],)):
            raise InvalidTypeParameter((self._fields["resultCode"],))
        self._value["resultCode"] = val

    @property
    def matchedDN(self) -> AttributeDescription:
        """Get the value of the mandatory 'matchedDN' field
        Use as:
            >>> myField = myObject.matchedDN
        """
        return self._value.get("matchedDN")

    @matchedDN.setter
    def matchedDN(self, val: AttributeDescription):
        """Set the value of the mandatory  'matchedDN' field
        Use as:
            >>> myObject.matchedDN = AttributeDescription()
        """
        if not isinstance(val, (self._fields["matchedDN"],)):
            raise InvalidTypeParameter((self._fields["matchedDN"],))
        self._value["matchedDN"] = val

    @property
    def diagnosticMessage(self) -> AttributeDescription:
        """Get the value of the mandatory 'diagnosticMessage' field
        Use as:
            >>> myField = myObject.diagnosticMessage
        """
        return self._value.get("diagnosticMessage")

    @diagnosticMessage.setter
    def diagnosticMessage(self, val: AttributeDescription):
        """Set the value of the mandatory  'diagnosticMessage' field
        Use as:
            >>> myObject.diagnosticMessage = AttributeDescription()
        """
        if not isinstance(val, (self._fields["diagnosticMessage"],)):
            raise InvalidTypeParameter((self._fields["diagnosticMessage"],))
        self._value["diagnosticMessage"] = val

    @property
    def referral(self) -> Union[Referral, None]:
        """Get the value of the optional 'referral' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.referral
        """
        return self._value.get("referral")

    @referral.setter
    def referral(self, val: Referral):
        """Set the value of the optional 'referral' field
        Use as:
            >>> myObject.referral = Referral()
        """
        if not isinstance(val, (self._fields["referral"],)):
            raise InvalidTypeParameter((self._fields["referral"],))
        self._value["referral"] = val

    @referral.deleter
    def referral(self):
        """Delete the optional 'referral' field
        Use as:
            >>> del myObject.referral
        """
        if "referral" in self._value:
            del self._value["referral"]

    @property
    def responseName(self) -> Union[LDAPOID, None]:
        """Get the value of the optional 'responseName' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.responseName
        """
        return self._value.get("responseName")

    @responseName.setter
    def responseName(self, val: LDAPOID):
        """Set the value of the optional 'responseName' field
        Use as:
            >>> myObject.responseName = LDAPOID()
        """
        if not isinstance(val, (self._fields["responseName"],)):
            raise InvalidTypeParameter((self._fields["responseName"],))
        self._value["responseName"] = val

    @responseName.deleter
    def responseName(self):
        """Delete the optional 'responseName' field
        Use as:
            >>> del myObject.responseName
        """
        if "responseName" in self._value:
            del self._value["responseName"]

    @property
    def responseValue(self) -> Union[OSS_OctetString, None]:
        """Get the value of the optional 'responseValue' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.responseValue
        """
        return self._value.get("responseValue")

    @responseValue.setter
    def responseValue(self, val: OSS_OctetString):
        """Set the value of the optional 'responseValue' field
        Use as:
            >>> myObject.responseValue = OSS_OctetString()
        """
        if not isinstance(val, (self._fields["responseValue"],)):
            raise InvalidTypeParameter((self._fields["responseValue"],))
        self._value["responseValue"] = val

    @responseValue.deleter
    def responseValue(self):
        """Delete the optional 'responseValue' field
        Use as:
            >>> del myObject.responseValue
        """
        if "responseValue" in self._value:
            del self._value["responseValue"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of ExtendedResponse from it's Python json dict representation."""
        obj = ExtendedResponse()
        vald = jsond["resultCode"]
        valo = LDAPResult.ResultCode.from_native_type(vald)
        obj.resultCode = valo
        vald = jsond["matchedDN"]
        valo = AttributeDescription.from_native_type(vald)
        obj.matchedDN = valo
        vald = jsond["diagnosticMessage"]
        valo = AttributeDescription.from_native_type(vald)
        obj.diagnosticMessage = valo
        if "referral" in jsond.keys():
            vald = jsond["referral"]
            valo = Referral.from_native_type(vald)
            obj.referral = valo
        if "responseName" in jsond.keys():
            vald = jsond["responseName"]
            valo = LDAPOID.from_native_type(vald)
            obj.responseName = valo
        if "responseValue" in jsond.keys():
            vald = jsond["responseValue"]
            valo = OSS_OctetString.from_native_type(vald)
            obj.responseValue = valo

        return obj


class IntermediateResponse(OSS_Sequence):
    @classmethod
    def _field_map(cls):
        return {
            "responseName": LDAPOID,
            "responseValue": OSS_OctetString,
        }

    _defaults = {}

    def __init__(self) -> None:
        """Instanciates a IntermediateResponse SEQUENCE type object.
        The object will contain all mandatory fields and no optional fields.
        """
        super().__init__()
        self._value = {}

    @property
    def responseName(self) -> Union[LDAPOID, None]:
        """Get the value of the optional 'responseName' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.responseName
        """
        return self._value.get("responseName")

    @responseName.setter
    def responseName(self, val: LDAPOID):
        """Set the value of the optional 'responseName' field
        Use as:
            >>> myObject.responseName = LDAPOID()
        """
        if not isinstance(val, (self._fields["responseName"],)):
            raise InvalidTypeParameter((self._fields["responseName"],))
        self._value["responseName"] = val

    @responseName.deleter
    def responseName(self):
        """Delete the optional 'responseName' field
        Use as:
            >>> del myObject.responseName
        """
        if "responseName" in self._value:
            del self._value["responseName"]

    @property
    def responseValue(self) -> Union[OSS_OctetString, None]:
        """Get the value of the optional 'responseValue' field.
        Will return ``None`` if the field is not present.
        Use as:
            >>> myField = myObject.responseValue
        """
        return self._value.get("responseValue")

    @responseValue.setter
    def responseValue(self, val: OSS_OctetString):
        """Set the value of the optional 'responseValue' field
        Use as:
            >>> myObject.responseValue = OSS_OctetString()
        """
        if not isinstance(val, (self._fields["responseValue"],)):
            raise InvalidTypeParameter((self._fields["responseValue"],))
        self._value["responseValue"] = val

    @responseValue.deleter
    def responseValue(self):
        """Delete the optional 'responseValue' field
        Use as:
            >>> del myObject.responseValue
        """
        if "responseValue" in self._value:
            del self._value["responseValue"]

    @staticmethod
    def from_native_type(jsond: dict):
        """Obtain an instance of IntermediateResponse from it's Python json dict representation."""
        obj = IntermediateResponse()
        if "responseName" in jsond.keys():
            vald = jsond["responseName"]
            valo = LDAPOID.from_native_type(vald)
            obj.responseName = valo
        if "responseValue" in jsond.keys():
            vald = jsond["responseValue"]
            valo = OSS_OctetString.from_native_type(vald)
            obj.responseValue = valo

        return obj
