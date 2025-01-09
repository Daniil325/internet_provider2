from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from backend.core.entities import ChosenTariff, Client, Payment, Tariff


class TariffRepo(ABC):
    
    @abstractmethod
    async def get_all(self) -> list[Tariff]:
        ...
        
    @abstractmethod
    async def get_by_id(self, id: UUID) -> Tariff:
        ...
        
    @abstractmethod
    async def add(self, tariff: Tariff):
        ...
    
    @abstractmethod
    async def update(self, id: UUID, obj: dict[str, Any]):
        ...
    
    @abstractmethod
    async def delete(self, id: UUID):
        ...
    

class ClientRepo(ABC):
    
    @abstractmethod
    async def get_all(self) -> list[Client]:
        ...
        
    @abstractmethod
    async def get_by_id(self, id: UUID) -> Client | None:
        ...
        
    @abstractmethod
    async def add(self, client: Client):
        ...
    
    @abstractmethod
    async def update(self, id: UUID, obj: dict[str, Any]):
        ...
    
    @abstractmethod
    async def delete(self, id: UUID):
        ...
        
    @abstractmethod
    async def get_by_email(self, email: str) -> Client | None:
        ...
        

class ChosenTariffRepo(ABC):
    
    @abstractmethod
    async def get_all(self) -> list[ChosenTariff]:
        ...
        
    @abstractmethod
    async def get_by_id(self, id: UUID) -> ChosenTariff:
        ...
        
    @abstractmethod
    async def add(self, chosen_tariff: ChosenTariff):
        ...
    
    @abstractmethod
    async def update(self, id: UUID, obj: dict[str, Any]):
        ...
    
    @abstractmethod
    async def delete(self, id: UUID):
        ...
        

class PaymentRepo(ABC):
    
    @abstractmethod
    async def get_all(self) -> list[Payment]:
        ...
        
    @abstractmethod
    async def get_by_id(self, id: UUID) -> Payment:
        ...
        
    @abstractmethod
    async def add(self, payment: Payment):
        ...
    
    @abstractmethod
    async def update(self, id: UUID, obj: dict[str, Any]):
        ...
    
    @abstractmethod
    async def delete(self, id: UUID):
        ...