from . import ChangeProps, Collections
from datetime import datetime, timezone, date
from pydantic import BaseModel, Field, EmailStr
from beanie import Document, PydanticObjectId, Indexed
from typing import Optional
from enum import Enum

class UserRoles(str, Enum):
    CITIZEN = "Citizen"
    AUTHORITY = "Authority"
    ADMIN = "Admin"
    SUPER_ADMIN = "SuperAdmin"


class PersonalInfo(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    phone_number: Optional[str]
    email: Optional[EmailStr] = None
    date_of_birth: date

class AccountDetails(BaseModel):
    username: str = Indexed(unique=True)
    password_hash: str

    recovery_email: Optional[EmailStr] = None
    recovery_phone: Optional[str] = None
    is_active: bool = True
    role: UserRoles = UserRoles.CITIZEN

    account_created_on : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class User(Document, ChangeProps):
    id: Optional[PydanticObjectId] = Field(None, alias="_id", description="Unique Id for User")
    personal_details: PersonalInfo
    account_details : AccountDetails

    class Settings:
        name = Collections.USERS
        indexes = ["account_details.username", "personal_details.email"]