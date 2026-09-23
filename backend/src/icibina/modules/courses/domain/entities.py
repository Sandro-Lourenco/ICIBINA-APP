from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from uuid import UUID


class CourseStatus(StrEnum):
    DRAFT = "draft"
    REVIEW_PENDING = "review_pending"
    PUBLISHED = "published"
    ARCHIVED = "archived"


@dataclass(frozen=True, slots=True)
class Course:
    id: UUID
    slug: str
    title: str
    summary: str
    price_cents: int
    currency: str
    status: CourseStatus
    published_at: datetime | None
    created_at: datetime
    updated_at: datetime

    def __post_init__(self) -> None:
        if self.status is CourseStatus.PUBLISHED and self.published_at is None:
            raise ValueError("published courses require published_at")
