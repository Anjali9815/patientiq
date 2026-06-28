from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import uuid
from datetime import datetime

class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    doc_type = Column(String)
    file_bucket = Column(String)
    file_key = Column(String)
    original_filename = Column(String)
    mime_type = Column(String)

    file_size_bytes = Column(Integer)
    page_count = Column(Integer)

    checksum_sha256 = Column(String)
    ocr_status = Column(String)

    extracted_text = Column(String)
    encryption_key_id = Column(String)

    status = Column(String)
    error_message = Column(String)

    uploaded_at = Column(DateTime, default=datetime.utcnow)
    processed_at = Column(DateTime)

