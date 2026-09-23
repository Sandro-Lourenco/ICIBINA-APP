from functools import lru_cache

from src.core.database.database import get_admin_supabase_client
from src.core.storage.repositories import StorageRepository
from src.core.storage.supabase_storage_repository import SupabaseStorageRepository
from src.modules.courses.domain.repositories import CourseRepository
from src.modules.courses.infrastructure.repositories.supabase_course_repository import (
    SupabaseCourseRepository,
)


@lru_cache(maxsize=4)
def _get_course_repository_for_client(client: object) -> CourseRepository:
    """Reuse repositories while the underlying Supabase client is unchanged.

    Keying the cache by client preserves the production singleton and also avoids
    leaking a stale client when tests or a controlled runtime swap the dependency.
    """
    return SupabaseCourseRepository(client)  # type: ignore[arg-type]


def get_course_repository() -> CourseRepository:
    return _get_course_repository_for_client(get_admin_supabase_client())


@lru_cache(maxsize=4)
def _get_storage_repository_for_client(client: object) -> StorageRepository:
    return SupabaseStorageRepository(client)  # type: ignore[arg-type]


def get_storage_repository() -> StorageRepository:
    return _get_storage_repository_for_client(get_admin_supabase_client())
