from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from icibina.modules.courses.domain.entities import CourseStatus


class CourseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    slug: str
    title: str
    summary: str
    price_cents: int
    currency: str
    status: CourseStatus
    published_at: datetime | None
