from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from datetime import datetime

class Status(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class IssueBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Status = Status.OPEN
    priority: Priority = Priority.MEDIUM
    assignee: Optional[str] = None

class IssueCreate(IssueBase):
    pass

class IssueUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Status] = None
    priority: Optional[Priority] = None
    assignee: Optional[str] = None

class Issue(IssueBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True