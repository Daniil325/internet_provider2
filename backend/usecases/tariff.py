from dataclasses import dataclass
from typing import Any
from uuid import UUID

from backend.core.entities import Tariff
from backend.infra.database import SqlTariffRepo


@dataclass
class CreateTariffDto:
    name: str
    descripiton: str
    price: int


@dataclass
class CreateTariffCommand:
    repo: SqlTariffRepo
    
    async def __call__(self, dto: CreateTariffDto):
        identity = self.repo.new_id()
        obj = Tariff(identity, dto.name, dto.descripiton, dto.price)
        await self.repo.add(obj)
        return identity
    
    
@dataclass
class UpdateTariffDto(CreateTariffDto):
    id: UUID
    
    
@dataclass
class UpdateTariffCommand:
    repo: SqlTariffRepo
    
    async def __call__(self, dto: UpdateTariffDto, update_obj: dict[str, Any]) -> str:
        await self.repo.update(dto.id, update_obj)
        return dto.id
    

@dataclass
class DeleteTariffCommand:
    repo: SqlTariffRepo
    
    async def __call__(self, id: UUID) -> None:
        await self.repo.delete(id)
        return id
