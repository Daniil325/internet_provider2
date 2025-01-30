from dataclasses import dataclass
from uuid import UUID

from backend.core.entities import ChosenTariff
from backend.infra.database import SqlChosenTariffRepo


@dataclass
class CreateChosenTariffDto:
    client_id: UUID
    tariff_id: UUID


@dataclass
class CreateChosenTariffCommand:
    repo: SqlChosenTariffRepo
    
    async def __call__(self, dto: CreateChosenTariffDto):
        identity = self.repo.new_id()
        obj = ChosenTariff(identity, dto.client_id, dto.tariff_id)
        await self.repo.add(obj)
        return identity