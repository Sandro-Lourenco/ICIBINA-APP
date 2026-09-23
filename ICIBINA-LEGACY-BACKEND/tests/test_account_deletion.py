from datetime import datetime, timezone
from decimal import Decimal
from unittest.mock import AsyncMock

from fastapi.testclient import TestClient

from src.core.security.security import CurrentUser, get_current_user
from src.main import app
from src.modules.profiles.application.use_cases.delete_my_account_use_case import (
    DeleteMyAccountUseCase,
)
from src.modules.profiles.interface.api.dependencies import get_profile_repository
from src.modules.subscriptions.domain.entities import Subscription
from src.modules.subscriptions.interface.api.dependencies import (
    get_subscription_gateway,
    get_subscription_repository,
)


def subscription(*, already_cancelled: bool = False) -> Subscription:
    now = datetime.now(timezone.utc)
    return Subscription(
        id="subscription-1",
        student_id="student-1",
        course_id="course-1",
        provider="stripe",
        provider_customer_id="customer-1",
        provider_subscription_id="provider-subscription-1",
        status="active",
        monthly_price=Decimal("59.90"),
        currency="BRL",
        current_period_start=now,
        current_period_end=now,
        cancel_at_period_end=already_cancelled,
    )


async def test_delete_account_cancels_renewal_before_anonymizing_and_disabling() -> None:
    profile_repository = AsyncMock()
    profile_repository.anonymize_account.return_value = "request-1"
    subscription_repository = AsyncMock()
    subscription_repository.get_by_student.return_value = [subscription()]
    gateway = AsyncMock()

    result = await DeleteMyAccountUseCase(
        profile_repository, subscription_repository, gateway
    ).execute("student-1")

    assert result == "request-1"
    gateway.cancel_at_period_end.assert_awaited_once()
    profile_repository.anonymize_account.assert_awaited_once_with("student-1")
    profile_repository.disable_auth_account.assert_awaited_once_with("student-1")


async def test_delete_account_does_not_cancel_an_already_scheduled_subscription() -> None:
    profile_repository = AsyncMock()
    profile_repository.anonymize_account.return_value = "request-1"
    subscription_repository = AsyncMock()
    subscription_repository.get_by_student.return_value = [subscription(already_cancelled=True)]
    gateway = AsyncMock()

    await DeleteMyAccountUseCase(profile_repository, subscription_repository, gateway).execute(
        "student-1"
    )

    gateway.cancel_at_period_end.assert_not_awaited()


def test_delete_my_account_api_uses_only_the_authenticated_user() -> None:
    profile_repository = AsyncMock()
    profile_repository.anonymize_account.return_value = "request-1"
    subscription_repository = AsyncMock()
    subscription_repository.get_by_student.return_value = []
    gateway = AsyncMock()
    app.dependency_overrides[get_current_user] = lambda: CurrentUser(
        id="student-1", email="student@example.com", role="student"
    )
    app.dependency_overrides[get_profile_repository] = lambda: profile_repository
    app.dependency_overrides[get_subscription_repository] = lambda: subscription_repository
    app.dependency_overrides[get_subscription_gateway] = lambda: gateway

    try:
        response = TestClient(app).delete("/api/v1/profiles/me")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json()["data"] == {
        "request_id": "request-1",
        "account_status": "deleted",
    }
    profile_repository.disable_auth_account.assert_awaited_once_with("student-1")
