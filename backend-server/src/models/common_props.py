from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChangeProps(BaseModel):
    created_on : datetime
    created_by: Optional[str]
    last_updated_on: datetime
    last_updated_by: Optional[str]
    