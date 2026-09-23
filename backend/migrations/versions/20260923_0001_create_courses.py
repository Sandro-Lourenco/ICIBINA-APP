"""Create the courses catalog table.

Revision ID: 20260923_0001
Revises: None
Create Date: 2026-09-23
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "20260923_0001"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "courses",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("slug", sa.String(length=160), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("summary", sa.String(length=500), nullable=False),
        sa.Column("price_cents", sa.BigInteger(), server_default="0", nullable=False),
        sa.Column("currency", sa.String(length=3), server_default="BRL", nullable=False),
        sa.Column("status", sa.String(length=32), server_default="draft", nullable=False),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.CheckConstraint("price_cents >= 0", name="price_cents_nonnegative"),
        sa.CheckConstraint(
            "status IN ('draft', 'review_pending', 'published', 'archived')",
            name="status",
        ),
        sa.CheckConstraint(
            "status <> 'published' OR published_at IS NOT NULL",
            name="published_requires_published_at",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_courses"),
        sa.UniqueConstraint("slug", name="uq_courses_slug"),
    )
    op.create_index(
        "ix_courses_status_published_at", "courses", ["status", sa.text("published_at DESC")]
    )


def downgrade() -> None:
    op.drop_index("ix_courses_status_published_at", table_name="courses")
    op.drop_table("courses")
