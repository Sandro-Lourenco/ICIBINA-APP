from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import BigInteger, CheckConstraint, DateTime, Index, String, text
from sqlalchemy.orm import Mapped, mapped_column

from icibina.infrastructure.database.base import Base


class CourseModel(Base):
    __tablename__ = "courses"
    __table_args__ = (
        CheckConstraint("price_cents >= 0", name="price_cents_nonnegative"),
        CheckConstraint(
            "status IN ('draft', 'review_pending', 'published', 'archived')",
            name="status",
        ),
        CheckConstraint(
            "status <> 'published' OR published_at IS NOT NULL",
            name="published_requires_published_at",
        ),
        Index("ix_courses_status_published_at", "status", text("published_at DESC")),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    slug: Mapped[str] = mapped_column(String(160), unique=True)
    title: Mapped[str] = mapped_column(String(200))
    summary: Mapped[str] = mapped_column(String(500))
    price_cents: Mapped[int] = mapped_column(BigInteger, server_default="0")
    currency: Mapped[str] = mapped_column(String(3), server_default="BRL")
    status: Mapped[str] = mapped_column(String(32), server_default="draft")
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()")
    )
