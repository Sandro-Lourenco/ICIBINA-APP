from icibina.modules.courses.domain.entities import Course, CourseStatus
from icibina.modules.courses.infrastructure.models import CourseModel


def course_to_domain(model: CourseModel) -> Course:
    return Course(
        id=model.id,
        slug=model.slug,
        title=model.title,
        summary=model.summary,
        price_cents=model.price_cents,
        currency=model.currency,
        status=CourseStatus(model.status),
        published_at=model.published_at,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )
