from datetime import UTC, datetime
from uuid import uuid4

import pytest

from icibina.modules.courses.domain.entities import Course, CourseStatus


def test_published_course_requires_publication_time() -> None:
    now = datetime.now(UTC)
    with pytest.raises(ValueError, match="published_at"):
        Course(
            id=uuid4(),
            slug="invalid",
            title="Invalid",
            summary="Missing publication time",
            price_cents=0,
            currency="BRL",
            status=CourseStatus.PUBLISHED,
            published_at=None,
            created_at=now,
            updated_at=now,
        )
