from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import uuid
from datetime import datetime

class SymptomEntry(Base):
    __tablename__ = "symptom_entries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    entry_date = Column(DateTime)

    input_type = Column(String)
    symptom_tags = Column(Text)
    body_parts_affected = Column(Text)

    severity_score = Column(Integer)
    duration = Column(String)
    frequency = Column(String)

    triggers = Column(Text)
    relieving_factors = Column(Text)

    stress_level = Column(Integer)
    affects_work = Column(Boolean)

    mood = Column(String)
    temperature_f = Column(Float)
    medications_taken = Column(Text)

    notes = Column(Text)
    raw_input = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SymptomPattern(Base):
    __tablename__ = "symptom_patterns"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    pattern_type = Column(String)
    related_symptom_ids = Column(Text)
    description = Column(Text)

    confidence_score = Column(Float)
    suggested_action = Column(String)

    user_acknowledged = Column(Boolean)

    detected_at = Column(DateTime, default=datetime.utcnow)

