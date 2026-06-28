from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import uuid
from datetime import datetime

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    type = Column(String)
    title = Column(String)
    body = Column(Text)
    channel = Column(String)

    extra_data = Column(Text)

    scheduled_at = Column(DateTime)
    sent_at = Column(DateTime)
    read_at = Column(DateTime)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    action = Column(String)
    resource_type = Column(String)
    resource_id = Column(UUID(as_uuid=True))

    ip_address = Column(String)
    user_agent = Column(String)

    extra_data = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
