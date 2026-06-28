from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class SymptomCreate(BaseModel):
    raw_input: str
    severity_score: int
    input_type: str = "text"
    occurred_at: datetime
    notes: Optional[str] = None

    @validator('occurred_at')
    def remove_timezone(cls, v):
        return v.replace(tzinfo=None)