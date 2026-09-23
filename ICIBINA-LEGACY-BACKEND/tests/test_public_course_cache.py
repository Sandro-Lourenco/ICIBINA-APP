from unittest.mock import AsyncMock, MagicMock

import pytest

from src.modules.courses.infrastructure.repositories.supabase_course_repository import (
    SupabaseCourseRepository,
)


@pytest.mark.asyncio
async def test_public_catalog_reuses_short_lived_snapshot() -> None:
    repository = SupabaseCourseRepository(MagicMock())
    expected: list = []
    repository._load_published_versions = AsyncMock(return_value=expected)  # type: ignore[method-assign]

    first = await repository.list_published_versions(limit=20)
    second = await repository.list_published_versions(limit=20)

    assert first is expected
    assert second is expected
    repository._load_published_versions.assert_awaited_once_with(20)  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_public_catalog_cache_is_invalidated_after_content_change() -> None:
    repository = SupabaseCourseRepository(MagicMock())
    repository._load_published_versions = AsyncMock(  # type: ignore[method-assign]
        side_effect=[[], []]
    )

    await repository.list_published_versions(limit=50)
    repository._invalidate_public_course_cache()
    await repository.list_published_versions(limit=50)

    assert repository._load_published_versions.await_count == 2  # type: ignore[attr-defined]
