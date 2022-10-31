from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.database import Base, GUID, GUID_SERVER_DEFAULT_POSTGRESQL
import datetime

class PermissionModel(Base):
    __tablename__ = "permissions"

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    menu_id = Column(GUID, ForeignKey("menus.id"), nullable=False)
    name = Column(String(50), nullable=False)
    alias = Column(String(50))
    url = Column(String(50))
    icon = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

    roles = relationship("RolePermissionModel", back_populates="permissions")
    menu = relationship("MenuModel", back_populates="permissions")

class MenuModel(Base):
    __tablename__ = "menus"

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String(50), nullable=False)
    icon = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

    permissions = relationship("PermissionModel", back_populates="menu")
    
class RolePermissionModel(Base):
    __tablename__ = "role_permission"

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    role_id = Column(GUID, ForeignKey("roles.id"), nullable=False)
    permission_id = Column(GUID, ForeignKey("permissions.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

    roles = relationship("RoleModel", back_populates="permissions")
    permissions = relationship("PermissionModel", back_populates="roles")
