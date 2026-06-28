from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import uuid
from datetime import datetime


class AIResult(Base):
    __tablename__ = "ai_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    source_type = Column(String)
    source_id = Column(UUID(as_uuid=True))

    feature = Column(String)
    model_used = Column(String)
    model_version = Column(String)

    raw_prompt = Column(Text)
    system_prompt = Column(Text)

    ai_output = Column(Text)
    structured_output = Column(Text)

    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)
    total_tokens = Column(Integer)

    latency_ms = Column(Float)
    estimated_cost_usd = Column(Float)

    status = Column(String)
    error_message = Column(Text)

    retry_count = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

