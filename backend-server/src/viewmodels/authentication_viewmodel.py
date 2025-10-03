from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUserRequest(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    phone_number: Optional[str] = None
    email: EmailStr
    date_of_birth: Optional[date] = None

    username: str
    password: str   # plaintext only in request, will be hashed before saving
    recovery_email: Optional[EmailStr] = None
    recovery_phone: Optional[str] = None

class CreateUserResponse(BaseModel):
    pass