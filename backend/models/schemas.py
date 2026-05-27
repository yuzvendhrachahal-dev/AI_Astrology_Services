from dataclasses import dataclass
from typing import Optional

@dataclass
class BirthData:
    name: str
    date: str  # YYYY-MM-DD
    time: Optional[str] = None  # HH:MM
    place: Optional[str] = None

@dataclass
class NamingPreferences:
    gender: Optional[str] = None
    origin: Optional[str] = None
    meanings: Optional[list] = None
