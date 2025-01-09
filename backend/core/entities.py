from dataclasses import dataclass
from uuid import UUID


@dataclass
class Entity:
    id: UUID
    

@dataclass
class Tariff(Entity):
    name: str
    descripiton: str
    price: int
    

@dataclass
class Client(Entity):
    fio: str
    phone: str
    email: str
    username: str
    password: str
    

@dataclass
class ChosenTariff(Entity):
    client_id: UUID
    tariff_id: UUID
    
    
@dataclass
class Payment(Entity):
    client_id: UUID
    amount: int
