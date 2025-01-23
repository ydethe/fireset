from typing import List, Optional, Dict
import aiosqlite
import json
from pathlib import Path
from .Contact import Contact

class Database:
    def __init__(self, db_path: str = "cardav.db"):
        self.db_path = db_path
        
    async def initialize(self):
        """Initialize the database with required tables"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            await db.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    uid TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    vcard TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (username) REFERENCES users(username)
                )
            """)
            
            await db.execute("""
                CREATE TABLE IF NOT EXISTS addressbooks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(username, name),
                    FOREIGN KEY (username) REFERENCES users(username)
                )
            """)
            await db.commit()
            
    async def add_contact(self, username: str, contact: Contact) -> bool:
        """Add or update a contact in the database"""
        async with aiosqlite.connect(self.db_path) as db:
            try:
                await db.execute("""
                    INSERT OR REPLACE INTO contacts (uid, username, vcard)
                    VALUES (?, ?, ?)
                """, (contact.uid, username, contact.to_vcard()))
                await db.commit()
                return True
            except Exception as e:
                return False
                
    async def get_contact(self, username: str, uid: str) -> Optional[Contact]:
        """Retrieve a contact by UID"""
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(
                "SELECT vcard FROM contacts WHERE username = ? AND uid = ?",
                (username, uid)
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return Contact.from_vcard(row[0])
                return None
                
    async def get_all_contacts(self, username: str) -> List[Contact]:
        """Retrieve all contacts for a user"""
        contacts = []
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(
                "SELECT vcard FROM contacts WHERE username = ?",
                (username,)
            ) as cursor:
                async for row in cursor:
                    contacts.append(Contact.from_vcard(row[0]))
        return contacts
        
    async def delete_contact(self, username: str, uid: str) -> bool:
        """Delete a contact"""
        async with aiosqlite.connect(self.db_path) as db:
            try:
                await db.execute(
                    "DELETE FROM contacts WHERE username = ? AND uid = ?",
                    (username, uid)
                )
                await db.commit()
                return True
            except Exception as e:
                return False
