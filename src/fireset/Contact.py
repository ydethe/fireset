from dataclasses import dataclass
from typing import Dict, List, Optional
import vobject
import uuid

@dataclass
class Contact:
    uid: str
    full_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    raw_vcard: Optional[str] = None

    @classmethod
    def from_vcard(cls, vcard_str: str) -> 'Contact':
        """Create a Contact instance from a vCard string"""
        vcard = vobject.readOne(vcard_str)
        
        return cls(
            uid=str(getattr(vcard, 'uid', uuid.uuid4())),
            full_name=str(vcard.fn.value),
            email=str(vcard.email.value) if hasattr(vcard, 'email') else None,
            phone=str(vcard.tel.value) if hasattr(vcard, 'tel') else None,
            address=str(vcard.adr.value) if hasattr(vcard, 'adr') else None,
            raw_vcard=vcard_str
        )

    def to_vcard(self) -> str:
        """Convert Contact to vCard format"""
        if self.raw_vcard:
            return self.raw_vcard
            
        vcard = vobject.vCard()
        vcard.add('fn').value = self.full_name
        vcard.add('uid').value = self.uid
        
        if self.email:
            vcard.add('email').value = self.email
        if self.phone:
            vcard.add('tel').value = self.phone
        if self.address:
            vcard.add('adr').value = self.address
            
        return vcard.serialize()
