from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import uuid
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    clerk_id = Column(String, unique=True, nullable=False)
    timezone = Column(String, default="UTC")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserHealthProfile(Base):
    __tablename__ = "user_health_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    age = Column(Integer)
    biological_sex = Column(String)
    blood_type = Column(String)

    chronic_conditions = Column(Text)
    current_medications = Column(Text)
    allergies = Column(Text)
    past_surgeries = Column(Text)

    primary_physician = Column(String)
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)

    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserInsurancePlan(Base):
    __tablename__ = "user_insurance_plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    plan_name = Column(String)
    insurer_name = Column(String)
    member_id = Column(String)
    group_number = Column(String)
    plan_type = Column(String)

    deductible_total = Column(Float)
    deductible_met = Column(Float)

    out_of_pocket_max = Column(Float)
    out_of_pocket_met = Column(Float)

    coverage_start = Column(Date)
    coverage_end = Column(Date)

    is_primary = Column(Boolean)

    front_card_key = Column(String)
    back_card_key = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
