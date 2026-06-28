from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import uuid
from datetime import datetime



class Bill(Base):
    __tablename__ = "bills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"))
    insurance_plan_id = Column(UUID(as_uuid=True), ForeignKey("user_insurance_plans.id"))

    provider_name = Column(String)
    provider_npi = Column(String)
    provider_address = Column(String)
    facility_type = Column(String)

    total_billed = Column(Float)
    total_allowed = Column(Float)
    total_paid_by_insurance = Column(Float)
    patient_responsibility = Column(Float)
    amount_paid = Column(Float)
    amount_disputed = Column(Float)

    bill_status = Column(String)
    dispute_status = Column(String)
    claim_number = Column(String)

    service_date_start = Column(Date)
    service_date_end = Column(Date)
    bill_received_date = Column(Date)

    diagnosis_codes = Column(Text)
    notes = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BillLineItem(Base):
    __tablename__ = "bill_line_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bill_id = Column(UUID(as_uuid=True), ForeignKey("bills.id"))

    cpt_code = Column(String)
    cpt_description = Column(String)
    revenue_code = Column(String)
    modifier_codes = Column(String)

    units = Column(Integer)

    billed_amount = Column(Float)
    allowed_amount = Column(Float)
    paid_amount = Column(Float)
    patient_portion = Column(Float)

    flag_type = Column(String)
    flag_reason = Column(String)
    potential_savings = Column(Float)

    is_disputed = Column(Boolean)
    is_duplicate = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)

class AppealLetter(Base):
    __tablename__ = "appeal_letters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    bill_id = Column(UUID(as_uuid=True), ForeignKey("bills.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    appeal_type = Column(String)
    letter_content = Column(Text)

    status = Column(String)
    sent_via = Column(String)

    deadline_date = Column(Date)
    sent_date = Column(Date)

    response_id = Column(String)
    response_outcome = Column(String)

    amount_recovered = Column(Float)
    insurer_response_notes = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

