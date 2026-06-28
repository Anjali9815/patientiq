from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select
from schemas.symptom import SymptomCreate
from core.database import AsyncSessionLocal
from models.symptom import SymptomEntry
from models.user import User

router = APIRouter()

from core.auth import get_current_user
from fastapi import Depends
@router.post("/symptoms/test")
async def create_symptom_test(symptom: SymptomCreate):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.email == "test@patientiq.com")
        )
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="Test user not found")
        
        db_symptom = SymptomEntry(
            user_id=user.id,
            raw_input=symptom.raw_input,
            entry_date=symptom.occurred_at,
            input_type=symptom.input_type,
            severity_score=symptom.severity_score,
            notes=symptom.notes
        )
        session.add(db_symptom)
        await session.commit()
        await session.refresh(db_symptom)
        return {
            "message": "Symptom created",
            "id": str(db_symptom.id)
        }