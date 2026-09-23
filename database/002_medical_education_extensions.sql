-- Reference blueprint only. Convert to Alembic migrations in the real backend.
-- Governance extensions for integrative-medical education.

CREATE TABLE instructor_credentials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    credential_type TEXT NOT NULL,
    title TEXT NOT NULL,
    issuer TEXT,
    jurisdiction TEXT,
    credential_identifier TEXT,
    verified_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    public_display BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX ix_instructor_credentials_user ON instructor_credentials(user_id);

CREATE TABLE course_references (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    citation TEXT NOT NULL,
    doi TEXT,
    pmid TEXT,
    url TEXT,
    position INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (position >= 0)
);
CREATE INDEX ix_course_references_course_position ON course_references(course_id, position);

CREATE TABLE lesson_references (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lesson_id UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    citation TEXT NOT NULL,
    doi TEXT,
    pmid TEXT,
    url TEXT,
    position INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (position >= 0)
);
CREATE INDEX ix_lesson_references_lesson_position ON lesson_references(lesson_id, position);

CREATE TABLE course_disclosures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    instructor_user_id UUID NOT NULL REFERENCES users(id),
    has_conflict BOOLEAN NOT NULL DEFAULT FALSE,
    statement TEXT NOT NULL,
    reviewed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(course_id, instructor_user_id)
);

CREATE TABLE course_content_reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    reviewer_user_id UUID NOT NULL REFERENCES users(id),
    review_type TEXT NOT NULL CHECK (review_type IN ('editorial','scientific','clinical','compliance')),
    status TEXT NOT NULL CHECK (status IN ('pending','changes_requested','approved','rejected','superseded')),
    notes TEXT,
    reviewed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX ix_course_content_reviews_course_status ON course_content_reviews(course_id, status, created_at DESC);

CREATE TABLE course_education_credits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    credit_type TEXT NOT NULL,
    accreditor TEXT NOT NULL,
    credit_hours NUMERIC(7,2) NOT NULL CHECK (credit_hours > 0),
    valid_from DATE,
    valid_until DATE,
    evidence_storage_key TEXT,
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft','verified','expired','revoked')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (valid_until IS NULL OR valid_from IS NULL OR valid_until >= valid_from)
);
CREATE INDEX ix_course_education_credits_course_status ON course_education_credits(course_id, status);
