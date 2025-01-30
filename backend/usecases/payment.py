from dataclasses import dataclass
from uuid import UUID

from backend.core.entities import Payment
from backend.infra.database import SqlPaymentRepo


@dataclass
class CreatePaymentDto:
    client_id: UUID
    amount: int


@dataclass
class CreatePaymentCommand:
    repo: SqlPaymentRepo
    
    async def __call__(self, dto: CreatePaymentDto):
        identity = self.repo.new_id()
        payment = Payment(identity, dto.client_id, dto.amount)
        await self.repo.add(payment)
        return identity
    