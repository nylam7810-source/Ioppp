from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from app.core.database import Base


class SongSession(Base):
    __tablename__ = "song_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    session_name = Column(String)
    beat_file_path = Column(String, nullable=True)
    current_bar = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SessionMemory(Base):
    __tablename__ = "session_memory"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, index=True)  # Plain integer, no relationship
    
    # Beat analysis as JSON
    beat_analysis = Column(JSON, default={})
    
    # Vibe signature as JSON
    vibe_signature = Column(JSON, default={})
    
    # Lists of kept/rejected bars as JSON
    kept_bars = Column(JSON, default=[])
    rejected_bars = Column(JSON, default=[])
    
    # Artist influences as JSON
    artist_influences = Column(JSON, default=[])
    
    # Languages as JSON
    languages = Column(JSON, default=["en"])
    
    # AI context as JSON
    ai_context = Column(JSON, default={})
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
