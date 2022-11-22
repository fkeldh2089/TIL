from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AuthStandardImg(Base):
    __tablename__ = "auth_standard_img"

    auth_standard_img_id = Column(Integer, primary_key=True, index=True)
    participation_id = Column(Integer, ForeignKey("users.id"))
    standard_img = Column(String)


class Feed(Base):
    __tablename__ = "feed"

    feed_id = Column(Integer, primary_key=True, index=True)
    feed_type = Column(String, index=True)
    participation_id = Column(Integer, ForeignKey("users.id"))
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    # time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    feed_img = Column(String)
    feed_content = Column(String)

    owner = relationship("User", back_populates="items")