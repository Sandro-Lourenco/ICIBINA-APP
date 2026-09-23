"""Harden course constraint names and publication invariant.

This compatibility revision repairs databases that applied the original baseline
before its naming-convention inputs were corrected. Fresh databases already have
the final names after revision 0001, so every operation is conditional.

Revision ID: 20260923_0002
Revises: 20260923_0001
Create Date: 2026-09-23
"""

from collections.abc import Sequence

from alembic import op

revision: str = "20260923_0002"
down_revision: str | Sequence[str] | None = "20260923_0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Raw SQL is required here because this revision must support both the old
    # applied baseline and the corrected clean-install baseline idempotently.
    op.execute(
        """
        DO $$
        BEGIN
          IF EXISTS (
            SELECT 1 FROM pg_constraint
            WHERE conname = 'ck_courses_ck_courses_price_cents_nonnegative'
              AND conrelid = 'courses'::regclass
          ) THEN
            ALTER TABLE courses
              RENAME CONSTRAINT ck_courses_ck_courses_price_cents_nonnegative
              TO ck_courses_price_cents_nonnegative;
          END IF;

          IF EXISTS (
            SELECT 1 FROM pg_constraint
            WHERE conname = 'ck_courses_ck_courses_status'
              AND conrelid = 'courses'::regclass
          ) THEN
            ALTER TABLE courses
              RENAME CONSTRAINT ck_courses_ck_courses_status
              TO ck_courses_status;
          END IF;

          IF NOT EXISTS (
            SELECT 1 FROM pg_constraint
            WHERE conname = 'ck_courses_published_requires_published_at'
              AND conrelid = 'courses'::regclass
          ) THEN
            ALTER TABLE courses
              ADD CONSTRAINT ck_courses_published_requires_published_at
              CHECK (status <> 'published' OR published_at IS NOT NULL);
          END IF;
        END $$;
        """
    )


def downgrade() -> None:
    # Revision 0001 now represents the corrected baseline, so no schema reversal
    # is necessary when moving back one revision. Recovery is roll-forward.
    pass
