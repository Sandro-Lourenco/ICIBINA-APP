from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from src.core.security.security import CurrentUser, get_current_user
from src.main import app
from src.modules.assessments.domain.entities import Task
from src.modules.assessments.interface.api.dependencies import get_assessment_repository
from src.modules.courses.interface.api.dependencies import get_course_repository


client = TestClient(app)


@pytest.fixture
def teacher_user() -> CurrentUser:
    return CurrentUser(id="teacher_123", email="teacher@lawrence.com", role="teacher")


@pytest.fixture
def student_user() -> CurrentUser:
    return CurrentUser(id="student_123", email="student@lawrence.com", role="student")


def override_dependencies(
    user: CurrentUser,
    assessment_repository: AsyncMock,
    course_repository: AsyncMock,
) -> None:
    app.dependency_overrides[get_current_user] = lambda: user
    app.dependency_overrides[get_assessment_repository] = lambda: assessment_repository
    app.dependency_overrides[get_course_repository] = lambda: course_repository


def make_task(*, title: str = "Atividade prática") -> Task:
    return Task(
        id="task_abc",
        course_id="course_123",
        lesson_id="lesson_123",
        title=title,
        task_type="essay",
        description="Faça uma costura francesa.",
        max_attempts=2,
        passing_score=Decimal("7.0"),
    )


def test_create_task_by_teacher(teacher_user: CurrentUser) -> None:
    assessment_repository = AsyncMock()
    assessment_repository.save_task.return_value = make_task(title="Nova atividade prática")
    course_repository = AsyncMock()
    course_repository.get_instructor_id.return_value = "teacher_123"
    course_repository.get_lesson_by_id.return_value = SimpleNamespace(id="lesson_123")
    override_dependencies(teacher_user, assessment_repository, course_repository)

    try:
        response = client.post(
            "/api/v1/tasks",
            json={
                "course_id": "course_123",
                "lesson_id": "lesson_123",
                "title": "Nova atividade prática",
                "task_type": "essay",
                "description": "Faça uma costura francesa.",
                "max_attempts": 2,
                "passing_score": 7.0,
            },
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 201
    assert response.json()["data"]["id"] == "task_abc"
    assessment_repository.save_task.assert_awaited_once()


def test_create_task_forbidden_for_student(student_user: CurrentUser) -> None:
    override_dependencies(student_user, AsyncMock(), AsyncMock())
    try:
        response = client.post(
            "/api/v1/tasks",
            json={
                "course_id": "course_123",
                "lesson_id": "lesson_123",
                "title": "Tentativa do aluno",
                "task_type": "essay",
            },
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 403


def test_create_task_bola_protection(teacher_user: CurrentUser) -> None:
    assessment_repository = AsyncMock()
    course_repository = AsyncMock()
    course_repository.get_instructor_id.return_value = "teacher_different"
    override_dependencies(teacher_user, assessment_repository, course_repository)

    try:
        response = client.post(
            "/api/v1/tasks",
            json={
                "course_id": "course_123",
                "lesson_id": "lesson_123",
                "title": "Proteção BOLA",
                "task_type": "essay",
            },
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 403
    assert "Acesso negado" in response.json()["error"]["message"]
    assessment_repository.save_task.assert_not_awaited()


def test_update_task_by_teacher(teacher_user: CurrentUser) -> None:
    assessment_repository = AsyncMock()
    assessment_repository.get_task_by_id.return_value = make_task()
    assessment_repository.save_task.return_value = make_task(title="Atividade prática atualizada")
    course_repository = AsyncMock()
    course_repository.get_instructor_id.return_value = "teacher_123"
    override_dependencies(teacher_user, assessment_repository, course_repository)

    try:
        response = client.patch(
            "/api/v1/tasks/task_abc",
            json={"title": "Atividade prática atualizada"},
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json()["data"]["title"] == "Atividade prática atualizada"


def test_delete_task_by_teacher(teacher_user: CurrentUser) -> None:
    assessment_repository = AsyncMock()
    assessment_repository.get_task_by_id.return_value = make_task()
    course_repository = AsyncMock()
    course_repository.get_instructor_id.return_value = "teacher_123"
    override_dependencies(teacher_user, assessment_repository, course_repository)

    try:
        response = client.delete("/api/v1/tasks/task_abc")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assessment_repository.delete_task.assert_awaited_once_with("task_abc")
