from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.database import Base, GUID, GUID_SERVER_DEFAULT_POSTGRESQL
import datetime

class RoleModel(Base):
    __tablename__ = "roles"

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

    users = relationship("UserModel", back_populates="role", lazy="joined")
    permissions = relationship("RolePermissionModel", back_populates="roles", lazy="joined")
