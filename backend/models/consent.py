from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import uuid
from datetime import datetime
class ConsentForm(Base):
    __tablename__ = "consent_forms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"))

    procedure_name = Column(String)
    procedure_code = Column(String)
    provider_name = Column(String)
    facility_name = Column(String)

    procedure_date = Column(Date)

    anesthesia_type = Column(String)
    risks_identified = Column(Text)
    alternatives_listed = Column(Text)

    patient_signed = Column(Boolean)

    decode_status = Column(String)
    plain_language_summary = Column(Text)
    questions_to_ask = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
