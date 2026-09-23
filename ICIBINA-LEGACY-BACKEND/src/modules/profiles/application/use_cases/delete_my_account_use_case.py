from src.modules.profiles.domain.repositories import ProfileRepository
from src.modules.subscriptions.domain.gateways import SubscriptionGateway
from src.modules.subscriptions.domain.repositories import SubscriptionRepository


class DeleteMyAccountUseCase:
    """Cancela renovações, anonimiza dados e desabilita a identidade do usuário."""

    def __init__(
        self,
        profile_repository: ProfileRepository,
        subscription_repository: SubscriptionRepository,
        subscription_gateway: SubscriptionGateway,
    ) -> None:
        self.profile_repository = profile_repository
        self.subscription_repository = subscription_repository
        self.subscription_gateway = subscription_gateway

    async def execute(self, user_id: str) -> str:
        subscriptions = await self.subscription_repository.get_by_student(user_id)
        for subscription in subscriptions:
            if subscription.cancel_at_period_end or subscription.status in {
                "canceled",
                "cancelled",
            }:
                continue
            await self.subscription_gateway.cancel_at_period_end(subscription)

        request_id = await self.profile_repository.anonymize_account(user_id)
        await self.profile_repository.disable_auth_account(user_id)
        return request_id
